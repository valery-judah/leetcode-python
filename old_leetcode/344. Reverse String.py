from typing import List


def test(f):
    letters = ["a", "s", "d", "w"]
    f(letters)
    print(letters)


@test
def reverseString(s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[right], s[left] = s[left], s[right]
        left += 1
        right -= 1
