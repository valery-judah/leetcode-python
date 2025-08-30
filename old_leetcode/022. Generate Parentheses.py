def test(f):
    print(f(3))


@test
def generateParenthesis(n: int) -> list[str]:
    out = []

    def helper(left: int, right: int, brackets: str):
        if not left and not right:
            out.append(brackets)
        elif not left:
            helper(left, right - 1, brackets + ")")
        elif not right:
            helper(left - 1, right, brackets + "(")
        else:
            helper(left - 1, right, brackets + "(")
            if left < right:
                helper(left, right - 1, brackets + ")")

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
