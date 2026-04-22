# /// script
# dependencies = [
#   "gql[requests]",
# ]
# ///
import argparse
import json
import os
from dataclasses import asdict, dataclass
from datetime import UTC, datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport

CACHE_FILE_DEFAULT = Path("cache.json")
CACHE_TTL = timedelta(hours=24)


@dataclass(frozen=True, slots=True)
class RepoSpec:
    owner: str
    name: str

    @property
    def key(self) -> str:
        return f"{self.owner}/{self.name}"

    @staticmethod
    def parse(value: str) -> RepoSpec:
        if "/" not in value:
            raise ValueError(f"Invalid repo format: {value!r}. Expected 'owner/repo'.")
        owner, name = value.split("/", 1)
        if not owner or not name:
            raise ValueError(f"Invalid repo format: {value!r}. Expected 'owner/repo'.")
        return RepoSpec(owner=owner, name=name)


@dataclass
class RepoStats:
    num_stars: int
    num_commits: int
    latest_commit_date: str | None

    def to_public_dict(self) -> dict[str, Any]:
        return asdict(self)


class Cache:
    def __init__(self, path: Path):
        self.path = path
        self.data: dict[str, Any] = self._load()

    def _load(self) -> dict[str, Any]:
        if self.path.exists():
            with self.path.open("r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def save(self) -> None:
        with self.path.open("w", encoding="utf-8") as f:
            json.dump(self.data, f, sort_keys=True)

    @staticmethod
    def _parse_dt(value: str) -> datetime:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))

    def is_fresh(self, key: str) -> bool:
        entry = self.data.get(key)
        if not entry or "cached_at" not in entry:
            return False
        try:
            cached_at = self._parse_dt(entry["cached_at"])
        except Exception:
            return False
        return datetime.now(UTC) - cached_at < CACHE_TTL

    def get_stats(self, key: str) -> RepoStats | None:
        entry = self.data.get(key)
        if not entry or not self.is_fresh(key):
            return None
        return RepoStats(
            num_stars=entry["num_stars"],
            num_commits=entry["num_commits"],
            latest_commit_date=entry["latest_commit_date"],
        )

    def set_stats(self, key: str, stats: RepoStats) -> None:
        self.data[key] = {
            **asdict(stats),
            "cached_at": datetime.now(UTC).isoformat(),
        }
        self.save()


class GitHubRepoFetcher:
    def __init__(self, token: str, user_id: str):
        transport = RequestsHTTPTransport(
            url="https://api.github.com/graphql",
            headers={"Authorization": f"Bearer {token}"},
            use_json=True,
        )
        self.client = Client(transport=transport, fetch_schema_from_transport=False)
        self.user_id = user_id

        self.query = gql("""
        query($owner: String!, $repo: String!, $user_id: ID!) {
          repository(owner: $owner, name: $repo) {
            stargazerCount
            defaultBranchRef {
              target {
                ... on Commit {
                  userHistory: history(author: { id: $user_id }) {
                    totalCount
                  }
                  latestHistory: history(first: 1) {
                    nodes {
                      committedDate
                    }
                  }
                }
              }
            }
          }
        }
        """)

    def fetch(self, repo: RepoSpec) -> RepoStats:
        result = self.client.execute(
            self.query,
            variable_values={
                "owner": repo.owner,
                "repo": repo.name,
                "user_id": self.user_id,
            },
        )

        repository = result["repository"]
        if repository is None:
            raise ValueError(f"Repository not found: {repo.key}")

        default_branch = repository["defaultBranchRef"]
        num_commits = 0
        latest_commit_date = None

        if default_branch and default_branch["target"]:
            target = default_branch["target"]
            num_commits = target["userHistory"]["totalCount"]
            nodes = target["latestHistory"]["nodes"] or []
            if nodes:
                latest_commit_date = nodes[0].get("committedDate")

        return RepoStats(
            num_stars=repository["stargazerCount"],
            num_commits=num_commits,
            latest_commit_date=latest_commit_date,
        )


def load_repos_from_file(path: Path) -> list[str]:
    if not path.exists():
        raise FileNotFoundError(f"Repos file not found: {path}")

    if path.suffix.lower() == ".json":
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, list):
            raise ValueError("JSON repos file must contain a list of repo strings.")
        return [str(x) for x in data]

    with path.open("r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch GitHub repo stats.")
    parser.add_argument(
        "repos",
        nargs="*",
        help="Repos in owner/repo format, e.g. huggingface/transformers",
    )
    parser.add_argument(
        "--repos-file",
        type=Path,
        help="Path to a .txt or .json file containing repo list.",
    )
    parser.add_argument(
        "--cache-file",
        type=Path,
        default=CACHE_FILE_DEFAULT,
        help="Path to JSON cache file.",
    )
    parser.add_argument(
        "--user-id",
        required=True,
        help="GitHub user node ID.",
    )
    return parser.parse_args()


def resolve_repo_inputs(args: argparse.Namespace) -> list[RepoSpec]:
    raw_items: list[str] = []

    if args.repos_file:
        raw_items.extend(load_repos_from_file(args.repos_file))

    raw_items.extend(args.repos)

    if not raw_items:
        raise ValueError("No repos provided. Use positional args or --repos-file.")

    seen = set()
    repos: list[RepoSpec] = []
    for item in raw_items:
        repo = RepoSpec.parse(item)
        if repo.key not in seen:
            seen.add(repo.key)
            repos.append(repo)
    return repos


def main() -> None:
    args = parse_args()

    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise RuntimeError("GITHUB_TOKEN environment variable is not set.")

    repos = resolve_repo_inputs(args)
    cache = Cache(args.cache_file)
    fetcher = GitHubRepoFetcher(token=token, user_id=args.user_id)

    results: list[dict[str, Any]] = []
    for repo in repos:
        cached = cache.get_stats(repo.key)
        if cached is not None:
            results.append(cached.to_public_dict())
            continue

        stats = fetcher.fetch(repo)
        cache.set_stats(repo.key, stats)
        results.append(stats.to_public_dict())

    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
