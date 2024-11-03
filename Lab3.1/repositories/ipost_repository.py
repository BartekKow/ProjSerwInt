from abc import ABC
from typing import Iterable
from domains.post import PostRecord

class IPostRepository(ABC):

    async def get_all_posts(self) -> Iterable[PostRecord] | None:
        pass