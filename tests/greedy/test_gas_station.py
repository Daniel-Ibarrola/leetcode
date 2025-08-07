import pytest
from leetcode.greedy.gas_station import can_complete_circuit


@pytest.mark.parametrize(
    "gas, cost, expected",
    [
        # Example cases
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
        ([2, 3, 4], [3, 4, 3], -1),
        # Exact gas at each step
        ([5, 1, 2, 3, 4], [4, 4, 1, 5, 1], 4),
        # Only one station, enough gas
        ([5], [4], 0),
        # Only one station, not enough gas
        ([3], [4], -1),
        # Gas always less than cost
        ([1, 1, 1], [2, 2, 2], -1),
        # Gas always greater than cost
        ([3, 3, 3], [2, 2, 2], 0),
        # Start must be at last station
        ([2, 3, 4], [3, 4, 2], 2),
        # Requires scanning through multiple bad starts
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
    ],
)
def test_can_complete_circuit(gas: list[int], cost: list[int], expected: int):
    assert can_complete_circuit(gas, cost) == expected
