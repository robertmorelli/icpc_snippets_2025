import random

class Treap:
    def __init__(self, key):
        self.key = key
        self.priority = random.getrandbits(64)  # true random 64-bit priority
        self.left = None
        self.right = None

def rotate_left(p):
    r = p.right
    p.right = r.left
    r.left = p
    return r

def rotate_right(p):
    l = p.left
    p.left = l.right
    l.right = p
    return l

def insert(root, key):
    if not root:
        return Treap(key)
    if key < root.key:
        root.left = insert(root.left, key)
        if root.left.priority > root.priority:
            root = rotate_right(root)
    else:
        root.right = insert(root.right, key)
        if root.right.priority > root.priority:
            root = rotate_left(root)
    return root

def print_tree(Treap, indent=0):
    if Treap:
        print_tree(Treap.right, indent + 4)
        print(" " * indent + f"{Treap.key} (p={Treap.priority})")
        print_tree(Treap.left, indent + 4)

if __name__ == "__main__":
    random.seed(42)  # optional: deterministic output
    root = None
    vals = random.sample(range(100), 20)
    for v in vals:
        root = insert(root, v)
    print_tree(root)
