from abc import ABC
from typing import Iterable
from domains.post import Post

class IPostRepository(ABC):

    async def get_all_posts(self) -> Iterable[Post] | None:
        pass