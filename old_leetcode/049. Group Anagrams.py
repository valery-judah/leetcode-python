from collections import defaultdict
from functools import lru_cache
from typing import List


def test(f):
    words = ["bat", "cat", "tac", "tacc"]
    print(f(words))


def get_word_representation(word: str) -> List[int]:
    key_array = [0] * 26
    for letter in word:
        key = ord(letter) - ord('a')
        key_array[key] += ord(letter)
    return key_array


@test
def groupAnagrams_dict(strs: List[str]) -> List[List[str]]:
    anagrams = defaultdict(list)
    for word in strs:
        group_key = tuple(get_word_representation(word))
        anagrams[group_key].append(word)
    return list(anagrams.values())


@lru_cache(maxsize=None)
def get_hist_representation(word):
    group_key = defaultdict(int)
    for letter in word:
        group_key[letter] += 1
    vals = [item for item in sorted(group_key.items())]
    return tuple(vals)


@test
def groupAnagrams_dict(strs: List[str]) -> List[List[str]]:
    anagrams = defaultdict(list)
    for word in strs:
        group_key = get_hist_representation(word)
        # we can optimize this further
        anagrams[group_key].append(word)
    return list(anagrams.values())
