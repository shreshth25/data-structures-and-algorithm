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

def BottomView(root):
    q = []
    q.append(root)
    q1 = []
    q1.append(0)
    m = {}
    while len(q) > 0:
        res = q.pop(0)
        curr = q1.pop(0)

        if m.get(curr) is None:
            m[curr] = []
        m[curr].append(res.val)
        if res.left:
            q.append(res.left)
            q1.append(curr-1)
        if res.right:
            q.append(res.right)
            q1.append(curr+1)
    for i in sorted(m.items()):
        print(i[1][-1], end='-')


BottomView(root)