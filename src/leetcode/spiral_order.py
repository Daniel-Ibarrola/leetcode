class Solution:
    @staticmethod
    def spiral_order(matrix: list[list[int]]) -> list[int]:
        order: list[int] = []
        while matrix:
            # Traverse from right to left
            order += matrix.pop(0)

            # Traverse downwards
            for row in matrix:
                if row:
                    order.append(row.pop())

            # Traverse left to right
            if matrix:
                order += matrix.pop()[::-1]

            # Traverse upwards
            for row in reversed(matrix):
                if row:
                    order.append(row.pop(0))

        return order
