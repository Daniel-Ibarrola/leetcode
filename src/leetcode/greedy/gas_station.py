def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    if sum(gas) < sum(cost):
        return -1

    # There must be a solution at this point
    start, gas_in_tank = 0, 0
    for index in range(len(gas)):
        if gas_in_tank + gas[index] - cost[index] < 0:
            start = index + 1
            gas_in_tank = 0
        else:
            gas_in_tank += gas[index] - cost[index]

    return start
