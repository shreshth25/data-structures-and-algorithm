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
s=[]
def sum_of_nodes(root, s):
    if root:
        sum_of_nodes(root.left, s)
        s.append(root.val)
        sum_of_nodes(root.right, s)


sum_of_nodes(root,s)
print(sum(s))