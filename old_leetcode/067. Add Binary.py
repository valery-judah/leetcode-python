def test(f):
    a = "11"
    b = "1"
    print(f(a, b))


@test
def add_binary_with_conversion(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]


@test
def add_binary(a, b):
    carry = 0
    max_len = max(len(a), len(b))
    res = ""
    a, b = a[::-1], b[::-1]
    for i in range(max_len):
        digit_a = (ord(a[i]) - ord("0")) if i < len(a) else 0
        digit_b = (ord(b[i]) - ord("0")) if i < len(b) else 0
        summ = digit_a + digit_b + carry
        res += str(summ % 2)
        carry = summ // 2
    if carry:
        res += "1"

    return res[::-1]
