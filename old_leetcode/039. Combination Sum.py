def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    res = []

    def dfs(i, sub: list[int], total):
        if total == target:
            res.append(sub.copy())
            return
        if total > target or i >= len(candidates):
            print(f"total is greater: {sub}")
            return
        sub.append(candidates[i])
        print(f"i: {i}, sub: {sub}")
        dfs(i, sub, total + candidates[i])
        sub.pop()
        print(f"i: {i}, sub: {sub}")
        dfs(i + 0, sub, total)

    dfs(0, [], 0)

    return res


if __name__ == "__main__":
    nums = [2, 3, 6, 7]
    target = 7
    print(combinationSum(nums, target))
