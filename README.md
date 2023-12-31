## :wave: Hi, I am afuetterer (Heinz-Alexander Fuetterer)

![visitors](https://vbr.wocr.tk/badge?page_id=afuetterer.afuetterer&color=00cf00)

My name is Heinz-Alexander Fuetterer and I am a research data management officer at the University Library of Freie Universität Berlin. I am passionate about open source, open data and research software engineering.

### :wrench: Skills

[![Python][python-badge]][python]
[![Pytest][pytest-badge]][pytest]
[![Pandas][pandas-badge]][pandas]
[![Django][django-badge]][django]
[![Flask][flask-badge]][flask]

### :chart_with_upwards_trend: GitHub Stats

![metrics](https://metrics.lecoq.io/afuetterer?template=classic&languages=1&base=header%2C%20activity%2C%20community%2C%20repositories%2C%20metadata&base.indepth=false&base.hireable=false&base.skip=false&languages=false&languages.limit=5&languages.threshold=0%25&languages.other=false&languages.colors=github&languages.sections=most-used&languages.indepth=false&languages.analysis.timeout=15&languages.analysis.timeout.repositories=7.5&languages.categories=markup%2C%20programming&languages.recent.categories=markup%2C%20programming&languages.recent.load=300&languages.recent.days=14&config.timezone=Europe%2FBerlin)

### :handshake: Contributions

I have contributed to these projects. Follow the links to see the commits I authored for these projects.

<!-- adapted from https://github.com/cjolowicz/cjolowicz/blob/main/README.md -->
<!-- run "cog -r README.md" >
<!-- [[[cog

import requests

def get_commit_counts(repo: str, contributor: str, verbose: bool = False) -> int:
    commit_count = 0
    url = f"https://api.github.com/repos/{repo}/commits"
    params = {"author": contributor, "per_page": 100}

    with requests.Session() as session:
        while True:
            response = session.get(url, params=params)
            if response.status_code == 200:
                commits = response.json()
                for commit in commits:
                    message = commit["commit"]["message"]
                    # do not count merge commits
                    if not message.startswith("Merge pull request"):
                        if verbose:
                            print(f"{commit_count}: {message}\n")
                        commit_count += 1
                if len(commits) < 100:
                    break
                if "next" in response.links:
                    url = response.links["next"]["url"]
                else:
                    break
            else:
                print(f"Failed to fetch data: {response.status_code} - {response.text}")
                break
    return commit_count

HEADER = "| Name  | # My Commits | # Stars | Last Commit | Version | # Downloads |\n| ----  | -------: | ---------- | ----------- | ------- | ----------- |"

academic_repos = [
    "astropy/astropy",
    "rdmorganiser/rdmo",
    "rdmorganiser/rdmo-catalog",
    "rdmorganiser/rdmo-docs-en",
    "rdmorganiser/rdmo-plugins",
    "pangaea-data-publisher/fuji",
    "ddionrails/ddionrails",
    "galaxyproject/galaxy",
    "re3data/using_the_re3data_API",
    "dracor-org/dracor-api",
    "dracor-org/dracor-metrics",
    "dracor-org/dracor-notebooks",
    "merenlab/anvio",
    "psychopy/psychopy",
    "PlasmaPy/PlasmaPy",
]

oss_repos = [
    "python-semantic-release/python-semantic-release",
    "python/cpython",
    "tfranzel/drf-spectacular",
    "pennersr/django-allauth",
    "tiangolo/fastapi",
    "inveniosoftware/idutils",
    "iterative/dvc",
    "spec-first/connexion",
    "schemathesis/schemathesis",
    "huggingface/diffusers",
    "huggingface/transformers",
    "numpy/numpy",
]

not_on_pypi = {
    "pangaea-data-publisher/fuji",
    "python/cpython",
    "ddionrails/ddionrails",
    "dracor-org/dracor-api",
    "dracor-org/dracor-metrics",
    "dracor-org/dracor-notebooks",  
    "rdmorganiser/rdmo-catalog",
    "rdmorganiser/rdmo-docs-en",
    "rdmorganiser/rdmo-plugins",
    "galaxyproject/galaxy",
    "re3data/using_the_re3data_API",
    "merenlab/anvio",
}

academic_repos = sorted(academic_repos, key=lambda x: x.split("/")[1])
oss_repos = sorted(oss_repos, key=lambda x: x.split("/")[1])

def print_repo_table(repos):
    cog.outl(HEADER)
    for repo in repos:
        org, package = repo.split("/")
        github_url = f"https://github.com/{org}/{package}/commits?author=afuetterer"
        pypi_url = f"https://pypi.org/project/{package}/"
        pypi_version_url = f"https://img.shields.io/pypi/v/{package}"
        last_commit_url = f"https://img.shields.io/github/last-commit/{repo}"
        stars_url = f"https://img.shields.io/github/stars/{repo}"
        downloads_url = f"https://img.shields.io/pypi/dm/{package}"

        github = f"[{package}]({github_url})"
        pypi =f"[![PyPI version]({pypi_version_url})]({pypi_url})"
        last_commit = f"![GitHub last commit]({last_commit_url})"
        stars = f"![GitHub stars]({stars_url})"
        downloads = f"![Downloads]({downloads_url})"
        
        my_commits = get_commit_counts(repo, "afuetterer")

        if repo in not_on_pypi:
            entry = f"| {github} | {my_commits} | {stars} | {last_commit} | | |"
        else:
            entry = f"| {github} | {my_commits} | {stars} | {last_commit} | {pypi} | {downloads} |"
        cog.outl(entry)
cog.outl("#### Academia")
print_repo_table(academic_repos)
cog.outl("#### Open Source")
print_repo_table(oss_repos)

]]] -->
#### Academia
| Name  | # My Commits | # Stars | Last Commit | Version | # Downloads |
| ----  | -------: | ---------- | ----------- | ------- | ----------- |
| [PlasmaPy](https://github.com/PlasmaPy/PlasmaPy/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/PlasmaPy/PlasmaPy) | ![GitHub last commit](https://img.shields.io/github/last-commit/PlasmaPy/PlasmaPy) | [![PyPI version](https://img.shields.io/pypi/v/PlasmaPy)](https://pypi.org/project/PlasmaPy/) | ![Downloads](https://img.shields.io/pypi/dm/PlasmaPy) |
| [anvio](https://github.com/merenlab/anvio/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/merenlab/anvio) | ![GitHub last commit](https://img.shields.io/github/last-commit/merenlab/anvio) | | |
| [astropy](https://github.com/astropy/astropy/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/astropy/astropy) | ![GitHub last commit](https://img.shields.io/github/last-commit/astropy/astropy) | [![PyPI version](https://img.shields.io/pypi/v/astropy)](https://pypi.org/project/astropy/) | ![Downloads](https://img.shields.io/pypi/dm/astropy) |
| [ddionrails](https://github.com/ddionrails/ddionrails/commits?author=afuetterer) | 486 | ![GitHub stars](https://img.shields.io/github/stars/ddionrails/ddionrails) | ![GitHub last commit](https://img.shields.io/github/last-commit/ddionrails/ddionrails) | | |
| [dracor-api](https://github.com/dracor-org/dracor-api/commits?author=afuetterer) | 5 | ![GitHub stars](https://img.shields.io/github/stars/dracor-org/dracor-api) | ![GitHub last commit](https://img.shields.io/github/last-commit/dracor-org/dracor-api) | | |
| [dracor-metrics](https://github.com/dracor-org/dracor-metrics/commits?author=afuetterer) | 7 | ![GitHub stars](https://img.shields.io/github/stars/dracor-org/dracor-metrics) | ![GitHub last commit](https://img.shields.io/github/last-commit/dracor-org/dracor-metrics) | | |
| [dracor-notebooks](https://github.com/dracor-org/dracor-notebooks/commits?author=afuetterer) | 2 | ![GitHub stars](https://img.shields.io/github/stars/dracor-org/dracor-notebooks) | ![GitHub last commit](https://img.shields.io/github/last-commit/dracor-org/dracor-notebooks) | | |
| [fuji](https://github.com/pangaea-data-publisher/fuji/commits?author=afuetterer) | 61 | ![GitHub stars](https://img.shields.io/github/stars/pangaea-data-publisher/fuji) | ![GitHub last commit](https://img.shields.io/github/last-commit/pangaea-data-publisher/fuji) | | |
| [galaxy](https://github.com/galaxyproject/galaxy/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/galaxyproject/galaxy) | ![GitHub last commit](https://img.shields.io/github/last-commit/galaxyproject/galaxy) | | |
| [psychopy](https://github.com/psychopy/psychopy/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/psychopy/psychopy) | ![GitHub last commit](https://img.shields.io/github/last-commit/psychopy/psychopy) | [![PyPI version](https://img.shields.io/pypi/v/psychopy)](https://pypi.org/project/psychopy/) | ![Downloads](https://img.shields.io/pypi/dm/psychopy) |
| [rdmo](https://github.com/rdmorganiser/rdmo/commits?author=afuetterer) | 106 | ![GitHub stars](https://img.shields.io/github/stars/rdmorganiser/rdmo) | ![GitHub last commit](https://img.shields.io/github/last-commit/rdmorganiser/rdmo) | [![PyPI version](https://img.shields.io/pypi/v/rdmo)](https://pypi.org/project/rdmo/) | ![Downloads](https://img.shields.io/pypi/dm/rdmo) |
| [rdmo-catalog](https://github.com/rdmorganiser/rdmo-catalog/commits?author=afuetterer) | 2 | ![GitHub stars](https://img.shields.io/github/stars/rdmorganiser/rdmo-catalog) | ![GitHub last commit](https://img.shields.io/github/last-commit/rdmorganiser/rdmo-catalog) | | |
| [rdmo-docs-en](https://github.com/rdmorganiser/rdmo-docs-en/commits?author=afuetterer) | 9 | ![GitHub stars](https://img.shields.io/github/stars/rdmorganiser/rdmo-docs-en) | ![GitHub last commit](https://img.shields.io/github/last-commit/rdmorganiser/rdmo-docs-en) | | |
| [rdmo-plugins](https://github.com/rdmorganiser/rdmo-plugins/commits?author=afuetterer) | 5 | ![GitHub stars](https://img.shields.io/github/stars/rdmorganiser/rdmo-plugins) | ![GitHub last commit](https://img.shields.io/github/last-commit/rdmorganiser/rdmo-plugins) | | |
| [using_the_re3data_API](https://github.com/re3data/using_the_re3data_API/commits?author=afuetterer) | 7 | ![GitHub stars](https://img.shields.io/github/stars/re3data/using_the_re3data_API) | ![GitHub last commit](https://img.shields.io/github/last-commit/re3data/using_the_re3data_API) | | |
#### Open Source
| Name  | # My Commits | # Stars | Last Commit | Version | # Downloads |
| ----  | -------: | ---------- | ----------- | ------- | ----------- |
| [connexion](https://github.com/spec-first/connexion/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/spec-first/connexion) | ![GitHub last commit](https://img.shields.io/github/last-commit/spec-first/connexion) | [![PyPI version](https://img.shields.io/pypi/v/connexion)](https://pypi.org/project/connexion/) | ![Downloads](https://img.shields.io/pypi/dm/connexion) |
| [cpython](https://github.com/python/cpython/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/python/cpython) | ![GitHub last commit](https://img.shields.io/github/last-commit/python/cpython) | | |
| [diffusers](https://github.com/huggingface/diffusers/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/huggingface/diffusers) | ![GitHub last commit](https://img.shields.io/github/last-commit/huggingface/diffusers) | [![PyPI version](https://img.shields.io/pypi/v/diffusers)](https://pypi.org/project/diffusers/) | ![Downloads](https://img.shields.io/pypi/dm/diffusers) |
| [django-allauth](https://github.com/pennersr/django-allauth/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/pennersr/django-allauth) | ![GitHub last commit](https://img.shields.io/github/last-commit/pennersr/django-allauth) | [![PyPI version](https://img.shields.io/pypi/v/django-allauth)](https://pypi.org/project/django-allauth/) | ![Downloads](https://img.shields.io/pypi/dm/django-allauth) |
| [drf-spectacular](https://github.com/tfranzel/drf-spectacular/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/tfranzel/drf-spectacular) | ![GitHub last commit](https://img.shields.io/github/last-commit/tfranzel/drf-spectacular) | [![PyPI version](https://img.shields.io/pypi/v/drf-spectacular)](https://pypi.org/project/drf-spectacular/) | ![Downloads](https://img.shields.io/pypi/dm/drf-spectacular) |
| [dvc](https://github.com/iterative/dvc/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/iterative/dvc) | ![GitHub last commit](https://img.shields.io/github/last-commit/iterative/dvc) | [![PyPI version](https://img.shields.io/pypi/v/dvc)](https://pypi.org/project/dvc/) | ![Downloads](https://img.shields.io/pypi/dm/dvc) |
| [fastapi](https://github.com/tiangolo/fastapi/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/tiangolo/fastapi) | ![GitHub last commit](https://img.shields.io/github/last-commit/tiangolo/fastapi) | [![PyPI version](https://img.shields.io/pypi/v/fastapi)](https://pypi.org/project/fastapi/) | ![Downloads](https://img.shields.io/pypi/dm/fastapi) |
| [idutils](https://github.com/inveniosoftware/idutils/commits?author=afuetterer) | 3 | ![GitHub stars](https://img.shields.io/github/stars/inveniosoftware/idutils) | ![GitHub last commit](https://img.shields.io/github/last-commit/inveniosoftware/idutils) | [![PyPI version](https://img.shields.io/pypi/v/idutils)](https://pypi.org/project/idutils/) | ![Downloads](https://img.shields.io/pypi/dm/idutils) |
| [numpy](https://github.com/numpy/numpy/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/numpy/numpy) | ![GitHub last commit](https://img.shields.io/github/last-commit/numpy/numpy) | [![PyPI version](https://img.shields.io/pypi/v/numpy)](https://pypi.org/project/numpy/) | ![Downloads](https://img.shields.io/pypi/dm/numpy) |
| [python-semantic-release](https://github.com/python-semantic-release/python-semantic-release/commits?author=afuetterer) | 6 | ![GitHub stars](https://img.shields.io/github/stars/python-semantic-release/python-semantic-release) | ![GitHub last commit](https://img.shields.io/github/last-commit/python-semantic-release/python-semantic-release) | [![PyPI version](https://img.shields.io/pypi/v/python-semantic-release)](https://pypi.org/project/python-semantic-release/) | ![Downloads](https://img.shields.io/pypi/dm/python-semantic-release) |
| [schemathesis](https://github.com/schemathesis/schemathesis/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/schemathesis/schemathesis) | ![GitHub last commit](https://img.shields.io/github/last-commit/schemathesis/schemathesis) | [![PyPI version](https://img.shields.io/pypi/v/schemathesis)](https://pypi.org/project/schemathesis/) | ![Downloads](https://img.shields.io/pypi/dm/schemathesis) |
| [transformers](https://github.com/huggingface/transformers/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/huggingface/transformers) | ![GitHub last commit](https://img.shields.io/github/last-commit/huggingface/transformers) | [![PyPI version](https://img.shields.io/pypi/v/transformers)](https://pypi.org/project/transformers/) | ![Downloads](https://img.shields.io/pypi/dm/transformers) |
<!-- [[[end]]] -->

### :handshake: Hacktoberfest 2023
[![An image of @afuetterer's Holopin badges, which is a link to view their full Holopin profile](https://holopin.me/afuetterer)](https://holopin.io/@afuetterer)

<!-- Markdown links -->

[python]: https://www.python.org
[python-badge]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=white
[pytest]: https://docs.pytest.org
[pytest-badge]: https://img.shields.io/badge/Pytest-0A9EDC.svg?style=for-the-badge&logo=Pytest&logoColor=white
[pandas]: https://pandas.pydata.org
[pandas-badge]: https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white
[django]: https://www.djangoproject.com
[django-badge]: https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white
[flask]: https://flask.palletsprojects.com
[flask-badge]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white

<!-- 
metrics: https://github.com/lowlighter/metrics
-->
