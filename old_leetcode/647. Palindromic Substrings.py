def test(f):
    s = "baaba"
    print(f(s))


@test
def palindromeNumbers(s: str) -> int:
    res = 0

    def getPalindromeNumber(s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res

    for i in range(len(s)):
        res += getPalindromeNumber(s, i, i)
        res += getPalindromeNumber(s, i, i + 1)

    return res
