s = [2, 5, 6, 10, 1, 3, 12, 4]
n = 1

def linear(s):
    for i in s:
        if i == n:
            return True
    return False

print(f"Element {n} is there in {s}", "found" if linear(s) else "not found")