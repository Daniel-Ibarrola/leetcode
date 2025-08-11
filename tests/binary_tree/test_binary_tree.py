import pytest
from leetcode.binary_tree.binary_tree import NumericTreeNode, NumericBinaryTree


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
                left=NumericTreeNode(2.5, NumericTreeNode(3.0), NumericTreeNode(4.5)),
                right=NumericTreeNode(0.5),
            ),
            12.0,
        ),
        # Mixed int and float
        (NumericTreeNode(1, left=NumericTreeNode(2.5), right=NumericTreeNode(3)), 6.5),
    ],
)
def test_numeric_binary_tree_sum(root, expected):
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
                right=NumericTreeNode(-10, NumericTreeNode(-1), NumericTreeNode(-6)),
            ),
            -1,
        ),
        # Tree with floats
        (
            NumericTreeNode(
                1.5,
                left=NumericTreeNode(2.5, NumericTreeNode(3.0), NumericTreeNode(4.5)),
                right=NumericTreeNode(0.5),
            ),
            4.5,
        ),
        # Mixed int and float
        (NumericTreeNode(1, left=NumericTreeNode(2.5), right=NumericTreeNode(3)), 3),
    ],
)
def test_numeric_binary_tree_max(root, expected):
    tree = NumericBinaryTree(root)
    assert tree.max() == expected
