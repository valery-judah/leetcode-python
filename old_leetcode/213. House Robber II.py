def test(f):
    nums = [2, 3, 2]
    print(f(nums))


@test
def rob(nums: list[int]):
    def helper(nums):
        prev, cur = 0, 0
        for n in nums:
            prev, cur = cur, max(n + prev, cur)
        return cur

    return max(nums[0], helper(nums[1:]), helper(nums[:-1]))
