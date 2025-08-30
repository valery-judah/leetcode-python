def test(fun):
    s = "babad"
    print(fun(s))


@test
def longestPalindrome(s: str) -> str:
    res = ""
    lenMax = 0

    def anagramStat(l, r, res, lenMax):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > lenMax:
                lenMax = r - l + 1
                res = s[l : r + 1]
            l -= 1
            r += 1
        return res, lenMax

    for i in range(len(s)):
        l, r = i, i + 1
        res, lenMax = anagramStat(l, r, res, lenMax)

        l, r = i, i
        res, lenMax = anagramStat(l, r, res, lenMax)

    return res
