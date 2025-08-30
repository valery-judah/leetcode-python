def test(f):
    nums = [1, 2, 3]
    print(f"out: {f(nums)}")


# Choose a num for a seat - DFS
# It's not backtracking


def myGivePermutations(nums: list[int]) -> list[list[int]]:
    out = []

    def helper(path: list[int], candidates):
        if not candidates:
            out.append(path)
        for i in range(len(candidates)):
            helper(path + [candidates[i]], candidates[:i] + candidates[i + 1 :])

    helper([], nums)
    return out


@test
def myBacktracking(nums):
    res = []

    def backtrack(curr: list[int]):
        print(f"in backtrack: {curr}")
        if len(curr) == len(nums):
            res.append(curr[:])
            print(f"return from {curr}")
            return
        for n in nums:
            if n not in curr:
                curr.append(n)
                print(f"call backtrack for n: {n}")
                backtrack(curr)
                curr.pop()

    backtrack([])
    return res


# DFS
def moreElegantFromLeetCode(nums):
    res = []

    def dfs(nums, path, res):
        if not nums:
            res.append(path)
            # return # backtracking

        for i in range(len(nums)):
            dfs(nums[:i] + nums[i + 1 :], path + [nums[i]], res)

    dfs(nums, [], res)
    return res


# leetCode solution without intensive copying
def permute(nums: list[int]) -> list[list[int]]:
    def backtrack(curr):
        if len(curr) == len(nums):
            ans.append(curr[:])
            return

        for num in nums:
            if num not in curr:
                curr.append(num)
                backtrack(curr)
                curr.pop()

    ans = []
    backtrack([])
    return ans


def permute(nums: list[int]) -> list[list[int]]:
    candidates = set(nums)
    res = []

    def dfs(sub: list[int], currentCandidates: set[int]):
        print(f"sub: {sub}, currentCandidates: {currentCandidates}")
        if not currentCandidates:
            res.append(sub.copy())
            return
        for elem in currentCandidates:
            subb = sub.copy()
            subb.append(elem)
            cur = candidates.copy()
            cur.remove(elem)
            dfs(subb, cur)

    dfs([], candidates)

    return res
