def test(f):
    s = "PAYPALISHIRING"
    numRows = 3
    print(f(s, numRows))


@test
def convert(s: str, numRows: int) -> str:
    v = 1
    row = 0
    out = [[]] * numRows
    for i in range(len(s)):
        out[row].append(s[i])
        row += v
        if row == 0 or row == numRows - 1:
            v = -v
        print(row)
    print(out)
