import argparse
import sys
import os
import gitlab
from todoer import todoer
from typing import Dict, Any
from loguru import logger


def get_args() -> dict:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t", "--title", type=str, required=False, help="Regex of todo title to remove",
    )
    parser.add_argument(
        "-d",
        "--description",
        type=str,
        required=False,
        help="Regex of todo description to remove",
    )
    parser.add_argument(
        "-c",
        "--creator",
        type=str,
        required=False,
        help="Username of the issue creator",
    )
    return vars(parser.parse_args())


def setup_logger():
    logger.remove()
    logger.add(sys.stdout, colorize=True, format="<level>{message}</level>")


def get_gitlab() -> gitlab.Gitlab:
    gitlab_url: str = os.getenv("GITLAB_URL") or "https://gitlab.com"
    gitlab_token: str = os.getenv("GITLAB_TOKEN") or sys.exit(
        "No GITLAB_TOKEN provided."
    )
    return gitlab.Gitlab(gitlab_url, gitlab_token, per_page=100)


def main():
    setup_logger()
    args: Dict[str, Any] = get_args()
    gl: gitlab.Gitlab = get_gitlab()
    todoer.run(gl, args.get("title"), args.get("description"), args.get("creator"))
