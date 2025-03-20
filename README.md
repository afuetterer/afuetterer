## :wave: Hi, I am afuetterer (Heinz-Alexander Fütterer)

![visitors](https://komarev.com/ghpvc/?username=afuetterer)

I am a research software engineer at WZB Berlin Social Science Center. I am passionate about open source, open data and research software engineering.

### :wrench: Skills

[![Python][python-badge]][python]
[![Pytest][pytest-badge]][pytest]
[![Pandas][pandas-badge]][pandas]
[![Django][django-badge]][django]
[![Flask][flask-badge]][flask]

### :chart_with_upwards_trend: GitHub Statistics

![statistics](/images/statistics.svg)

### :ok_hand: My Projects

I maintain these open source projects:

| Name  | # Stars | Last Commit | Version | # Downloads |
| ----  | ------: | ----------- | ------- | ----------- |
| [oaipmh-scythe](https://github.com/afuetterer/oaipmh-scythe) | ![GitHub stars](https://img.shields.io/github/stars/afuetterer/oaipmh-scythe) | ![GitHub last commit](https://img.shields.io/github/last-commit/afuetterer/oaipmh-scythe) | [![PyPI version](https://img.shields.io/pypi/v/oaipmh-scythe)](https://pypi.org/project/oaipmh-scythe/) | ![Downloads](https://img.shields.io/pypi/dm/oaipmh-scythe) |
| [python-re3data](https://github.com/afuetterer/python-re3data) | ![GitHub stars](https://img.shields.io/github/stars/afuetterer/python-re3data) | ![GitHub last commit](https://img.shields.io/github/last-commit/afuetterer/python-re3data) | [![PyPI version](https://img.shields.io/pypi/v/python-re3data)](https://pypi.org/project/python-re3data/) | ![Downloads](https://img.shields.io/pypi/dm/python-re3data) |

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
            print(repo, response)
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
    "dracor-org/pydracor",
    "merenlab/anvio",
    "psychopy/psychopy",
    "plasmapy/plasmapy",
    "pymeasure/pymeasure",
    "pypsa/powerplantmatching",
    "pypsa/pypsa",
    "pypsa/linopy",
    "the-turing-way/the-turing-way",
    "sissaschool/xmlschema",
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
    "frictionlessdata/frictionless-py",
    "tefra/xsdata",
    "vitalik/django-ninja",
    "provinzkraut/unasyncd",
    "maartengr/bertopic",
    "maartengr/keybert",
    "scrapy/scrapyd",
    "scrapy/scrapyd-client",
]

not_on_pypi = {
    "pangaea-data-publisher/fuji",
    "python/cpython",
    "ddionrails/ddionrails",
    "dracor-org/dracor-api",
    "dracor-org/dracor-frontend",
    "dracor-org/dracor-fuseki",
    "dracor-org/dracor-metrics",
    "dracor-org/dracor-notebooks",
    "rdmorganiser/rdmo-catalog",
    "rdmorganiser/rdmo-docs-en",
    "rdmorganiser/rdmo-plugins",
    "galaxyproject/galaxy",
    "re3data/using_the_re3data_API",
    "merenlab/anvio",
    "gtonkinhill/panaroo",
    "nickjcroucher/gubbins",
    "the-turing-way/the-turing-way",
}

academic_repos = sorted(academic_repos, key=lambda x: x.split("/")[1])
oss_repos = sorted(oss_repos, key=lambda x: x.split("/")[1])

def print_repo_table(repos):
    cog.outl(HEADER)
    for repo in repos:
        org, package = repo.split("/")
        github_url = f"https://github.com/{org}/{package}/commits?author=afuetterer"
        github = f"[{package}]({github_url})"

        if package == "frictionless-py":
            package = "frictionless"

        pypi_url = f"https://pypi.org/project/{package}/"
        pypi_version_url = f"https://img.shields.io/pypi/v/{package}"
        last_commit_url = f"https://img.shields.io/github/last-commit/{repo}"
        stars_url = f"https://img.shields.io/github/stars/{repo}"
        downloads_url = f"https://img.shields.io/pypi/dm/{package}"
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
| [anvio](https://github.com/merenlab/anvio/commits?author=afuetterer) | 2 | ![GitHub stars](https://img.shields.io/github/stars/merenlab/anvio) | ![GitHub last commit](https://img.shields.io/github/last-commit/merenlab/anvio) | | |
| [astropy](https://github.com/astropy/astropy/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/astropy/astropy) | ![GitHub last commit](https://img.shields.io/github/last-commit/astropy/astropy) | [![PyPI version](https://img.shields.io/pypi/v/astropy)](https://pypi.org/project/astropy/) | ![Downloads](https://img.shields.io/pypi/dm/astropy) |
| [ddionrails](https://github.com/ddionrails/ddionrails/commits?author=afuetterer) | 486 | ![GitHub stars](https://img.shields.io/github/stars/ddionrails/ddionrails) | ![GitHub last commit](https://img.shields.io/github/last-commit/ddionrails/ddionrails) | | |
| [dracor-api](https://github.com/dracor-org/dracor-api/commits?author=afuetterer) | 7 | ![GitHub stars](https://img.shields.io/github/stars/dracor-org/dracor-api) | ![GitHub last commit](https://img.shields.io/github/last-commit/dracor-org/dracor-api) | | |
| [dracor-metrics](https://github.com/dracor-org/dracor-metrics/commits?author=afuetterer) | 13 | ![GitHub stars](https://img.shields.io/github/stars/dracor-org/dracor-metrics) | ![GitHub last commit](https://img.shields.io/github/last-commit/dracor-org/dracor-metrics) | | |
| [dracor-notebooks](https://github.com/dracor-org/dracor-notebooks/commits?author=afuetterer) | 2 | ![GitHub stars](https://img.shields.io/github/stars/dracor-org/dracor-notebooks) | ![GitHub last commit](https://img.shields.io/github/last-commit/dracor-org/dracor-notebooks) | | |
| [fuji](https://github.com/pangaea-data-publisher/fuji/commits?author=afuetterer) | 88 | ![GitHub stars](https://img.shields.io/github/stars/pangaea-data-publisher/fuji) | ![GitHub last commit](https://img.shields.io/github/last-commit/pangaea-data-publisher/fuji) | | |
| [galaxy](https://github.com/galaxyproject/galaxy/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/galaxyproject/galaxy) | ![GitHub last commit](https://img.shields.io/github/last-commit/galaxyproject/galaxy) | | |
| [linopy](https://github.com/pypsa/linopy/commits?author=afuetterer) | 25 | ![GitHub stars](https://img.shields.io/github/stars/pypsa/linopy) | ![GitHub last commit](https://img.shields.io/github/last-commit/pypsa/linopy) | [![PyPI version](https://img.shields.io/pypi/v/linopy)](https://pypi.org/project/linopy/) | ![Downloads](https://img.shields.io/pypi/dm/linopy) |
| [plasmapy](https://github.com/plasmapy/plasmapy/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/plasmapy/plasmapy) | ![GitHub last commit](https://img.shields.io/github/last-commit/plasmapy/plasmapy) | [![PyPI version](https://img.shields.io/pypi/v/plasmapy)](https://pypi.org/project/plasmapy/) | ![Downloads](https://img.shields.io/pypi/dm/plasmapy) |
| [powerplantmatching](https://github.com/pypsa/powerplantmatching/commits?author=afuetterer) | 3 | ![GitHub stars](https://img.shields.io/github/stars/pypsa/powerplantmatching) | ![GitHub last commit](https://img.shields.io/github/last-commit/pypsa/powerplantmatching) | [![PyPI version](https://img.shields.io/pypi/v/powerplantmatching)](https://pypi.org/project/powerplantmatching/) | ![Downloads](https://img.shields.io/pypi/dm/powerplantmatching) |
| [psychopy](https://github.com/psychopy/psychopy/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/psychopy/psychopy) | ![GitHub last commit](https://img.shields.io/github/last-commit/psychopy/psychopy) | [![PyPI version](https://img.shields.io/pypi/v/psychopy)](https://pypi.org/project/psychopy/) | ![Downloads](https://img.shields.io/pypi/dm/psychopy) |
| [pydracor](https://github.com/dracor-org/pydracor/commits?author=afuetterer) | 3 | ![GitHub stars](https://img.shields.io/github/stars/dracor-org/pydracor) | ![GitHub last commit](https://img.shields.io/github/last-commit/dracor-org/pydracor) | [![PyPI version](https://img.shields.io/pypi/v/pydracor)](https://pypi.org/project/pydracor/) | ![Downloads](https://img.shields.io/pypi/dm/pydracor) |
| [pymeasure](https://github.com/pymeasure/pymeasure/commits?author=afuetterer) | 2 | ![GitHub stars](https://img.shields.io/github/stars/pymeasure/pymeasure) | ![GitHub last commit](https://img.shields.io/github/last-commit/pymeasure/pymeasure) | [![PyPI version](https://img.shields.io/pypi/v/pymeasure)](https://pypi.org/project/pymeasure/) | ![Downloads](https://img.shields.io/pypi/dm/pymeasure) |
| [pypsa](https://github.com/pypsa/pypsa/commits?author=afuetterer) | 7 | ![GitHub stars](https://img.shields.io/github/stars/pypsa/pypsa) | ![GitHub last commit](https://img.shields.io/github/last-commit/pypsa/pypsa) | [![PyPI version](https://img.shields.io/pypi/v/pypsa)](https://pypi.org/project/pypsa/) | ![Downloads](https://img.shields.io/pypi/dm/pypsa) |
| [rdmo](https://github.com/rdmorganiser/rdmo/commits?author=afuetterer) | 134 | ![GitHub stars](https://img.shields.io/github/stars/rdmorganiser/rdmo) | ![GitHub last commit](https://img.shields.io/github/last-commit/rdmorganiser/rdmo) | [![PyPI version](https://img.shields.io/pypi/v/rdmo)](https://pypi.org/project/rdmo/) | ![Downloads](https://img.shields.io/pypi/dm/rdmo) |
| [rdmo-catalog](https://github.com/rdmorganiser/rdmo-catalog/commits?author=afuetterer) | 2 | ![GitHub stars](https://img.shields.io/github/stars/rdmorganiser/rdmo-catalog) | ![GitHub last commit](https://img.shields.io/github/last-commit/rdmorganiser/rdmo-catalog) | | |
| [rdmo-docs-en](https://github.com/rdmorganiser/rdmo-docs-en/commits?author=afuetterer) | 10 | ![GitHub stars](https://img.shields.io/github/stars/rdmorganiser/rdmo-docs-en) | ![GitHub last commit](https://img.shields.io/github/last-commit/rdmorganiser/rdmo-docs-en) | | |
| [rdmo-plugins](https://github.com/rdmorganiser/rdmo-plugins/commits?author=afuetterer) | 5 | ![GitHub stars](https://img.shields.io/github/stars/rdmorganiser/rdmo-plugins) | ![GitHub last commit](https://img.shields.io/github/last-commit/rdmorganiser/rdmo-plugins) | | |
| [the-turing-way](https://github.com/the-turing-way/the-turing-way/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/the-turing-way/the-turing-way) | ![GitHub last commit](https://img.shields.io/github/last-commit/the-turing-way/the-turing-way) | | |
| [using_the_re3data_API](https://github.com/re3data/using_the_re3data_API/commits?author=afuetterer) | 7 | ![GitHub stars](https://img.shields.io/github/stars/re3data/using_the_re3data_API) | ![GitHub last commit](https://img.shields.io/github/last-commit/re3data/using_the_re3data_API) | | |
| [xmlschema](https://github.com/sissaschool/xmlschema/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/sissaschool/xmlschema) | ![GitHub last commit](https://img.shields.io/github/last-commit/sissaschool/xmlschema) | [![PyPI version](https://img.shields.io/pypi/v/xmlschema)](https://pypi.org/project/xmlschema/) | ![Downloads](https://img.shields.io/pypi/dm/xmlschema) |
#### Open Source
| Name  | # My Commits | # Stars | Last Commit | Version | # Downloads |
| ----  | -------: | ---------- | ----------- | ------- | ----------- |
| [bertopic](https://github.com/maartengr/bertopic/commits?author=afuetterer) | 10 | ![GitHub stars](https://img.shields.io/github/stars/maartengr/bertopic) | ![GitHub last commit](https://img.shields.io/github/last-commit/maartengr/bertopic) | [![PyPI version](https://img.shields.io/pypi/v/bertopic)](https://pypi.org/project/bertopic/) | ![Downloads](https://img.shields.io/pypi/dm/bertopic) |
| [connexion](https://github.com/spec-first/connexion/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/spec-first/connexion) | ![GitHub last commit](https://img.shields.io/github/last-commit/spec-first/connexion) | [![PyPI version](https://img.shields.io/pypi/v/connexion)](https://pypi.org/project/connexion/) | ![Downloads](https://img.shields.io/pypi/dm/connexion) |
| [cpython](https://github.com/python/cpython/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/python/cpython) | ![GitHub last commit](https://img.shields.io/github/last-commit/python/cpython) | | |
| [diffusers](https://github.com/huggingface/diffusers/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/huggingface/diffusers) | ![GitHub last commit](https://img.shields.io/github/last-commit/huggingface/diffusers) | [![PyPI version](https://img.shields.io/pypi/v/diffusers)](https://pypi.org/project/diffusers/) | ![Downloads](https://img.shields.io/pypi/dm/diffusers) |
| [django-allauth](https://github.com/pennersr/django-allauth/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/pennersr/django-allauth) | ![GitHub last commit](https://img.shields.io/github/last-commit/pennersr/django-allauth) | [![PyPI version](https://img.shields.io/pypi/v/django-allauth)](https://pypi.org/project/django-allauth/) | ![Downloads](https://img.shields.io/pypi/dm/django-allauth) |
| [django-ninja](https://github.com/vitalik/django-ninja/commits?author=afuetterer) | 2 | ![GitHub stars](https://img.shields.io/github/stars/vitalik/django-ninja) | ![GitHub last commit](https://img.shields.io/github/last-commit/vitalik/django-ninja) | [![PyPI version](https://img.shields.io/pypi/v/django-ninja)](https://pypi.org/project/django-ninja/) | ![Downloads](https://img.shields.io/pypi/dm/django-ninja) |
| [drf-spectacular](https://github.com/tfranzel/drf-spectacular/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/tfranzel/drf-spectacular) | ![GitHub last commit](https://img.shields.io/github/last-commit/tfranzel/drf-spectacular) | [![PyPI version](https://img.shields.io/pypi/v/drf-spectacular)](https://pypi.org/project/drf-spectacular/) | ![Downloads](https://img.shields.io/pypi/dm/drf-spectacular) |
| [dvc](https://github.com/iterative/dvc/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/iterative/dvc) | ![GitHub last commit](https://img.shields.io/github/last-commit/iterative/dvc) | [![PyPI version](https://img.shields.io/pypi/v/dvc)](https://pypi.org/project/dvc/) | ![Downloads](https://img.shields.io/pypi/dm/dvc) |
| [fastapi](https://github.com/tiangolo/fastapi/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/tiangolo/fastapi) | ![GitHub last commit](https://img.shields.io/github/last-commit/tiangolo/fastapi) | [![PyPI version](https://img.shields.io/pypi/v/fastapi)](https://pypi.org/project/fastapi/) | ![Downloads](https://img.shields.io/pypi/dm/fastapi) |
| [frictionless-py](https://github.com/frictionlessdata/frictionless-py/commits?author=afuetterer) | 2 | ![GitHub stars](https://img.shields.io/github/stars/frictionlessdata/frictionless-py) | ![GitHub last commit](https://img.shields.io/github/last-commit/frictionlessdata/frictionless-py) | [![PyPI version](https://img.shields.io/pypi/v/frictionless)](https://pypi.org/project/frictionless/) | ![Downloads](https://img.shields.io/pypi/dm/frictionless) |
| [idutils](https://github.com/inveniosoftware/idutils/commits?author=afuetterer) | 3 | ![GitHub stars](https://img.shields.io/github/stars/inveniosoftware/idutils) | ![GitHub last commit](https://img.shields.io/github/last-commit/inveniosoftware/idutils) | [![PyPI version](https://img.shields.io/pypi/v/idutils)](https://pypi.org/project/idutils/) | ![Downloads](https://img.shields.io/pypi/dm/idutils) |
| [keybert](https://github.com/maartengr/keybert/commits?author=afuetterer) | 8 | ![GitHub stars](https://img.shields.io/github/stars/maartengr/keybert) | ![GitHub last commit](https://img.shields.io/github/last-commit/maartengr/keybert) | [![PyPI version](https://img.shields.io/pypi/v/keybert)](https://pypi.org/project/keybert/) | ![Downloads](https://img.shields.io/pypi/dm/keybert) |
| [numpy](https://github.com/numpy/numpy/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/numpy/numpy) | ![GitHub last commit](https://img.shields.io/github/last-commit/numpy/numpy) | [![PyPI version](https://img.shields.io/pypi/v/numpy)](https://pypi.org/project/numpy/) | ![Downloads](https://img.shields.io/pypi/dm/numpy) |
| [python-semantic-release](https://github.com/python-semantic-release/python-semantic-release/commits?author=afuetterer) | 10 | ![GitHub stars](https://img.shields.io/github/stars/python-semantic-release/python-semantic-release) | ![GitHub last commit](https://img.shields.io/github/last-commit/python-semantic-release/python-semantic-release) | [![PyPI version](https://img.shields.io/pypi/v/python-semantic-release)](https://pypi.org/project/python-semantic-release/) | ![Downloads](https://img.shields.io/pypi/dm/python-semantic-release) |
| [schemathesis](https://github.com/schemathesis/schemathesis/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/schemathesis/schemathesis) | ![GitHub last commit](https://img.shields.io/github/last-commit/schemathesis/schemathesis) | [![PyPI version](https://img.shields.io/pypi/v/schemathesis)](https://pypi.org/project/schemathesis/) | ![Downloads](https://img.shields.io/pypi/dm/schemathesis) |
| [scrapyd](https://github.com/scrapy/scrapyd/commits?author=afuetterer) | 3 | ![GitHub stars](https://img.shields.io/github/stars/scrapy/scrapyd) | ![GitHub last commit](https://img.shields.io/github/last-commit/scrapy/scrapyd) | [![PyPI version](https://img.shields.io/pypi/v/scrapyd)](https://pypi.org/project/scrapyd/) | ![Downloads](https://img.shields.io/pypi/dm/scrapyd) |
| [scrapyd-client](https://github.com/scrapy/scrapyd-client/commits?author=afuetterer) | 2 | ![GitHub stars](https://img.shields.io/github/stars/scrapy/scrapyd-client) | ![GitHub last commit](https://img.shields.io/github/last-commit/scrapy/scrapyd-client) | [![PyPI version](https://img.shields.io/pypi/v/scrapyd-client)](https://pypi.org/project/scrapyd-client/) | ![Downloads](https://img.shields.io/pypi/dm/scrapyd-client) |
| [transformers](https://github.com/huggingface/transformers/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/huggingface/transformers) | ![GitHub last commit](https://img.shields.io/github/last-commit/huggingface/transformers) | [![PyPI version](https://img.shields.io/pypi/v/transformers)](https://pypi.org/project/transformers/) | ![Downloads](https://img.shields.io/pypi/dm/transformers) |
| [unasyncd](https://github.com/provinzkraut/unasyncd/commits?author=afuetterer) | 7 | ![GitHub stars](https://img.shields.io/github/stars/provinzkraut/unasyncd) | ![GitHub last commit](https://img.shields.io/github/last-commit/provinzkraut/unasyncd) | [![PyPI version](https://img.shields.io/pypi/v/unasyncd)](https://pypi.org/project/unasyncd/) | ![Downloads](https://img.shields.io/pypi/dm/unasyncd) |
| [xsdata](https://github.com/tefra/xsdata/commits?author=afuetterer) | 4 | ![GitHub stars](https://img.shields.io/github/stars/tefra/xsdata) | ![GitHub last commit](https://img.shields.io/github/last-commit/tefra/xsdata) | [![PyPI version](https://img.shields.io/pypi/v/xsdata)](https://pypi.org/project/xsdata/) | ![Downloads](https://img.shields.io/pypi/dm/xsdata) |
<!-- [[[end]]] -->

<details>
<summary>:handshake: Holopin Badges</summary>

### :handshake: Holopin Badges
[![An image of @afuetterer's Holopin badges, which is a link to view their full Holopin profile](https://holopin.me/afuetterer)](https://holopin.io/@afuetterer)
</details>

<!-- Refs -->

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
