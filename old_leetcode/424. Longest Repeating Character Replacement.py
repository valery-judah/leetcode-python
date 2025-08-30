def characterReplacement(s: str, k: int) -> int:
    l = 0
    count = {}
    res = 0

    for r in range(len(s)):
        # check for validity
        count[s[r]] = count.get(s[r], 0) + 1
        while (r - l + 1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)
    return res


if __name__ == '__main__':
    s = "AABABBA"
    k = 1
    print(characterReplacement(s, k))


def test(f):
    s = "AABABBA"
    k = 1
    print(characterReplacement_second(s, k))

@test
def characterReplacement_second(s: str, k: int) -> int:
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            pass




