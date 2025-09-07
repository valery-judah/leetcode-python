import sys


def test(f):
    nums = [1, -2, 3, -1, 5]
    maxSum = f(nums)
    print(maxSum)


@test
def maxSub(nums: list[int]) -> int:
    curMax = globalMax = -sys.maxsize
    for n in nums:
        curMax = max(n, n + curMax)
        if globalMax < curMax:
            globalMax = curMax
        print(f"n: {n}, curMax = {curMax}, globalMax = {globalMax}")
    return globalMax
