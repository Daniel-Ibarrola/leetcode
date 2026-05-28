import asyncio

SENTINEL = None


async def produce_some_tasks(queue: asyncio.Queue[str], name: str) -> None:
    print(f"Producer {name} started")
    for i in range(10):
        item = f"{name} task {i}"
        print(f"Producer {name} producing {item}")
        await queue.put(item)
        await asyncio.sleep(0.1)

    print(f"Producer {name} done")


async def consume_some_tasks(queue: asyncio.Queue[str], name: str) -> None:
    print(f"Consumer {name} started")
    while True:
        item = await queue.get()

        if item is SENTINEL:
            queue.task_done()
            break

        print(f"Consumer {name} processing {item}")
        await asyncio.sleep(0.2)
        queue.task_done()

    print(f"Consumer {name} done")


async def main():
    queue: asyncio.Queue[str | None] = asyncio.Queue()

    producers = [
        asyncio.create_task(produce_some_tasks(queue, "P1")),
        asyncio.create_task(produce_some_tasks(queue, "P2")),
    ]

    consumers = [
        asyncio.create_task(consume_some_tasks(queue, "C1")),
        asyncio.create_task(consume_some_tasks(queue, "C2")),
    ]

    # wait for producers
    await asyncio.gather(*producers)

    # wait until all produced tasks are processed
    await queue.join()

    # stop consumers
    for _ in consumers:
        await queue.put(SENTINEL)

    await asyncio.gather(*consumers)

    print("Done")


if __name__ == "__main__":
    asyncio.run(main())
