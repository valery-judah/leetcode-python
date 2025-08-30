from typing import List

# tags: coding-pattern/2-pointers
# given array in non-decreasing order
def solution(nums: List[int]) -> List[int]:
    left = 0
    right = len(nums) - 1
    squares = [x ** 2 for x in nums]
    out = []
    while left <= right:
        if squares[left] < squares[right]:
            out.append(squares[right])
            right -= 1
        else:
            out.append(squares[left])
            left += 1
    # revert massive
    out.reverse()
    return out


if __name__ == '__main__':
    massOne = [-2, 1, 4, 5]
    output = solution(massOne)
    print(output)
    desire = [1, 4, 16, 25]
    print(desire == output)
