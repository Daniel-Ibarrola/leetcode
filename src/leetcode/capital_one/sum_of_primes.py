def sum_of_primes(n: int) -> int:
    """Given a non-negative integer n, return the sum of all prime numbers from 0 to n (inclusive).

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

    Example 1:
        Input: n = 10
        Output: 17
        Explanation: Primes up to 10 are 2, 3, 5, 7. Their sum is 17.

    Example 2:
        Input: n = 1
        Output: 0
        Explanation: There are no prime numbers <= 1.

    Example 3:
        Input: n = 2
        Output: 2
        Explanation: 2 is the only prime <= 2.

    Constraints:
        - 0 <= n <= 10^6

    :param n: upper bound (inclusive)
    :return: sum of all primes from 0 to n
    """
    sum_ = 0

    for num in range(2, n + 1):
        is_prime = True

        for divisor in range(2, (num // 2) + 1):
            if num % divisor == 0:
                is_prime = False
                break

        if is_prime:
            sum_ += num

    return sum_
