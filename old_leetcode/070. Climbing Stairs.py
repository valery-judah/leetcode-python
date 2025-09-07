def test(f):
    n = 3
    print(f(n))


@test
def climbStairs(n: int) -> int:
    ways = {1: 1, 2: 2}

    def helper(step):
        if step in ways:
            return ways[step]
        else:
            ways[step] = helper(step - 1) + helper(step - 2)
            return ways[step]

    return helper(n)


@test
def climb2(n: int) -> int:
    one, two = 1, 1
    for _ in range(n - 1):
        one, two = one + two, one
    return one
