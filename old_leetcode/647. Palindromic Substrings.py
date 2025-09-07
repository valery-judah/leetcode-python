def test(f):
    s = "baaba"
    print(f(s))


@test
def palindromeNumbers(s: str) -> int:
    res = 0

    def getPalindromeNumber(s, left, right):
        res = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            res += 1
            left -= 1
            right += 1
        return res

    for i in range(len(s)):
        res += getPalindromeNumber(s, i, i)
        res += getPalindromeNumber(s, i, i + 1)

    return res
