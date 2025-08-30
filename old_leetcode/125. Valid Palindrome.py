def test(f):
    s = "A man, a plan, a canal: Panama"
    print(f(s))


@test
def is_palindrome(word: str) -> bool:
    word = word.lower()
    left, right = 0, len(word) - 1
    while left < right:
        while left < right and not word[left].isalnum():
            left += 1
        while left < right and not word[right].isalnum():
            right -= 1
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True
