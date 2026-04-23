import json
from datetime import UTC, datetime, timezone

import humanize


def format_latest_commit(commit_timestamp: str | None) -> str:
    """Format commit timestamp string into human-readable time ago.

    Args:
        commit_timestamp: ISO format datetime string, e.g. '2024-01-15T10:30:00Z'

    Returns:
        Human-readable string like '2 days ago' or '-' if input is None/empty
    """
    if not commit_timestamp:
        return "-"

    try:
        dt = datetime.fromisoformat(commit_timestamp.replace("Z", "+00:00"))
        time_ago = datetime.now(timezone.utc) - dt
        return humanize.naturaltime(time_ago)
    except ValueError:
        return "-"


def render_table(cog, cache_file: str = "cache.json") -> None:
    """Render cached repository statistics as a markdown table.

    Args:
        cog: Content generator from cogapp
        cache_file: Path to JSON cache file containing repo statistics
    """
    with open(cache_file, encoding="utf-8") as f:
        rows = json.load(f).items()

    cog.outl("\n| Name | # My Commits | # Stars | Latest commit |")
    cog.outl("|---|---:|---:|---|")
    for repo, stats in rows:
        latest = format_latest_commit(stats.get("latest_commit_date"))
        my_commits_url = f"https://github.com/{repo}/commits?author=afuetterer"
        num_stars = humanize.intword(stats["num_stars"])
        cog.outl(f"| [{repo}]({my_commits_url}) | {stats['num_commits']} | {num_stars} | {latest} |")
