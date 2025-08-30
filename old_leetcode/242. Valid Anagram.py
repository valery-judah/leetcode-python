def test(f):
    print(f("asf", "fsa"))
    print(f("asf", "fsai"))


@test
def isAnagram(s: str, t: str) -> bool:
    # create histogram function
    def get_histogram(word: str):
        histogram = {}
        for letter in word:
            histogram[letter] = histogram.get(letter, 0) + 1
        return histogram

    s_histogram = get_histogram(s)
    t_histogram = get_histogram(t)
    return s_histogram == t_histogram


@test
def isAnagram_alt(s: str, t: str) -> bool:
    def get_histogram(word: str):
        histogram = {}
        for letter in word:
            histogram[letter] = histogram.get(letter, 0) + 1
        return histogram

    def isEqual(s: dict, t: dict):
        return s == t

    return isEqual(get_histogram(s), get_histogram(t))
