def test(f):
    permutation = [1, 2, 5, 4, 0]
    f(permutation)
    print(permutation)


@test
def nextPermutation(nums: list[int]) -> None:

    i = len(nums) - 1
    while nums[i - 1] > nums[i]:
        i -= 1
    i -= 1  # find first descending position

    if i <= 0:
        nums.reverse()

    k = len(nums) - 1
    while nums[k] > nums[i]:
        k -= 1

    print(k)
