from typing import Iterable

from domains.post import PostRecord
from repositories.post_repository import PostRepository
from services.ipost_service import IPostService


class PostService(IPostService):
    repository: PostRepository

    def __init__(self, repository: PostRepository) -> None:
        self.repository = repository

    async def get_all_posts(self) -> Iterable[PostRecord] | None:
        return await self.repository.get_all_posts()

    async def get_posts_json(self) -> Iterable[dict] | None:
        return await self.repository.get_posts_json()

    async def get_posts_by_title(self, title: str) -> list[PostRecord]:
        posts = await self.repository.get_all_posts()
        filtered_posts = [post for post in posts if title in post.title]
        return filtered_posts

    async def get_posts_by_body(self, body: str) -> list[PostRecord]:
        posts = await self.repository.get_all_posts()
        filtered_posts = [post for post in posts if body in post.body]
        return filtered_posts