def prefix_sums(arr: list[int | float]) -> list[int | float]:
    size = len(arr)
    sums = [0] * (size + 1)
    for ii in range(1, size + 1):
        sums[ii] = sums[ii - 1] + arr[ii - 1]
    return sums
