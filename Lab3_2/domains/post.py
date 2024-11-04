from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class PostRecord:
    userId: int
    id: int
    title: str
    body: str
    last_accessed: datetime = field(default_factory=datetime.now)