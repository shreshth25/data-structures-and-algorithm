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

def levelOrder(root):
    q = []
    q.append(root)

    while len(q) > 0:
        res = q.pop(0)
        print(res.val, end="->")
        if res.left:
            q.append(res.left)
        if res.right:
            q.append(res.right)
        

levelOrder(root)