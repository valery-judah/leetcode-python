from collections import Counter


def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    s1_count = Counter(s1)
    s2_count = Counter()

    for i in range(len(s2)):
        s2_count[s2[i]] += 1
        if i >= len(s1):
            if s2_count[s2[i - len(s1)]] == 1:
                del s2_count[s2[i - len(s1)]]
            else:
                s2_count[s2[i - len(s1)]] -= 1
        if s1_count == s2_count:
            return True
    return False


if __name__ == "__main__":
    s1 = "ab"
    s2 = "xxxdba"
    print(checkInclusion(s1, s2))
