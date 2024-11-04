from dependency_injector.wiring import Provide

import asyncio

from container import Container
from services.iservice import IPostService
from services.iservice import ICommentService


async def main(
        post_service: IPostService = Provide[Container.post_service],
        comm_service: ICommentService = Provide[Container.comment_service],
) -> None:
    print("Pobieranie wszystkich postów:")
    posts = await post_service.get_all_posts()
    print(posts)

    print("\nPobieranie postów w formacie JSON:")
    posts_json = await post_service.get_posts_json()
    print(posts_json)

    print("\nFiltrowanie postów według tytułu:")
    filtered_by_title = await post_service.get_posts_by_title("eum et est occaecati")
    print(filtered_by_title)

    print("\nFiltrowanie postów według treści:")
    filtered_by_body = await (
        post_service.get_posts_by_body("quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architect"))
    print(filtered_by_body)

    print("\nPobieranie wszystkich komentarzy:")
    comments = await comm_service.get_all_comments()
    print(comments)

    print("\nFiltrowanie komentarzy według treści:")
    filtered_comments = await (
        comm_service.get_comments_by_body("laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"))
    print(filtered_comments)


if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])

    asyncio.run(main())
