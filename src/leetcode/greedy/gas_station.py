def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    """
    There are n gas stations along a circular route.

    You are given two integer arrays stations and cost of length n.
    At each gas station i, stations[i] represents the amount of gas you receive by stopping at this station,
    and costs[i] represents the amount of gas required to travel from station i to the next station.
    You begin the journey with an empty tank at one of the gas stations.

    Write a function to return the starting gas station's index if you can travel around the circuit once
    in the clockwise direction; otherwise, return -1. Note that if there exists a solution, it is guaranteed
    to be unique. Also, you can only travel from station i to station i + 1, and the last station will lead back
    to the first station.

    """
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
