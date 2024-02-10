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
s = []
def leaf_nodes(root):
    if root:
        if root.left == None and root.right == None:
            s.append(root.val)
        leaf_nodes(root.left)
        leaf_nodes(root.right)
    

leaf_nodes(root)
print(s)