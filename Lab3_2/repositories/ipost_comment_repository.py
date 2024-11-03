from abc import ABC
from typing import Iterable
from domains.post import PostRecord
from domains.comment import CommentRecord

class IPostRepository(ABC):

    async def get_all_posts(self) -> Iterable[PostRecord] | None:
        pass

class ICommentRepository(ABC):

    async def get_all_comments(self) -> Iterable[CommentRecord] | None:
        pass