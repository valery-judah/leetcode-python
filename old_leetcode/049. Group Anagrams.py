from collections import defaultdict
from functools import cache


def test(f):
    words = ["bat", "cat", "tac", "tacc"]
    print(f(words))


def get_word_representation(word: str) -> list[int]:
    key_array = [0] * 26
    for letter in word:
        key = ord(letter) - ord("a")
        key_array[key] += ord(letter)
    return key_array


@test
def groupAnagrams_dict(strs: list[str]) -> list[list[str]]:
    anagrams = defaultdict(list)
    for word in strs:
        group_key = tuple(get_word_representation(word))
        anagrams[group_key].append(word)
    return list(anagrams.values())


@cache
def get_hist_representation(word):
    group_key = defaultdict(int)
    for letter in word:
        group_key[letter] += 1
    vals = [item for item in sorted(group_key.items())]
    return tuple(vals)


@test
def groupAnagrams_histogram(strs: list[str]) -> list[list[str]]:
    anagrams = defaultdict(list)
    for word in strs:
        group_key = get_hist_representation(word)
        # we can optimize this further
        anagrams[group_key].append(word)
    return list(anagrams.values())
