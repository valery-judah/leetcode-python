from collections import Counter


def checkInclusion(s1: str, s2: str) -> bool:
    l = 0
    firstCount = Counter(s1)
    stringCount = {}
    for i in range(len(s1) - len(s1)):
        word2check = s2[i : i + len(s1)]


if __name__ == "__main__":
    s1 = "ab"
    s2 = "xxxdba"
    print(checkInclusion(s1, s2))
