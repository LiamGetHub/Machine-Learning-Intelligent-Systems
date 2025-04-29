# Implementing a Minimax tree using a Python dictionary

#          A
#        /   \
#       B     C
#      / \   / \
#    10   5 7   9
#

tree = {'A': ['B', 'C'], 'B': [10, 5], 'C': [7, 9]}

# The function __str()__ returns the preorder traversal of the tree as a string
# For example, the preorder traversal of the tree above is: A B 10 5 C 7 9


# The root of the tree and its children

root = list(tree)[0]

# The function get() returns a list with the values for a key

root_children = tree.get(root)

print ("The root node", root, "has children", root_children)

# The children of the root node

b = root_children[0]
c = root_children[1]

print ("The left child of A is", b)
print ("The right right child of A is", c)

if isinstance(b, int):
    print ("The left child of A is a leaf")
else:
    print ("The left child of A is an internal node")

# Leaf nodes represent the scores of a game

score = tree['B'][0]

# The function isinstance(node, int) returns true if a node is a leaf

if isinstance(score, int):
    print ("The left child of B is a leaf with score", score)


