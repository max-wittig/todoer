# todoer

Remove your todos on GitLab based on different criteria.

### build

```sh
poetry install --no-dev --no-root
poetry build
```

### installation

```sh
pip3 install dist/todoer-0.1.0-py3-none-any.whl
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

