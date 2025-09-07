from collections import Counter


def test(f):
    s = "abccccdd"
    print(f(s))
    print(9 // 2)


@test
def longestPalindrome(s: str) -> int:
    counter = Counter(s)
    maxLen = 0
    center = 0
    for v in counter.values():
        maxLen += v // 2 * 2
        if not center:
            center = v % 2
    return maxLen + center
