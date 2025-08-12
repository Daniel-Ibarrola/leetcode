import pytest
from leetcode.binary_tree.binary_tree import (
    NumericTreeNode,
    NumericBinaryTree,
    TreeNode,
    BinaryTree,
)


class TestBinaryTree:
    @pytest.mark.parametrize(
        "root, expected",
        [
            # Empty tree
            (None, 0),
            # Single node
            (TreeNode(1), 1),
            # Simple tree
            (TreeNode(1, left=TreeNode(2), right=TreeNode(3)), 2),
            # Skewed to the right
            (TreeNode(1, right=TreeNode(2, right=TreeNode(3))), 3),
            # Skewed to the left
            (
                TreeNode(1, left=TreeNode(2, left=TreeNode(3, left=TreeNode(4)))),
                4,
            ),
            # More complex tree
            (
                TreeNode(
                    3,
                    left=TreeNode(9),
                    right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)),
                ),
                3,
            ),
            # Unbalanced tree
            (
                TreeNode(
                    1,
                    left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
                    right=TreeNode(3, left=TreeNode(6)),
                ),
                3,
            ),
        ],
    )
    def test_max_depth(self, root: TreeNode, expected: int):
        tree = BinaryTree(root)
        assert tree.max_depth() == expected


class TestNumericBinaryTree:
    @pytest.mark.parametrize(
        "root, expected",
        [
            # Empty tree
            (None, 0),
            # Single node
            (NumericTreeNode(5), 5),
            # Only left child
            (NumericTreeNode(10, left=NumericTreeNode(5)), 15),
            # Only right child
            (NumericTreeNode(1, right=NumericTreeNode(9)), 10),
            # Full binary tree with positive integers
            (
                NumericTreeNode(
                    1,
                    left=NumericTreeNode(2, NumericTreeNode(4), NumericTreeNode(5)),
                    right=NumericTreeNode(3, NumericTreeNode(6), NumericTreeNode(7)),
                ),
                28,  # 1+2+3+4+5+6+7
            ),
            # Tree with negative values
            (
                NumericTreeNode(
                    -5,
                    left=NumericTreeNode(2, NumericTreeNode(-3), NumericTreeNode(4)),
                    right=NumericTreeNode(1, NumericTreeNode(0), NumericTreeNode(-2)),
                ),
                -3,  # sum of all values
            ),
            # Tree with floats
            (
                NumericTreeNode(
                    1.5,
                    left=NumericTreeNode(
                        2.5, NumericTreeNode(3.0), NumericTreeNode(4.5)
                    ),
                    right=NumericTreeNode(0.5),
                ),
                12.0,
            ),
            # Mixed int and float
            (
                NumericTreeNode(1, left=NumericTreeNode(2.5), right=NumericTreeNode(3)),
                6.5,
            ),
        ],
    )
    def test_numeric_binary_tree_sum(
        self, root: NumericTreeNode[float], expected: float
    ):
        tree = NumericBinaryTree(root)
        assert tree.sum() == expected

    @pytest.mark.parametrize(
        "root, expected",
        [
            # Empty tree
            (None, None),  # Assuming max() should return None for empty tree
            # Single node
            (NumericTreeNode(5), 5),
            # Only left child
            (NumericTreeNode(10, left=NumericTreeNode(5)), 10),
            # Only right child
            (NumericTreeNode(1, right=NumericTreeNode(9)), 9),
            # Full binary tree with positive integers
            (
                NumericTreeNode(
                    1,
                    left=NumericTreeNode(2, NumericTreeNode(4), NumericTreeNode(5)),
                    right=NumericTreeNode(3, NumericTreeNode(6), NumericTreeNode(7)),
                ),
                7,
            ),
            # Tree with negative values
            (
                NumericTreeNode(
                    -5,
                    left=NumericTreeNode(-2, NumericTreeNode(-3), NumericTreeNode(-4)),
                    right=NumericTreeNode(
                        -10, NumericTreeNode(-1), NumericTreeNode(-6)
                    ),
                ),
                -1,
            ),
            # Tree with floats
            (
                NumericTreeNode(
                    1.5,
                    left=NumericTreeNode(
                        2.5, NumericTreeNode(3.0), NumericTreeNode(4.5)
                    ),
                    right=NumericTreeNode(0.5),
                ),
                4.5,
            ),
            # Mixed int and float
            (
                NumericTreeNode(1, left=NumericTreeNode(2.5), right=NumericTreeNode(3)),
                3,
            ),
        ],
    )
    def test_numeric_binary_tree_max(
        self, root: NumericTreeNode[float], expected: float
    ):
        tree = NumericBinaryTree(root)
        assert tree.max() == expected
