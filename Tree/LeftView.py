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

def LeftView(root):
    q = []
    q.append(root)
    s = []
    while len(q) > 0:
        k = len(q)
        e = []
        for i in range(k):
            res = q.pop(0)
            e.append(res.val)
            if res.left:
                q.append(res.left)
            if res.right:
                q.append(res.right)
        s.append(e[0])
    print(s)

LeftView(root)