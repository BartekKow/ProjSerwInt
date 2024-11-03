from dependency_injector import containers, providers

from repositories.post_comment_repository import PostRepository
from services.service import PostService

from repositories.post_comment_repository import CommentRepository
from services.service import CommentService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    repository = providers.Singleton(
        PostRepository,
    )


    service = providers.Factory(
        PostService,
        repository=repository,
    )

    C_repository = providers.Singleton(
        CommentRepository,
    )


    C_service = providers.Factory(
        CommentService,
        repository=C_repository,
    )