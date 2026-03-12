import multiprocessing


def count_words(text: str):
    return len(text.split())


def main():
    text = "Hello World " * 10
    chunks = [text[0 : len(text) // 2], text[len(text) // 2 :]]

    with multiprocessing.Pool() as pool:
        results = pool.map(count_words, chunks)
        for result in results:
            print(f"Words in chunk: {result}")
        print("Total words:", sum(results))


if __name__ == "__main__":
    main()
