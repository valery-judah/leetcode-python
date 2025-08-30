def lengthOfLongestSubstring(s: str) -> int:
    left = 0
    subset = {}
    max_len = 0
    for r in range(len(s)):
        while s[r] in subset:
            subset.pop(s[left])
            left += 1
        subset[s[r]] = r
        max_len = max(max_len, len(subset))
    return max_len


def test(f):
    strs = "abcabcbb"
    print(f(strs))


@test
def get_longest_len(s):
    unique_letters = set()  # fast lookup
    left = 0
    max_len = 0
    for letter in s:
        if letter not in unique_letters:
            unique_letters.add(letter)
            max_len = max(max_len, len(unique_letters))
        else:
            while s[left] in unique_letters:  # preserve invariant (all letters should be unique)
                unique_letters.remove(s[left])
                left += 1
            unique_letters.add(letter)
            max_len = max(max_len, len(unique_letters))
    return max_len

