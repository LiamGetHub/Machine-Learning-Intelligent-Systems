from minimaxtree import MinimaxTree

if __name__ == '__main__':
    # Minimax tree with alpha-beta pruning
    tree = MinimaxTree({'A': ['B', 'C'], 'B': [8, 6], 'C': [9, 2, 1]})

    print("Minimax tree", tree)

    (value, explored_leaves) = tree.minimax_max()
    print("The optimal value for Max player is", value, "after exploring leaves", explored_leaves)

    (value, explored_leaves) = tree.minimax_min()
    print("The optimal value for Min player is", value, "after exploring leaves", explored_leaves)

    # Additional test cases
    print("\nAdditional test cases:")

    # Test case 1: Deeper tree
tree1 = MinimaxTree({'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F', 'G'], 
                     'D': [7, 4], 'E': [5, 2], 'F': [9, 6], 'G': [8, 3]})
print("\nMinimax tree", tree1)
(value, explored_leaves) = tree1.minimax_max()
print("The optimal value for Max player is", value, "after exploring leaves", explored_leaves)
(value, explored_leaves) = tree1.minimax_min()
print("The optimal value for Min player is", value, "after exploring leaves", explored_leaves)

# Test case 2: Unbalanced tree
tree2 = MinimaxTree({'A': ['B', 'C', 'D'], 'B': [4], 'C': ['E', 'F'], 'D': [7, 5, 6], 
                     'E': [3, 1], 'F': [2]})
print("\nMinimax tree", tree2)
(value, explored_leaves) = tree2.minimax_max()
print("The optimal value for Max player is", value, "after exploring leaves", explored_leaves)
(value, explored_leaves) = tree2.minimax_min()
print("The optimal value for Min player is", value, "after exploring leaves", explored_leaves)
