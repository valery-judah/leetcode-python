def dailyTemperatures(temperatures: list[int]) -> list[int]:
    stack = []
    days = [0] * len(temperatures)
    for i in range(len(temperatures)):
        if stack:
            while stack and temperatures[stack[-1]] < temperatures[i]:
                prev = stack.pop()
                days[prev] = i - prev
        stack.append(i)
    return days


if __name__ == "__main__":
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(dailyTemperatures(temperatures))
