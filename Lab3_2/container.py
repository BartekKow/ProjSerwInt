from dependency_injector import containers, providers

from repositories.post_comment_repository import PostRepository
from services.service import PostService

from repositories.post_comment_repository import CommentRepository
from services.service import CommentService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    post_repository = providers.Singleton(
        PostRepository,
    )

    post_service = providers.Factory(
        PostService,
        repository=post_repository,
    )

    comment_repository = providers.Singleton(
        CommentRepository,
    )

    comment_service = providers.Factory(
        CommentService,
        repository=comment_repository,
    )