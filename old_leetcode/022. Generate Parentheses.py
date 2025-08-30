

def test(f):
    print(f(3))


@test
def generateParenthesis(n: int) -> list[str]:
    out = []

    def helper(l: int, r: int, brackets: str):
        if not l and not r:
            out.append(brackets)
        elif not l:
            helper(l, r - 1, brackets + ")")
        elif not r:
            helper(l - 1, r, brackets + "(")
        else:
            helper(l - 1, r, brackets + "(")
            if l < r:
                helper(l, r - 1, brackets + ")")

    helper(3, 3, "")
    return out


@test
def generateByNeetcode(n: int) -> list[str]:
    out = []

    def helper(open: int, close: int, brackets=""):
        if open == n and close == n:
            out.append(brackets)
        if open < n:
            helper(open + 1, close, brackets + "(")
        if close < open:
            helper(open, close + 1, brackets + ")")

    helper(0, 0)
    return out
