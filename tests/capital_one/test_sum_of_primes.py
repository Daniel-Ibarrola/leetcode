from leetcode.capital_one.sum_of_primes import sum_of_primes


class TestSumOfPrimes:

    def test_up_to_ten(self):
        assert sum_of_primes(10) == 17  # 2 + 3 + 5 + 7

    def test_zero(self):
        assert sum_of_primes(0) == 0

    def test_one(self):
        assert sum_of_primes(1) == 0

    def test_two(self):
        assert sum_of_primes(2) == 2

    def test_prime_boundary(self):
        assert sum_of_primes(7) == 17  # 2 + 3 + 5 + 7

    def test_non_prime_boundary(self):
        assert sum_of_primes(9) == 17  # 8 and 9 are not prime

    def test_larger_input(self):
        assert sum_of_primes(20) == 77  # 2+3+5+7+11+13+17+19
