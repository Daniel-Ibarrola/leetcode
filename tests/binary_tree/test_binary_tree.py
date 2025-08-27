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

    @pytest.mark.parametrize(
        "root, expected",
        [
            # Empty tree
            (None, 0),
            # Single node tree
            (TreeNode(1), 0),
            # Simple tree, diameter passes through root
            (TreeNode(1, left=TreeNode(2), right=TreeNode(3)), 2),
            # Skewed left tree
            (TreeNode(1, left=TreeNode(2, left=TreeNode(3))), 2),
            # Skewed right tree
            (TreeNode(1, right=TreeNode(2, right=TreeNode(3))), 2),
            # Complex tree where diameter passes through the root
            # Path: 4 -> 2 -> 1 -> 3
            (
                TreeNode(
                    1,
                    left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
                    right=TreeNode(3),
                ),
                3,
            ),
            # Complex tree where diameter is in the left subtree
            # Path: 7 -> 5 -> 3 -> 6 -> 8
            (
                TreeNode(
                    1,
                    left=TreeNode(
                        2,
                        right=TreeNode(
                            3,
                            left=TreeNode(5, left=TreeNode(7)),
                            right=TreeNode(6, right=TreeNode(8)),
                        ),
                    ),
                    right=TreeNode(4),
                ),
                5,
            ),
            # Another standard case
            (
                TreeNode(
                    4,
                    left=TreeNode(2, left=TreeNode(1), right=TreeNode(3)),
                    right=TreeNode(7, left=TreeNode(6)),
                ),
                4,
            ),
        ],
    )
    def test_diameter(self, root: TreeNode, expected: int):
        tree = BinaryTree(root)
        assert tree.diameter() == expected


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

    @pytest.mark.parametrize(
        "root, target_sum, expected",
        [
            # Empty tree, target is 0
            (None, 0, False),
            # Empty tree, target is non-zero
            (None, 5, False),
            # Single node, target matches
            (NumericTreeNode(5), 5, True),
            # Single node, target does not match
            (NumericTreeNode(5), 10, False),
            # Classic case: path exists
            (
                NumericTreeNode(
                    5,
                    left=NumericTreeNode(
                        4,
                        left=NumericTreeNode(
                            11, left=NumericTreeNode(7), right=NumericTreeNode(2)
                        ),
                    ),
                    right=NumericTreeNode(
                        8,
                        left=NumericTreeNode(13),
                        right=NumericTreeNode(4, right=NumericTreeNode(1)),
                    ),
                ),
                22,
                True,
            ),
            # Path with negative numbers
            (
                NumericTreeNode(
                    10, left=NumericTreeNode(-2), right=NumericTreeNode(-5)
                ),
                8,
                True,
            ),
            # Path with floats
            (
                NumericTreeNode(
                    1.5, left=NumericTreeNode(2.5), right=NumericTreeNode(3.5)
                ),
                4.0,
                True,
            ),
            # Path does not exist with floats
            (
                NumericTreeNode(
                    1.5, left=NumericTreeNode(2.5), right=NumericTreeNode(3.5)
                ),
                5.1,
                False,
            ),
            # Path sum is zero
            (NumericTreeNode(5, left=NumericTreeNode(-5)), 0, True),
        ],
    )
    def test_path_sum(
        self, root: NumericTreeNode[float], target_sum: float, expected: bool
    ):
        tree = NumericBinaryTree(root)
        assert tree.path_sum(target_sum) == expected

    @pytest.mark.parametrize(
        "root, expected",
        [
            # Empty tree
            (None, 0),
            # Single node
            (NumericTreeNode(5), 1),
            # Simple tree
            (NumericTreeNode(3, left=NumericTreeNode(1), right=NumericTreeNode(4)), 2),
            # Another simple tree
            (NumericTreeNode(3, left=NumericTreeNode(3), right=NumericTreeNode(1)), 2),
            # Complex tree
            (
                NumericTreeNode(
                    3,
                    left=NumericTreeNode(1, left=NumericTreeNode(3)),
                    right=NumericTreeNode(
                        4, left=NumericTreeNode(1), right=NumericTreeNode(5)
                    ),
                ),
                4,
            ),
            # All nodes are the same
            (NumericTreeNode(2, left=NumericTreeNode(2), right=NumericTreeNode(2)), 3),
            # Strictly decreasing path
            (NumericTreeNode(5, left=NumericTreeNode(4), right=NumericTreeNode(3)), 1),
            # Tree with negative numbers
            (
                NumericTreeNode(-1, left=NumericTreeNode(-2), right=NumericTreeNode(0)),
                2,
            ),
            # Tree with floats
            (
                NumericTreeNode(
                    2.5, left=NumericTreeNode(1.5), right=NumericTreeNode(3.5)
                ),
                2,
            ),
        ],
    )
    def test_num_good_nodes(self, root: NumericTreeNode[float], expected: int):
        tree = NumericBinaryTree(root)
        assert tree.num_good_nodes() == expected

    @pytest.mark.parametrize(
        "root, expected",
        [
            # Empty tree
            (None, []),
            # Single node
            (NumericTreeNode(5), [5]),
            # Simple tree
            (
                NumericTreeNode(3, left=NumericTreeNode(1), right=NumericTreeNode(4)),
                [3, 4],
            ),
            # Another simple tree
            (
                NumericTreeNode(3, left=NumericTreeNode(3), right=NumericTreeNode(1)),
                [3, 3],
            ),
            # Complex tree
            (
                NumericTreeNode(
                    3,
                    left=NumericTreeNode(1, left=NumericTreeNode(3)),
                    right=NumericTreeNode(
                        4, left=NumericTreeNode(1), right=NumericTreeNode(5)
                    ),
                ),
                [3, 3, 4, 5],
            ),
            # All nodes are the same
            (
                NumericTreeNode(2, left=NumericTreeNode(2), right=NumericTreeNode(2)),
                [2, 2, 2],
            ),
            # Strictly decreasing path
            (
                NumericTreeNode(5, left=NumericTreeNode(4), right=NumericTreeNode(3)),
                [5],
            ),
            # Tree with negative numbers
            (
                NumericTreeNode(-1, left=NumericTreeNode(-2), right=NumericTreeNode(0)),
                [-1, 0],
            ),
            # Tree with floats
            (
                NumericTreeNode(
                    2.5, left=NumericTreeNode(1.5), right=NumericTreeNode(3.5)
                ),
                [2.5, 3.5],
            ),
        ],
    )
    def test_good_nodes(self, root: NumericTreeNode[float], expected: list[float]):
        tree = NumericBinaryTree(root)
        assert sorted(tree.good_nodes()) == sorted(expected)

    @pytest.mark.parametrize(
        "root, expected",
        [
            # An empty tree is a valid BST
            (None, True),
            # A single node is a valid BST
            (NumericTreeNode(10), True),
            # A valid, simple BST
            (
                NumericTreeNode(10, left=NumericTreeNode(5), right=NumericTreeNode(15)),
                True,
            ),
            # A more complex, valid BST
            (
                NumericTreeNode(
                    10,
                    left=NumericTreeNode(
                        5, left=NumericTreeNode(2), right=NumericTreeNode(7)
                    ),
                    right=NumericTreeNode(
                        15, left=NumericTreeNode(12), right=NumericTreeNode(18)
                    ),
                ),
                True,
            ),
            # A valid right-skewed BST
            (
                NumericTreeNode(
                    10, right=NumericTreeNode(20, right=NumericTreeNode(30))
                ),
                True,
            ),
            # A valid left-skewed BST
            (
                NumericTreeNode(30, left=NumericTreeNode(20, left=NumericTreeNode(10))),
                True,
            ),
            # Invalid BST: Left child's value is greater than the root's
            (
                NumericTreeNode(
                    10, left=NumericTreeNode(20), right=NumericTreeNode(30)
                ),
                False,
            ),
            # Invalid BST: Right child's value is less than the root's
            (
                NumericTreeNode(
                    20, left=NumericTreeNode(10), right=NumericTreeNode(15)
                ),
                False,
            ),
            # Invalid BST: A node in the right subtree is smaller than the root
            (
                NumericTreeNode(
                    20,
                    left=NumericTreeNode(10),
                    right=NumericTreeNode(30, left=NumericTreeNode(15)),
                ),
                False,
            ),
            # Invalid BST: A node in the left subtree is larger than the root
            (
                NumericTreeNode(
                    20,
                    left=NumericTreeNode(10, right=NumericTreeNode(25)),
                    right=NumericTreeNode(30),
                ),
                False,
            ),
            # Invalid BST: Duplicate value (assuming strict inequality)
            (
                NumericTreeNode(
                    10, left=NumericTreeNode(10), right=NumericTreeNode(20)
                ),
                False,
            ),
            # Invalid BST with floats
            (
                NumericTreeNode(
                    10.0,
                    left=NumericTreeNode(5.5),
                    right=NumericTreeNode(15.5, left=NumericTreeNode(9.9)),
                ),
                False,
            ),
            # Valid BST with negative numbers
            (
                NumericTreeNode(
                    -10, left=NumericTreeNode(-20), right=NumericTreeNode(-5)
                ),
                True,
            ),
        ],
    )
    def test_is_bst(self, root: NumericTreeNode[float], expected: bool):
        tree = NumericBinaryTree(root)
        assert tree.is_bst() == expected

    @pytest.mark.parametrize(
        "root, expected",
        [
            # An empty tree has a tilt sum of 0
            (None, 0),
            # A single node tree has a tilt of 0
            (NumericTreeNode(10), 0),
            # Simple tree with only a left child
            # Tilt of 5 is 0. Tilt of 10 is |5 - 0| = 5. Total = 5.
            (NumericTreeNode(10, left=NumericTreeNode(5)), 5),
            # Simple tree with only a right child
            # Tilt of 15 is 0. Tilt of 10 is |0 - 15| = 15. Total = 15.
            (NumericTreeNode(10, right=NumericTreeNode(15)), 15),
            # Symmetric tree
            # Tilt of 5 is 0. Tilt of 15 is 0. Tilt of 10 is |5 - 15| = 10. Total = 10.
            (
                NumericTreeNode(10, left=NumericTreeNode(5), right=NumericTreeNode(15)),
                10,
            ),
            # A more complex tree
            # Tilt(3)=0, Tilt(5)=0, Tilt(7)=0
            # Tilt(2)=|3-5|=2
            # Tilt(9)=|0-7|=7
            # Tilt(4)=|(2+3+5)-(9+7)| = |10-16|=6
            # Total=0+0+0+2+7+6=15
            (
                NumericTreeNode(
                    4,
                    left=NumericTreeNode(
                        2, left=NumericTreeNode(3), right=NumericTreeNode(5)
                    ),
                    right=NumericTreeNode(9, right=NumericTreeNode(7)),
                ),
                15,
            ),
            # Another complex tree from a common example
            # Tilt(2)=0, Tilt(3)=0, Tilt(5)=0, Tilt(7)=0
            # Tilt(4)=|2-3|=1, Tilt(6)=|5-7|=2
            # Tilt(1)=|(4+2+3)-(6+5+7)| = |9-18|=9
            # Total=0+0+0+0+1+2+9=12
            (
                NumericTreeNode(
                    1,
                    left=NumericTreeNode(
                        4, left=NumericTreeNode(2), right=NumericTreeNode(3)
                    ),
                    right=NumericTreeNode(
                        6, left=NumericTreeNode(5), right=NumericTreeNode(7)
                    ),
                ),
                12,
            ),
            # Tree with negative values
            # Tilt(-5)=0, Tilt(5)=0
            # Tilt(0)=|-5 - 5|=10
            # Total=10
            (
                NumericTreeNode(0, left=NumericTreeNode(-5), right=NumericTreeNode(5)),
                10,
            ),
            # Tree with floats
            # Tilt(1.5)=0, Tilt(3.0)=0
            # Tilt(2.5)=|1.5-3.0|=1.5
            # Total=1.5
            (
                NumericTreeNode(
                    2.5, left=NumericTreeNode(1.5), right=NumericTreeNode(3.0)
                ),
                1.5,
            ),
        ],
    )
    def test_tilt_sum(self, root: NumericTreeNode[float], expected: float):
        tree = NumericBinaryTree(root)
        assert tree.tilt_sum() == expected
