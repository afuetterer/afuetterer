import json
from datetime import UTC, datetime, timezone

import humanize


def format_latest_commit(dt_str):
    if not dt_str:
        return "-"
    dt = datetime.fromisoformat(dt_str.replace("Z", "+00:00"))
    return humanize.naturaltime(datetime.now(UTC) - dt)


def render_table(cog, cache_file="cache.json"):
    with open(cache_file, encoding="utf-8") as f:
        rows = json.load(f).items()

    cog.outl("\n| Name | # My Commits | # Stars | Latest commit |")
    cog.outl("|---|---:|---:|---|")
    for repo, stats in rows:
        latest = format_latest_commit(stats.get("latest_commit_date"))
        my_commits_url = f"https://github.com/{repo}/commits?author=afuetterer"
        num_stars = humanize.intword(stats["num_stars"])
        cog.outl(f"| [{repo}]({my_commits_url}) | {stats['num_commits']} | {num_stars} | {latest} |")
