

def test(f):
    nums = [2, 3, -1, -1, 5]
    print(f(nums))


@test
def maxProd(nums):
    globalMax = nums[0]
    curMin = curMax = 1
    for n in nums:
        curMax, curMin = max(curMax * n, curMin * n, n), min(curMax * n, curMin * n, n)
        globalMax = max(globalMax, curMax, n)
    return globalMax

def maxProduct(nums: list[int]) -> int:
    maxProd = float("-inf")
    for i in range(len(nums)):
        curProduct = 1
        for j in range(i, len(nums)):
            curProduct *= nums[j]
            maxProd = max(maxProd, curProduct)
    return maxProd
