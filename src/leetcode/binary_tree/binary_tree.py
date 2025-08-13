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
