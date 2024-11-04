from abc import ABC
from typing import Iterable

from domains.post import PostRecord


class IPostService(ABC):

    async def get_all_posts(self) -> str:
        pass

    async def get_posts_json(self) -> str:
        pass

    async def get_posts_by_title(self, title: str) -> str:
        pass

    async def get_posts_by_body(self, body: str) -> str:
        pass

    async def sort_by_last_accessed(self) -> Iterable[PostRecord]:
        pass

    async def clean_old_posts(self, seconds: int) -> None:
        pass


class ICommentService(ABC):

    async def get_all_comments(self) -> str:
        pass

    async def get_comments_json(self) -> str:
        pass

    async def get_comments_by_name(self, name: str) -> str:
        pass

    async def get_comments_by_body(self, body: str) -> str:
        pass

    async def get_posts_by_author(self, body: str) -> str:
        pass