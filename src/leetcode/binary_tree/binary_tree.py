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

    def _max_depth_helper(self, node: Optional[TreeNode[T]]) -> int:
        if node is None:
            return 0

        left_depth = self._max_depth_helper(node.left)
        right_depth = self._max_depth_helper(node.right)

        return max(left_depth, right_depth) + 1

    def max_depth(self) -> int:
        return self._max_depth_helper(self.root)


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

    def _sum_helper(self, node: Optional[NumericTreeNode[NumericT]]) -> NumericT:
        if node is None:
            return 0

        left_sum = self._sum_helper(node.left)
        right_sum = self._sum_helper(node.right)

        return left_sum + right_sum + node.val

    def sum(self) -> NumericT:
        return self._sum_helper(self.root)

    def _max_helper(self, node: Optional[NumericTreeNode[NumericT]]) -> NumericT:
        if node is None:
            return float("-inf")

        left_max = self._max_helper(node.left)
        right_max = self._max_helper(node.right)

        return max(left_max, right_max, node.val)

    def max(self) -> Optional[NumericT]:
        """
        Finds the maximum value within the tree

        This method calculates the maximum value contained within the tree
        If the tree is empty, the result will be `None`.

        :return: The maximum value as an instance of the NumericT type if the
            tree contains elements, otherwise `None`.
        """
        max_ = self._max_helper(self.root)
        if max_ == float("-inf"):
            return None
        return max_

    def _path_sum_helper(
        self,
        node: Optional[NumericTreeNode[NumericT]],
        target_sum: NumericT,
    ) -> bool:
        if node is None:
            return False

        if not node.left and not node.right:
            return target_sum == node.val

        target_sum -= node.val
        return self._path_sum_helper(node.left, target_sum) or self._path_sum_helper(
            node.right, target_sum
        )

    def path_sum(self, target_sum: NumericT) -> bool:
        """Return true if the tree has a root-to-leaf path such that adding
            up all the values along the path equals target_sum.

        :param target_sum: the target sum
        :return: Whether the target sum is found in the tree
        """
        return self._path_sum_helper(self.root, target_sum)

    def _num_good_nodes_helper(
        self, node: Optional[NumericTreeNode[NumericT]], max_val: NumericT
    ) -> int:
        if node is None:
            return 0

        count = 0
        current_max = max_val
        if node.val >= max_val:
            count = 1
            current_max = node.val

        left_nodes = self._num_good_nodes_helper(node.left, current_max)
        right_nodes = self._num_good_nodes_helper(node.right, current_max)

        return left_nodes + right_nodes + count

    def num_good_nodes(self) -> int:
        return self._num_good_nodes_helper(self.root, float("-inf"))

    def _good_nodes_helper(
        self,
        node: Optional[NumericTreeNode[NumericT]],
        max_val: T,
        good_nodes: list[NumericT],
    ) -> None:
        if node is None:
            return

        current_max = max_val
        if node.val >= max_val:
            current_max = node.val
            good_nodes.append(node.val)

        self._good_nodes_helper(node.left, current_max, good_nodes)
        self._good_nodes_helper(node.right, current_max, good_nodes)

    def good_nodes(self) -> list[NumericT]:
        good_nodes: list[NumericT] = []
        self._good_nodes_helper(self.root, float("-inf"), good_nodes)
        return good_nodes
