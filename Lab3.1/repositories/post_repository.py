import aiohttp

from utils import consts
from typing import Iterable
from domains.post import Post
from repositories.ipost_repository import IPostRepository

class PostRepository(IPostRepository):
    async def get_all_posts(self) -> Iterable[Post] | None:
        all_posts = await self.get_posts_json()
        parsed_posts = await self._parse_posts(all_posts)

        return parsed_posts

    async def get_posts_json(self) -> Iterable[dict] | None:
        async with aiohttp.ClientSession() as session:
            async with session.get(consts.API_URL.format()) as response:
                if response.status != 200:
                    return None

                return await response.json()

    async def _parse_posts(self, posts: Iterable[dict]) -> Iterable[Post]:
        return [Post(userId=record.get("userId"), id=record.get("id"), title=record.get('title'), body=record.get("body")) for record in posts]
