# todoer

[![PyPI](https://badge.fury.io/py/todoer.svg)](https://badge.fury.io/py/todoer)
[![PyPI - License](https://img.shields.io/pypi/l/todoer.svg)](https://github.com/max-wittig/todoer/blob/master/LICENSE)
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

Remove your todos on GitLab based on different criteria.

### build

```sh
poetry install --no-dev --no-root
poetry build
```

### installation

```sh
pip3 install todoer
```

### usage

Specific the following environment variables:

* GITLAB_URL (defaults to `https://gitlab.com`)
* GITLAB_TOKEN

```sh
usage: todoer [-h] [-t TITLE] [-d DESCRIPTION] [-c CREATOR]

optional arguments:
  -h, --help            show this help message and exit
  -t TITLE, --title TITLE
                        Regex of todo title to remove
  -d DESCRIPTION, --description DESCRIPTION
                        Regex of todo description to remove
  -c CREATOR, --creator CREATOR
                        Username of the issue creator
```

