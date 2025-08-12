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
        max_ = self._max_helper(self.root)
        if max_ == float("-inf"):
            return None
        return max_
