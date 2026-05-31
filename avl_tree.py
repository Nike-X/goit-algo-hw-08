# In this script, we prepare functions to find 
# minimal value and total value for all nodes of AVL-tree

# Use existing implementation of AVL-tree from learning materials
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

    def __str__(self, level=0, prefix="Root: "):
        ret = "\\t" * level + prefix + str(self.key) + "\\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def get_height(node):
    if not node:
        return 0
    return node.height

def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def left_rotate(z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y

def right_rotate(y):
    x = y.left
    T3 = x.right

    x.right = y
    y.left = T3

    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x

def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def insert(root, key):
    if not root:
        return AVLNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    if balance > 1:
        if key < root.left.key:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    if balance < -1:
        if key > root.right.key:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root

def delete_node(root, key):
    if not root:
        return root

    if key < root.key:
        root.left = delete_node(root.left, key)
    elif key > root.key:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = min_value_node(root.right)
        root.key = temp.key
        root.right = delete_node(root.right, temp.key)

    if root is None:
        return root

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    if balance > 1:
        if get_balance(root.left) >= 0:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    if balance < -1:
        if get_balance(root.right) <= 0:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root

# End of AVL-tree implementation

# This function searches for minimal value in the tree
# To find minimal value, we should always go to the left 
# subtree until it ends. The last node contains tree's minimal value
# This conclusion follows directly from the definition of BST 
# (and AVL-tree as a subtype of BST) itself:
# All keys in the left subtree always lesser then current key
def find_min_value(root):
    # Check if root exists
    if root is None:
        return None
    
    current = root

    # Go to the left until left subtree ends
    while current.left is not None:
        current = current.left

    # Return node value
    return current.key

# Function to find total sum of all nodes
def sum_tree_values(root):
    # Check if root exists
    if root is None:
        return 0
    
    # Recursively calculate sum of left and right subtrees
    return root.key + sum_tree_values(root.left) + sum_tree_values(root.right)

# Creates a new tree and prints out minimal value and total sum
def main():
    # Create a new tree
    root = None
    keys = [10, 20, 30, 25, 28, 27, -1]

    for key in keys:
        root = insert(root, key)
    
    print("AVL-Tree:")
    print(root)

    # Find and print minimal value
    print("Minimal value: ", find_min_value(root))

    # Calculate and print tree sum
    print("Sum of all values: ", sum_tree_values(root))

# This code executes main() function if script is launched from command line
if __name__ == "__main__":
    main()