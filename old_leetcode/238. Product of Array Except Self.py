# tags: #tricks


def test(f):
    print(f([2, 3, 4, 1]))


# bruteforce approach
def productExceptSelf(nums: list[int]) -> list[int]:
    out = [1] * len(nums)
    for i, _ in enumerate(nums):
        for j in range(len(nums)):
            if i != j:
                out[i] = out[i] * nums[j]
    return out


def productExceptSelf_other(nums: list[int]) -> list[int]:
    prefix = [1] * len(nums)
    for i in range(1, len(nums)):
        prefix[i] = nums[i - 1] * prefix[i - 1]

    suffix = [1] * len(nums)
    for i in reversed(range(len(nums) - 1)):
        suffix[i] = suffix[i + 1] * nums[i + 1]
    return [a * b for a, b in zip(prefix, suffix, strict=False)]


@test
def productExceptSelf_optimized(nums: list[int]) -> list[int]:
    res = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res
