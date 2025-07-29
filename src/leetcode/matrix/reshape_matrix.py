class Solution:
    @staticmethod
    def matrix_reshape(
        mat: list[list[int]], n_rows: int, n_columns: int
    ) -> list[list[int]]:
        original_size = len(mat) * len(mat[0])
        if original_size != n_rows * n_columns:
            return mat

        reshaped_matrix: list[list[int]] = [[0] * n_columns for _ in range(n_rows)]
        reshaped_row, reshaped_col = 0, 0

        for original_row in range(len(mat)):
            for original_col in range(len(mat[0])):
                reshaped_matrix[reshaped_row][reshaped_col] = mat[original_row][
                    original_col
                ]

                reshaped_col += 1

                if reshaped_col == n_columns:
                    reshaped_row += 1
                    reshaped_col = 0

        return reshaped_matrix
