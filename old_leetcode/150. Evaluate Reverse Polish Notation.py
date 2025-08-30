def evalRPN(tokens: list[str]) -> int:
    stack = []
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }

    for token in tokens:
        if token not in operations:
            stack.append(int(token))
        else:
            right = stack.pop()
            left = stack.pop()
            fun = operations[token]
            stack.append(int(fun(left, right)))
    return stack[-1]


if __name__ == "__main__":
    tokens = ["4", "13", "5", "/", "+"]
    answer = 6
    print(evalRPN(tokens))
    print(int(13 / 5))
