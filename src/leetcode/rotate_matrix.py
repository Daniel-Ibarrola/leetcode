class Solution:
    @staticmethod
    def rotate(matrix: list[list[int]]) -> None:
        """
        Rotates a square matrix 90 degrees clockwise in-place.
        """
        size = len(matrix)

        # 1. Transpose the matrix across the main diagonal
        # We only need to iterate through the upper triangle (where jj > ii)
        for ii in range(size):
            for jj in range(ii + 1, size):
                # Swap the element at (ii, jj) with the element at (jj, ii)
                matrix[ii][jj], matrix[jj][ii] = matrix[jj][ii], matrix[ii][jj]

        # 2. Reverse each row of the transposed matrix
        for ii in range(size):
            matrix[ii].reverse()
