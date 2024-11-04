from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class CommentRecord:
    postId: int
    id: int
    name: str
    email: str
    body: str
    last_accessed: datetime = field(default_factory=datetime.now)