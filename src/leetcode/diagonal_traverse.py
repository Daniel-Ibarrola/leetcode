class Solution:
    @staticmethod
    def diagonal_traverse(mat: list[list[int]]) -> list[int]:
        if not mat:
            return []

        num_rows = len(mat)
        num_cols = len(mat[0])
        size = num_rows * num_cols

        result: list[int] = [0] * size
        result_index = 0

        current_row = 0
        current_col = 0

        going_up = True
        while current_row < num_rows and current_col < num_cols:
            result[result_index] = mat[current_row][current_col]
            result_index += 1

            if going_up:
                # Start descending at the row below
                if current_col == num_cols - 1:
                    current_row += 1
                    going_up = False

                # Start descending at the column to the right
                elif current_row == 0:
                    current_col += 1
                    going_up = False

                else:
                    # One row up and one column to the right
                    current_row -= 1
                    current_col += 1

            else:

                # Start ascending at the column to the right
                if current_row == num_rows - 1:
                    current_col += 1
                    going_up = True

                # Start ascending at the row below
                elif current_col == 0:
                    current_row += 1
                    going_up = True

                else:
                    # One row down and one column to the left
                    current_row += 1
                    current_col -= 1

        return result
