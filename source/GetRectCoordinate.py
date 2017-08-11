# Problem: given 2D matrix filled with 1s. There is a rectangle inside that 2D
# matrix filled with 0s.
# Write a function to return the coordinate of top-left and bottom-right of
# that rectangle


class GetRectangleCoord:
    def solution(self, matrix):
        ROW = len(matrix)
        COL = len(matrix[0])
        start_row, start_col, end_row, end_col = 0, 0, 0, 0
        for start_row in range(ROW):
            for start_col in range(COL):
                if matrix[start_row][start_col] == 0:  # found top-left
                    end_row = start_row
                    end_col = start_col
                    # move down till "1"
                    while end_row < ROW:
                        if matrix[end_row][start_col] == 0:
                            end_row += 1
                        else:
                            break
                    # move right till "1"
                    while end_col < COL:
                        if matrix[start_row][end_col] == 0:
                            end_col += 1
                        else:
                            break
                    # found bottom-right
                    return [start_row, start_col, end_row - 1, end_col - 1]
        return [-1, -1, -1, -1]


solver = GetRectangleCoord()
matrix = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0]
]
print(solver.solution(matrix))
