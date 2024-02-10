class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# ---------1----------
# -----2-------3------
# --4----5---6----7---    

def max_value(root):
    if not root:
        return 0
    return max(root.val, max_value(root.left), max_value(root.right))
    

print(max_value(root))