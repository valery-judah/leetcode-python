def isValid(s: str) -> bool:
    stack = []
    openingBrackets = {"(", "[", "{"}
    closingBrackets = {")", "]", "}"}
    closeToOpen = {")": "(", "]": "[", "}": "{"}
    for elem in s:
        if elem in openingBrackets:
            stack.append(elem)
        elif elem in closingBrackets:
            if stack and closeToOpen[elem] == stack[-1]:
                stack.pop()
            else:
                return False
    return len(stack) == 0


if __name__ == "__main__":
    s = "(z)[]{((3 + 1)(()))}"
    print(isValid(s))

    toTest = []
    toTest.append(1)
    toTest.append(2)
    print(toTest)
    print(toTest.pop())
