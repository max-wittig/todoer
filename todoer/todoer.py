import gitlab
import re
from typing import Optional
from loguru import logger


def run(
    gl: gitlab.Gitlab,
    title_pattern: Optional[str] = None,
    description_pattern: Optional[str] = None,
    creator_username: Optional[str] = None,
):
    for todo in gl.todos.list():
        todo_title: str = todo.attributes["target"]["title"]
        todo_description: str = todo.attributes["target"]["description"]
        todo_creator: str = todo.attributes["author"]["username"]
        done: bool = False
        if title_pattern:
            if re.match(title_pattern, todo_title):
                done = True
        if description_pattern:
            if re.match(description_pattern, todo_description):
                done = True
            else:
                done = False
        if creator_username:
            if creator_username == todo_creator:
                done = True
            else:
                done = False
        if done:
            todo.mark_as_done()
            logger.info(f"{todo_title} was marked as done.")
