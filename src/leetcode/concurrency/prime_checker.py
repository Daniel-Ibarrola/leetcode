import multiprocessing


def is_prime(num: int) -> bool:
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def check_primes() -> None:
    """Check if numbers are prime."""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    with multiprocessing.Pool() as pool:
        results = pool.map(is_prime, numbers)

        for result, number in zip(results, numbers):
            if result:
                print(f"Is prime: {number}")


if __name__ == "__main__":
    check_primes()
