def test(f):
    nums = [2, 3, -1, -1, 5]
    print(f(nums))


@test
def maxProd(nums):
    globalMax = nums[0]
    curMin = curMax = 1
    for n in nums:
        temp_max = max(curMax * n, curMin * n, n)
        curMin = min(curMax * n, curMin * n, n)
        curMax = temp_max
        globalMax = max(globalMax, curMax, n)
    return globalMax


def maxProduct(nums: list[int]) -> int:
    maxProd = nums[0]
    for i in range(len(nums)):
        curProduct = 1
        for j in range(i, len(nums)):
            curProduct *= nums[j]
            maxProd = max(maxProd, curProduct)
    return maxProd
