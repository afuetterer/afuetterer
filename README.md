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

HEADER = "| Name  | # My Commits | # Stars | Last Commit | \n| ----  | -------: | ---------- | ----------- | "

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
    "chrismattmann/tika-python",
]

# spec-first/connexion
# tiangolo/fastapi
# iterative/dvc

oss_repos = [
    "python-semantic-release/python-semantic-release",
    "python/cpython",
    "tfranzel/drf-spectacular",
    "pennersr/django-allauth",
    "inveniosoftware/idutils",
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
    "huggingface/datasets",
    "spack/spack",
    "spack/spack-packages",
    "ibm/prompt-declaration-language",
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
    "spack/spack",
    "spack/spack-packages",
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

        last_commit_url = f"https://img.shields.io/github/last-commit/{repo}"
        stars_url = f"https://img.shields.io/github/stars/{repo}"
        last_commit = f"![GitHub last commit]({last_commit_url})"
        stars = f"![GitHub stars]({stars_url})"

        my_commits = get_commit_counts(repo, "afuetterer")

        if repo in not_on_pypi:
            entry = f"| {github} | {my_commits} | {stars} | {last_commit} |"
        else:
            entry = f"| {github} | {my_commits} | {stars} | {last_commit} |"
        cog.outl(entry)
cog.outl("#### Academia")
print_repo_table(academic_repos)
cog.outl("#### Open Source")
print_repo_table(oss_repos)

]]] -->
#### Academia
| Name  | # My Commits | # Stars | Last Commit | 
| ----  | -------: | ---------- | ----------- | 
| [anvio](https://github.com/merenlab/anvio/commits?author=afuetterer) | 2 | ![GitHub stars](https://img.shields.io/github/stars/merenlab/anvio) | ![GitHub last commit](https://img.shields.io/github/last-commit/merenlab/anvio) |
| [astropy](https://github.com/astropy/astropy/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/astropy/astropy) | ![GitHub last commit](https://img.shields.io/github/last-commit/astropy/astropy) |
| [ddionrails](https://github.com/ddionrails/ddionrails/commits?author=afuetterer) | 486 | ![GitHub stars](https://img.shields.io/github/stars/ddionrails/ddionrails) | ![GitHub last commit](https://img.shields.io/github/last-commit/ddionrails/ddionrails) |
| [dracor-api](https://github.com/dracor-org/dracor-api/commits?author=afuetterer) | 7 | ![GitHub stars](https://img.shields.io/github/stars/dracor-org/dracor-api) | ![GitHub last commit](https://img.shields.io/github/last-commit/dracor-org/dracor-api) |
| [dracor-metrics](https://github.com/dracor-org/dracor-metrics/commits?author=afuetterer) | 13 | ![GitHub stars](https://img.shields.io/github/stars/dracor-org/dracor-metrics) | ![GitHub last commit](https://img.shields.io/github/last-commit/dracor-org/dracor-metrics) |
| [dracor-notebooks](https://github.com/dracor-org/dracor-notebooks/commits?author=afuetterer) | 2 | ![GitHub stars](https://img.shields.io/github/stars/dracor-org/dracor-notebooks) | ![GitHub last commit](https://img.shields.io/github/last-commit/dracor-org/dracor-notebooks) |
| [fuji](https://github.com/pangaea-data-publisher/fuji/commits?author=afuetterer) | 97 | ![GitHub stars](https://img.shields.io/github/stars/pangaea-data-publisher/fuji) | ![GitHub last commit](https://img.shields.io/github/last-commit/pangaea-data-publisher/fuji) |
| [galaxy](https://github.com/galaxyproject/galaxy/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/galaxyproject/galaxy) | ![GitHub last commit](https://img.shields.io/github/last-commit/galaxyproject/galaxy) |
| [linopy](https://github.com/pypsa/linopy/commits?author=afuetterer) | 25 | ![GitHub stars](https://img.shields.io/github/stars/pypsa/linopy) | ![GitHub last commit](https://img.shields.io/github/last-commit/pypsa/linopy) |
| [plasmapy](https://github.com/plasmapy/plasmapy/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/plasmapy/plasmapy) | ![GitHub last commit](https://img.shields.io/github/last-commit/plasmapy/plasmapy) |
| [powerplantmatching](https://github.com/pypsa/powerplantmatching/commits?author=afuetterer) | 3 | ![GitHub stars](https://img.shields.io/github/stars/pypsa/powerplantmatching) | ![GitHub last commit](https://img.shields.io/github/last-commit/pypsa/powerplantmatching) |
| [psychopy](https://github.com/psychopy/psychopy/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/psychopy/psychopy) | ![GitHub last commit](https://img.shields.io/github/last-commit/psychopy/psychopy) |
| [pydracor](https://github.com/dracor-org/pydracor/commits?author=afuetterer) | 3 | ![GitHub stars](https://img.shields.io/github/stars/dracor-org/pydracor) | ![GitHub last commit](https://img.shields.io/github/last-commit/dracor-org/pydracor) |
| [pymeasure](https://github.com/pymeasure/pymeasure/commits?author=afuetterer) | 2 | ![GitHub stars](https://img.shields.io/github/stars/pymeasure/pymeasure) | ![GitHub last commit](https://img.shields.io/github/last-commit/pymeasure/pymeasure) |
| [pypsa](https://github.com/pypsa/pypsa/commits?author=afuetterer) | 7 | ![GitHub stars](https://img.shields.io/github/stars/pypsa/pypsa) | ![GitHub last commit](https://img.shields.io/github/last-commit/pypsa/pypsa) |
| [rdmo](https://github.com/rdmorganiser/rdmo/commits?author=afuetterer) | 154 | ![GitHub stars](https://img.shields.io/github/stars/rdmorganiser/rdmo) | ![GitHub last commit](https://img.shields.io/github/last-commit/rdmorganiser/rdmo) |
| [rdmo-catalog](https://github.com/rdmorganiser/rdmo-catalog/commits?author=afuetterer) | 2 | ![GitHub stars](https://img.shields.io/github/stars/rdmorganiser/rdmo-catalog) | ![GitHub last commit](https://img.shields.io/github/last-commit/rdmorganiser/rdmo-catalog) |
| [rdmo-docs-en](https://github.com/rdmorganiser/rdmo-docs-en/commits?author=afuetterer) | 10 | ![GitHub stars](https://img.shields.io/github/stars/rdmorganiser/rdmo-docs-en) | ![GitHub last commit](https://img.shields.io/github/last-commit/rdmorganiser/rdmo-docs-en) |
| [rdmo-plugins](https://github.com/rdmorganiser/rdmo-plugins/commits?author=afuetterer) | 5 | ![GitHub stars](https://img.shields.io/github/stars/rdmorganiser/rdmo-plugins) | ![GitHub last commit](https://img.shields.io/github/last-commit/rdmorganiser/rdmo-plugins) |
| [the-turing-way](https://github.com/the-turing-way/the-turing-way/commits?author=afuetterer) | 2 | ![GitHub stars](https://img.shields.io/github/stars/the-turing-way/the-turing-way) | ![GitHub last commit](https://img.shields.io/github/last-commit/the-turing-way/the-turing-way) |
| [tika-python](https://github.com/chrismattmann/tika-python/commits?author=afuetterer) | 2 | ![GitHub stars](https://img.shields.io/github/stars/chrismattmann/tika-python) | ![GitHub last commit](https://img.shields.io/github/last-commit/chrismattmann/tika-python) |
| [using_the_re3data_API](https://github.com/re3data/using_the_re3data_API/commits?author=afuetterer) | 7 | ![GitHub stars](https://img.shields.io/github/stars/re3data/using_the_re3data_API) | ![GitHub last commit](https://img.shields.io/github/last-commit/re3data/using_the_re3data_API) |
| [xmlschema](https://github.com/sissaschool/xmlschema/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/sissaschool/xmlschema) | ![GitHub last commit](https://img.shields.io/github/last-commit/sissaschool/xmlschema) |
#### Open Source
| Name  | # My Commits | # Stars | Last Commit | 
| ----  | -------: | ---------- | ----------- | 
| [bertopic](https://github.com/maartengr/bertopic/commits?author=afuetterer) | 20 | ![GitHub stars](https://img.shields.io/github/stars/maartengr/bertopic) | ![GitHub last commit](https://img.shields.io/github/last-commit/maartengr/bertopic) |
| [cpython](https://github.com/python/cpython/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/python/cpython) | ![GitHub last commit](https://img.shields.io/github/last-commit/python/cpython) |
| [datasets](https://github.com/huggingface/datasets/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/huggingface/datasets) | ![GitHub last commit](https://img.shields.io/github/last-commit/huggingface/datasets) |
| [diffusers](https://github.com/huggingface/diffusers/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/huggingface/diffusers) | ![GitHub last commit](https://img.shields.io/github/last-commit/huggingface/diffusers) |
| [django-allauth](https://github.com/pennersr/django-allauth/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/pennersr/django-allauth) | ![GitHub last commit](https://img.shields.io/github/last-commit/pennersr/django-allauth) |
| [django-ninja](https://github.com/vitalik/django-ninja/commits?author=afuetterer) | 2 | ![GitHub stars](https://img.shields.io/github/stars/vitalik/django-ninja) | ![GitHub last commit](https://img.shields.io/github/last-commit/vitalik/django-ninja) |
| [drf-spectacular](https://github.com/tfranzel/drf-spectacular/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/tfranzel/drf-spectacular) | ![GitHub last commit](https://img.shields.io/github/last-commit/tfranzel/drf-spectacular) |
| [frictionless-py](https://github.com/frictionlessdata/frictionless-py/commits?author=afuetterer) | 2 | ![GitHub stars](https://img.shields.io/github/stars/frictionlessdata/frictionless-py) | ![GitHub last commit](https://img.shields.io/github/last-commit/frictionlessdata/frictionless-py) |
| [idutils](https://github.com/inveniosoftware/idutils/commits?author=afuetterer) | 3 | ![GitHub stars](https://img.shields.io/github/stars/inveniosoftware/idutils) | ![GitHub last commit](https://img.shields.io/github/last-commit/inveniosoftware/idutils) |
| [keybert](https://github.com/maartengr/keybert/commits?author=afuetterer) | 9 | ![GitHub stars](https://img.shields.io/github/stars/maartengr/keybert) | ![GitHub last commit](https://img.shields.io/github/last-commit/maartengr/keybert) |
| [numpy](https://github.com/numpy/numpy/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/numpy/numpy) | ![GitHub last commit](https://img.shields.io/github/last-commit/numpy/numpy) |
| [prompt-declaration-language](https://github.com/ibm/prompt-declaration-language/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/ibm/prompt-declaration-language) | ![GitHub last commit](https://img.shields.io/github/last-commit/ibm/prompt-declaration-language) |
| [python-semantic-release](https://github.com/python-semantic-release/python-semantic-release/commits?author=afuetterer) | 10 | ![GitHub stars](https://img.shields.io/github/stars/python-semantic-release/python-semantic-release) | ![GitHub last commit](https://img.shields.io/github/last-commit/python-semantic-release/python-semantic-release) |
| [schemathesis](https://github.com/schemathesis/schemathesis/commits?author=afuetterer) | 1 | ![GitHub stars](https://img.shields.io/github/stars/schemathesis/schemathesis) | ![GitHub last commit](https://img.shields.io/github/last-commit/schemathesis/schemathesis) |
| [scrapyd](https://github.com/scrapy/scrapyd/commits?author=afuetterer) | 3 | ![GitHub stars](https://img.shields.io/github/stars/scrapy/scrapyd) | ![GitHub last commit](https://img.shields.io/github/last-commit/scrapy/scrapyd) |
| [scrapyd-client](https://github.com/scrapy/scrapyd-client/commits?author=afuetterer) | 0 | ![GitHub stars](https://img.shields.io/github/stars/scrapy/scrapyd-client) | ![GitHub last commit](https://img.shields.io/github/last-commit/scrapy/scrapyd-client) |
| [spack](https://github.com/spack/spack/commits?author=afuetterer) | 0 | ![GitHub stars](https://img.shields.io/github/stars/spack/spack) | ![GitHub last commit](https://img.shields.io/github/last-commit/spack/spack) |
| [spack-packages](https://github.com/spack/spack-packages/commits?author=afuetterer) | 0 | ![GitHub stars](https://img.shields.io/github/stars/spack/spack-packages) | ![GitHub last commit](https://img.shields.io/github/last-commit/spack/spack-packages) |
| [transformers](https://github.com/huggingface/transformers/commits?author=afuetterer) | 0 | ![GitHub stars](https://img.shields.io/github/stars/huggingface/transformers) | ![GitHub last commit](https://img.shields.io/github/last-commit/huggingface/transformers) |
| [unasyncd](https://github.com/provinzkraut/unasyncd/commits?author=afuetterer) | 0 | ![GitHub stars](https://img.shields.io/github/stars/provinzkraut/unasyncd) | ![GitHub last commit](https://img.shields.io/github/last-commit/provinzkraut/unasyncd) |
| [xsdata](https://github.com/tefra/xsdata/commits?author=afuetterer) | 0 | ![GitHub stars](https://img.shields.io/github/stars/tefra/xsdata) | ![GitHub last commit](https://img.shields.io/github/last-commit/tefra/xsdata) |
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
