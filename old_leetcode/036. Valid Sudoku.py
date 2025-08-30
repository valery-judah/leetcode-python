from collections import Counter


def test(f):
    sudoku = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(f(sudoku))






@test
def isValidSudoku(board: list[list[str]]) -> bool:

    def isUnique(slice):
        counter = Counter(slice)
        counter.pop(".")
        for v in counter.values():
            if v > 1:
                return False
        return True

    def getAreas(board: list[list[str]]):
        areas = []
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                areas.append(square)
        return areas

    rowsUnique = all([isUnique(row) for row in board])
    colsUnique = all([isUnique(col) for col in zip(*board, strict=False)])
    areasUnique = all([isUnique(area) for area in getAreas(board)])




    return rowsUnique and colsUnique and areasUnique
