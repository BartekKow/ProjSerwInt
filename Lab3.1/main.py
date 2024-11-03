from dependency_injector.wiring import Provide

import asyncio

from container import Container
from services.ipost_service import IPostService
from utils import consts

async def main(
        service: IPostService = Provide[Container.service],
) -> None:
    all_posts_json = await service.get_posts_json()
    posts_by_title = await service.get_posts_by_title(consts.title)
    posts_by_body = await service.get_posts_by_body(consts.body)

    print(all_posts_json)
    print(posts_by_title)
    print(posts_by_body)

if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])

    asyncio.run(main())

