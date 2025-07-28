class Solution:
    @staticmethod
    def set_zeroes(matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows_with_zeros = set()
        cols_with_zeros = set()

        for ii in range(len(matrix)):
            for jj in range(len(matrix[ii])):
                if matrix[ii][jj] == 0:
                    rows_with_zeros.add(ii)
                    cols_with_zeros.add(jj)

        for row_index in rows_with_zeros:
            matrix[row_index] = [0] * len(matrix[row_index])

        for col_index in cols_with_zeros:
            for row in matrix:
                row[col_index] = 0
