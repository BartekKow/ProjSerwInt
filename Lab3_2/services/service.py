from datetime import datetime, timedelta
from typing import Iterable

from domains.post import PostRecord
from repositories.post_comment_repository import PostRepository
from services.iservice import IPostService
from domains.comment import CommentRecord
from repositories.post_comment_repository import CommentRepository
from services.iservice import ICommentService


class PostService(IPostService):
    repository: PostRepository

    def __init__(self, repository: PostRepository) -> None:
        self.repository = repository

    async def get_all_posts(self):
        return await self.repository.get_all_posts()

    async def get_posts_json(self):
        return await self.repository.get_posts_json()

    async def get_posts_by_title(self, title: str) -> list[PostRecord]:
        posts = await self.repository.get_all_posts()
        filtered_posts = [post for post in posts if title in post.title]
        return filtered_posts

    async def get_posts_by_body(self, body: str) -> list[PostRecord]:
        posts = await self.repository.get_all_posts()
        filtered_posts = [post for post in posts if body in post.body]
        return filtered_posts

    async def clean_old_posts(self, seconds: int) -> None:
        threshold = datetime.now() - timedelta(seconds=seconds)
        posts = await self.repository.get_all_posts()
        self.repository.posts = [post for post in posts if post.last_accessed > threshold]

    async def sort_by_last_accessed(self) -> Iterable[PostRecord]:
        posts = await self.repository.get_all_posts()
        return sorted(posts, key=lambda p: p.last_accessed)


class CommentService(ICommentService):
    repository: CommentRepository

    def __init__(self, repository: CommentRepository) -> None:
        self.repository = repository

    async def get_all_comments(self):
        return await self.repository.get_all_comments()

    async def get_comments_json(self):
        return await self.repository.get_comments_json()

    async def get_comments_by_name(self, name: str) -> list[CommentRecord]:
        comments = await self.repository.get_all_comments()
        filtered_comments = [comment for comment in comments if name in comment.name]
        return filtered_comments

    async def get_comments_by_body(self, body: str) -> list[CommentRecord]:
        comments = await self.repository.get_all_comments()
        filtered_comments = [comment for comment in comments if body in comment.body]
        return filtered_comments