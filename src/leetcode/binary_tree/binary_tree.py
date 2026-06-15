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

        node_queue = deque([self.root])
        result = []

        while node_queue:
            node = node_queue.popleft()
            result.append(node.val)
            if node.left:
                node_queue.append(node.left)
            if node.right:
                node_queue.append(node.right)

        return result

    def rightmost_node(self) -> list[T]:
        """
        Given the root of a binary tree, return the rightmost node at each level of the tree.
        The output should be a list containing only the values of those nodes.
        """
        if not self.root:
            return []

        right_nodes: list[T] = []
        node_queue = deque([self.root])

        while node_queue:
            level_size = len(node_queue)

            for ii in range(level_size):
                current_node = node_queue.popleft()

                if ii == level_size - 1:
                    right_nodes.append(current_node.val)

                if current_node.left:
                    node_queue.append(current_node.left)
                if current_node.right:
                    node_queue.append(current_node.right)

        return right_nodes

    def zigzag_traversal(self) -> list[list[T]]:
        """
        Given the root of a binary tree, return the zigzag level-order traversal of its nodes' values.
        The output should be a list of lists containing the values of the nodes at each level.
        The first list should contain the value of the root, the second list should contain the values of the
        nodes at the second level from right to left, the third list should contain the values of the
        third level from left to right, and so on.
        """
        if not self.root:
            return []

        traversal: list[T] = []
        node_queue = deque([self.root])

        go_right = True
        while node_queue:
            level_size = len(node_queue)
            current_level = []

            for ii in range(level_size):
                current_node = node_queue.popleft()

                if current_node.left:
                    node_queue.append(current_node.left)
                if current_node.right:
                    node_queue.append(current_node.right)

                current_level.append(current_node.val)

            if go_right:
                traversal.append(current_level)
            else:
                traversal.append(current_level[::-1])

            go_right = not go_right
        return traversal


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
        if self.root is None:
            return None

        def _helper(node: Optional[NumericTreeNode[NumericT]]) -> NumericT:
            if node is None:
                return float("-inf")

            return max(node.val, _helper(node.left), _helper(node.right))

        return _helper(self.root)

    def path_sum(self, target_sum: NumericT) -> bool:
        """Return true if the tree has a root-to-leaf path such that adding
        up all the values along the path equals target_sum.

        :param target_sum: the target sum
        :return: Whether the target sum is found in the tree
        """

        def _helper(
            node: Optional[NumericTreeNode[NumericT]], leftover: NumericT
        ) -> bool:
            if node is None:
                return False

            updated_leftover = leftover - node.val
            # Check leaf node
            if node.left is None and node.right is None:
                return updated_leftover == 0

            return _helper(node.left, updated_leftover) or _helper(
                node.right, updated_leftover
            )

        return _helper(self.root, target_sum)

    def path_sum_paths(self, target_sum: NumericT) -> list[list[NumericT]]:
        """Return a list of all root-to-leaf paths in the tree that sum to target_sum."""
        all_paths: list[list[NumericT]] = []

        def _helper(
            node: Optional[NumericTreeNode[NumericT]],
            leftover: NumericT,
            current_path: list[NumericT],
        ):
            if node is None:
                return

            updated_leftover = leftover - node.val
            current_path.append(node.val)

            if node.left is None and node.right is None and updated_leftover == 0:
                all_paths.append(current_path[:])

            _helper(node.left, updated_leftover, current_path)
            _helper(node.right, updated_leftover, current_path)

            current_path.pop()

        _helper(self.root, target_sum, [])
        return all_paths

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
        """
        Given the root of a binary tree, return the sum of the nodes at each level.
        The output should be a list containing the sum of the nodes at each level.
        """
        if not self.root:
            return []

        level_sums: list[NumericT] = []
        node_queue = deque([self.root])

        while node_queue:
            level_size = len(node_queue)
            level_sum = 0

            for _ in range(level_size):
                node = node_queue.popleft()
                level_sum += node.val

                if node.left:
                    node_queue.append(node.left)
                if node.right:
                    node_queue.append(node.right)

            level_sums.append(level_sum)

        return level_sums
