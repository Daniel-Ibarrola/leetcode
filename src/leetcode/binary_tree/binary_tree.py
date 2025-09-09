from collections import deque
from typing import Generic, TypeVar, Optional

T = TypeVar("T")


class TreeNode(Generic[T]):
    def __init__(
        self,
        val: T,
        left: Optional["TreeNode[T]"] = None,
        right: Optional["TreeNode[T]"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree(Generic[T]):
    def __init__(self, root: Optional[TreeNode[T]] = None):
        self.root = root

    def max_depth(self) -> int:
        def _helper(node: Optional[TreeNode[T]]) -> int:
            if node is None:
                return 0
            left_depth = _helper(node.left)
            right_depth = _helper(node.right)
            return max(left_depth, right_depth) + 1

        return _helper(self.root)

    def diameter(self) -> int:
        max_diameter = 0

        def _helper(node: Optional[TreeNode[T]]) -> int:
            nonlocal max_diameter
            if node is None:
                return 0
            left_depth = _helper(node.left)
            right_depth = _helper(node.right)

            max_diameter = max(max_diameter, left_depth + right_depth)
            return max(left_depth, right_depth) + 1

        _helper(self.root)
        return max_diameter

    def level_order_traversal(self) -> list[T]:
        if not self.root:
            return []

        queue = deque([self.root])
        result = []

        while queue:
            node = queue.popleft()
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result

    def rightmost_node(self) -> list[T]:
        if not self.root:
            return []

        right_nodes: list[T] = []
        queue = deque([self.root])

        while queue:
            level_size = len(queue)

            for ii in range(level_size):
                current_node = queue.popleft()

                if ii == level_size - 1:
                    right_nodes.append(current_node.val)

                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

        return right_nodes


NumericT = TypeVar("NumericT", int, float)


class NumericTreeNode(TreeNode[NumericT]):
    def __init__(
        self,
        val: NumericT,
        left: Optional["NumericTreeNode[NumericT]"] = None,
        right: Optional["NumericTreeNode[NumericT]"] = None,
    ):
        if not isinstance(val, (int, float)):
            raise TypeError("Node value must be an integer or a float.")
        super().__init__(val, left, right)


class NumericBinaryTree(BinaryTree[NumericT]):
    def __init__(self, root: Optional[NumericTreeNode[NumericT]] = None):
        super().__init__(root)

    def sum(self) -> NumericT:
        def _helper(node: Optional[NumericTreeNode[NumericT]]) -> NumericT:
            if node is None:
                return 0
            left_sum = _helper(node.left)
            right_sum = _helper(node.right)
            return left_sum + right_sum + node.val

        return _helper(self.root)

    def max(self) -> Optional[NumericT]:
        """
        Finds the maximum value within the tree

        This method calculates the maximum value contained within the tree
        If the tree is empty, the result will be `None`.

        :return: The maximum value as an instance of the NumericT type if the
            tree contains elements, otherwise `None`.
        """

        def _helper(node: Optional[NumericTreeNode[NumericT]]) -> NumericT:
            if node is None:
                return float("-inf")
            left_max = _helper(node.left)
            right_max = _helper(node.right)
            return max(left_max, right_max, node.val)

        max_val = _helper(self.root)
        return max_val if max_val != float("-inf") else None

    def path_sum(self, target_sum: NumericT) -> bool:
        """Return true if the tree has a root-to-leaf path such that adding
        up all the values along the path equals target_sum.

        :param target_sum: the target sum
        :return: Whether the target sum is found in the tree
        """

        def _helper(
            node: Optional[NumericTreeNode[NumericT]], remaining_sum: NumericT
        ) -> bool:
            if not node:
                return False

            # If we are at a leaf node, check if its value equals the remaining sum.
            if not node.left and not node.right:
                return remaining_sum == node.val

            # Recurse down, subtracting the current node's value from the remaining sum.
            return _helper(node.left, remaining_sum - node.val) or _helper(
                node.right, remaining_sum - node.val
            )

        return _helper(self.root, target_sum)

    def path_sum_paths(self, target_sum: NumericT) -> list[list[NumericT]]:
        """Return a list of all root-to-leaf paths in the tree that sum to target_sum."""
        paths: list[list[NumericT]] = []
        current_path: list[NumericT] = []

        def _helper(
            node: Optional[NumericTreeNode[NumericT]], remaining_sum: NumericT
        ) -> None:
            if not node:
                return

            current_path.append(node.val)

            # Leaf Node
            if not node.left and not node.right and remaining_sum == node.val:
                paths.append(current_path.copy())

            _helper(node.left, remaining_sum - node.val) or _helper(
                node.right, remaining_sum - node.val
            )

            current_path.pop()

        _helper(self.root, target_sum)
        return paths

    def num_good_nodes(self) -> int:
        def _helper(
            node: Optional[NumericTreeNode[NumericT]], path_max: NumericT
        ) -> int:
            if not node:
                return 0

            count = 1 if node.val >= path_max else 0
            new_max = max(path_max, node.val)
            count += _helper(node.left, new_max)
            count += _helper(node.right, new_max)
            return count

        return _helper(self.root, float("-inf"))

    def good_nodes(self) -> list[NumericT]:
        good_nodes_list: list[NumericT] = []

        def _helper(
            node: Optional[NumericTreeNode[NumericT]], path_max: NumericT
        ) -> None:
            if not node:
                return

            if node.val >= path_max:
                good_nodes_list.append(node.val)

            new_max = max(path_max, node.val)
            _helper(node.left, new_max)
            _helper(node.right, new_max)

        _helper(self.root, float("-inf"))
        return good_nodes_list

    def is_bst(self) -> bool:
        def _helper(
            node: Optional[NumericTreeNode[NumericT]],
            min_val: NumericT,
            max_val: NumericT,
        ) -> bool:
            if not node:
                return True

            if node.val <= min_val or node.val >= max_val:
                return False

            return _helper(node.left, min_val, node.val) and _helper(
                node.right, node.val, max_val
            )

        return _helper(self.root, float("-inf"), float("inf"))

    def tilt_sum(self) -> NumericT:
        sum_ = 0

        def _helper(node: Optional[NumericTreeNode[NumericT]]) -> NumericT:
            nonlocal sum_
            if not node:
                return 0

            left_sum = _helper(node.left)
            right_sum = _helper(node.right)

            sum_ += abs(left_sum - right_sum)

            return left_sum + right_sum + node.val

        _helper(self.root)
        return sum_

    def longest_univalue_path(self) -> int:
        max_length = 0

        def _helper(node: Optional[NumericTreeNode[NumericT]]) -> int:
            nonlocal max_length
            if not node:
                return 0

            left_length = _helper(node.left)
            right_length = _helper(node.right)

            left_arrow = 0
            right_arrow = 0

            if node.left and node.left.val == node.val:
                left_arrow = left_length + 1

            if node.right and node.right.val == node.val:
                right_arrow = right_length + 1

            max_length = max(max_length, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)

        _helper(self.root)
        return max_length

    def level_order_sum(self) -> list[NumericT]:
        if not self.root:
            return []

        level_sum = []
        queue = deque([self.root])

        while queue:
            level_size = len(queue)
            current_level_sum = 0

            for _ in range(level_size):
                current_node = queue.popleft()
                current_level_sum += current_node.val

                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

            level_sum.append(current_level_sum)

        return level_sum
