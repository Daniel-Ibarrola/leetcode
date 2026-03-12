import queue
import threading
import time


def print_first(first_finished: threading.Event) -> None:
    print("First")
    first_finished.set()


def print_second(
    first_finished: threading.Event, second_finished: threading.Event
) -> None:
    first_finished.wait()
    print("Second")
    second_finished.set()


def print_third(second_finished: threading.Event) -> None:
    second_finished.wait()
    print("Third")


def print_in_order() -> None:
    first_finished = threading.Event()
    second_finished = threading.Event()
    threads = [
        threading.Thread(target=print_first, args=(first_finished,)),
        threading.Thread(target=print_second, args=(first_finished, second_finished)),
        threading.Thread(target=print_third, args=(second_finished,)),
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("Done")


def produce_some_tasks(tasks: queue.Queue[str], name: str) -> None:
    for i in range(10):
        tasks.put(f"{name} task {i}")
        time.sleep(0.1)


def consume_some_tasks(tasks: queue.Queue[str], name: str) -> None:
    while True:
        try:
            task = tasks.get(timeout=1)
        except queue.Empty:
            print("No tasks left to consume.")
            break
        print(f"Consumer {name} {task}")
        tasks.task_done()


def produce_and_consume_tasks() -> None:
    tasks = queue.Queue()
    producers = [
        threading.Thread(target=produce_some_tasks, args=(tasks, "P1")),
        threading.Thread(target=produce_some_tasks, args=(tasks, "P2")),
    ]
    consumers = [
        threading.Thread(target=consume_some_tasks, args=(tasks, "C1")),
        threading.Thread(target=consume_some_tasks, args=(tasks, "C2")),
    ]

    for thread in producers:
        thread.start()

    for thread in consumers:
        thread.start()

    for thread in producers:
        thread.join()

    for thread in consumers:
        thread.join()

    print("Done")


if __name__ == "__main__":
    produce_and_consume_tasks()
