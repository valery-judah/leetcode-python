class Solution:
    # Binary Search
    def search(self, nums: list[int], target: int) -> int:
        pass


if __name__ == "__main__":
    solver = Solution()

    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    assert solver.search(nums, target) == 4
