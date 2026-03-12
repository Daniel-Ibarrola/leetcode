import threading


class OddEvenPrinter:

    def __init__(self, max_num: int):
        self._max_num = max_num
        self._current_num = 0
        self._condition = threading.Condition()

    def _print_odd(self) -> None:
        with self._condition:
            while self._current_num < self._max_num:

                if self._current_num % 2 == 0:
                    self._condition.wait()

                print(self._current_num)
                self._current_num += 1
                self._condition.notify()

    def _print_even(self) -> None:
        with self._condition:
            while self._current_num < self._max_num:

                if self._current_num % 2 == 1:
                    self._condition.wait()

                print(self._current_num)
                self._current_num += 1
                self._condition.notify()

    def print(self) -> None:
        threads = [
            threading.Thread(target=self._print_odd),
            threading.Thread(target=self._print_even),
        ]
        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()


if __name__ == "__main__":
    odd_even_printer = OddEvenPrinter(20)
    odd_even_printer.print()
