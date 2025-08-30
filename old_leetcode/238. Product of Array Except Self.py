# tags: #tricks


def test(f):
    print(f([2, 3, 4, 1]))


# bruteforce approach
def productExceptSelf(nums: list[int]) -> list[int]:
    out = [1] * len(nums)
    for i, n in enumerate(nums):
        for j in range(0, len(nums)):
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
    product = [1] * len(nums)

    for i in range(1, len(nums)):
        pass
