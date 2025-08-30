

def test(f):
    nums = [3, 2, 1, 0, 4]
    print(f(nums))


@test
def canJump_Neetcode(nums: list[int]) -> bool:
    goal = len(nums) - 1
    for i in reversed(range(len(nums) - 1)):
        if i + nums[i] >= goal:
            goal = i
    return goal == 0


@test
def canJump(nums: list[int]) -> bool:
    steps = 1
    for n in nums:
        if steps - 1 < 0:
            return False
        else:
            steps = max(steps - 1, n)
    return True
