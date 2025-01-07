# Given two binary trees. The task is to write a program to check if the two trees
# are identical in structure.
# A binary tree node has data, pointer to left child
# and a pointer to right child
class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

# Helper function that allocates a new node with the
# given data and None left and right pointers.


def newNode(data):
    node = Node(data)
    return node

# Function to check if two trees have same
# structure


def isSameStructure(a, b):
    # 1. both empty
    if a is None and b is None:
        return 1

    # 2. both non-empty . compare them
    if a is not None and b is not None:
        return (isSameStructure(a.left, b.left) and isSameStructure(a.right, b.right))

    # 3. one empty, one not . false
    return 0


if __name__ == '__main__':
    root1 = newNode(10)
    root2 = newNode(100)
    root1.left = newNode(7)
    root1.right = newNode(15)
    root1.left.left = newNode(4)
    root1.left.right = newNode(9)
    root1.right.right = newNode(20)

    root2.left = newNode(70)
    root2.right = newNode(150)
    root2.left.left = newNode(40)
    root2.left.right = newNode(90)
    root2.right.right = newNode(200)

    if (isSameStructure(root1, root2)):
        print("Both trees have same structure")
    else:
        print("Trees do not have same structure")
