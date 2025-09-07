def test(fun):
    s = "babad"
    print(fun(s))


@test
def longestPalindrome(s: str) -> str:
    res = ""
    lenMax = 0

    def expand_around_center(left: int, right: int, res: str, lenMax: int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > lenMax:
                lenMax = right - left + 1
                res = s[left : right + 1]
            left -= 1
            right += 1
        return res, lenMax

    for i in range(len(s)):
        left, right = i, i + 1
        res, lenMax = expand_around_center(left, right, res, lenMax)

        left, right = i, i
        res, lenMax = expand_around_center(left, right, res, lenMax)

    return res
