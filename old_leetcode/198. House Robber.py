

def test(f):
    nums = [1, 2, 3, 1]
    print(f(nums))


@test
def rob(nums: list[int]) -> int:
    sub = [0] * len(nums)
    sub[0] = nums[0]
    sub[1] = max(nums[1], nums[0])
    for i in range(2, len(nums)):
        sub[i] = max(sub[i - 1], nums[i] + sub[i - 2])
    return sub[len(nums) - 1]


@test
def rob_dp(nums: list[int]) -> int:
    prev, cur = 0, 0
    for n in nums:
        prev, cur = cur, max(cur, prev + n)
    return cur
