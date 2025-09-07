from collections import defaultdict


def groupAnagrams(strs):
    groups = defaultdict(list)
    for anagram in strs:
        array = [0] * 26
        for letter in anagram:
            letterPosition = ord(letter) - ord("a")
            array[letterPosition] += 1
        groups[tuple(array)].append(anagram)
    return list(groups.values())


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    output = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    print(groupAnagrams(strs))
