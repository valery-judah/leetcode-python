def test(f):
    nums = [1, 2, 3]
    print(f(nums))


@test
def subsetsMy(nums: list[int]):
    out = []

    def helper(partialSubset: list[int], i: int):
        if i == len(nums):
            subsetToAdd = partialSubset.copy()
            out.append(subsetToAdd)
            return
        partialSubset.append(nums[i])
        helper(partialSubset, i + 1)
        partialSubset.remove(nums[i])
        helper(partialSubset, i + 1)

    helper([], 0)
    return out


def subsets(nums: list[int]) -> list[list[int]]:
    """
    Backtracking approach of neetcode project
    :param nums:
    :return:
    """
    res = []
    subset = []

    def dfs(i):
        if i >= len(nums):
            print(f"i: {i}, subset: {subset}")
            res.append(subset.copy())
            return
        subset.append(nums[i])
        print(f"1st: {subset}")
        dfs(i + 1)

        subset.pop()
        print(f"2nd: {subset}")
        dfs(i + 1)

    dfs(0)
    return res


def subsets_cascading(nums: list[int]) -> list[list[int]]:
    """
    Leetcode cascading approach
    :param self:
    :param nums:
    :return:
    """
    output = [[]]

    for num in nums:
        output += [curr + [num] for curr in output]

    return output


def subsets_back2(nums: list[int]) -> list[list[int]]:
    def backtrack(first=0, curr=[]):
        # if the combination is done
        if len(curr) == k:
            output.append(curr[:])
            return
        for i in range(first, n):
            # add nums[i] into the current combination
            curr.append(nums[i])
            # use next integers to complete the combination
            backtrack(i + 1, curr)
            # backtrack
            curr.pop()

    output = []
    n = len(nums)
    for k in range(n + 1):
        backtrack()
    return output
