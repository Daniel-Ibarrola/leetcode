class Solution:
    @staticmethod
    def generate_spiral_matrix(size: int) -> list[list[int]]:
        assert size > 0, "Size must be greater than 1"

        matrix = [[0] * size for _ in range(size)]

        num = 1
        size_squared = size * size

        # Initialize the four boundary pointers
        top, bottom = 0, size - 1
        left, right = 0, size - 1

        while top <= bottom and left <= right:

            # Go left to right
            for ii in range(left, right + 1):
                matrix[top][ii] = num
                num += 1

            top += 1

            # Go downwards
            for ii in range(top, bottom + 1):
                matrix[ii][right] = num
                num += 1

            right -= 1

            # Go right to left
            if top <= bottom:
                for ii in range(right, left - 1, -1):
                    matrix[bottom][ii] = num
                    num += 1

                bottom -= 1

            # Go upwards
            if left <= right:
                for ii in range(bottom, top - 1, -1):
                    matrix[ii][left] = num
                    num += 1

                left += 1

        return matrix
