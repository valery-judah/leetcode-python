def test(f):
    words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
    pattern = "abb"
    print(f(words, pattern))

    # Testing setdefault
    m = {}
    for c in "aqq":
        m.setdefault(c, len(m))
    print(m)


@test
def find_and_replace_pattern(words: list[str], pattern: str) -> list[str]:
    def match(word: str, cur_pattern: str) -> bool:
        word2pattern = dict()
        pattern2word = dict()
        if len(word) != len(cur_pattern):
            return False
        for i in range(len(word)):
            if word[i] not in word2pattern:
                word2pattern[word[i]] = cur_pattern[i]
            if cur_pattern[i] not in pattern2word:
                pattern2word[cur_pattern[i]] = word[i]
            if word2pattern[word[i]] != cur_pattern[i] or pattern2word[cur_pattern[i]] != word[i]:
                return False
        return True

    # todo caching

    def view(word: str):
        m = {}
        return [m.setdefault(c, len(m)) for c in word]

    return [w for w in words if view(w) == view(pattern)]
