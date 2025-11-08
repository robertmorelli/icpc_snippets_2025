import random

class Treap:
    def __init__(self, key):
        self.key = key
        self.priority = random.getrandbits(64)
        self.left = self.right = None

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

def treapify(root):
    if root.left and root.left.priority > root.priority:
        return rotate_right(root)
    if root.right and root.right.priority > root.priority:
        return rotate_left(root)
    return root

def insert(root, key):
    if not root:
        return Treap(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return treapify(root)

def delete(root, key):
    if not root:
        return None

    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        # Found node to delete
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        # Both children exist: rotate the higher-priority child up
        if root.left.priority > root.right.priority:
            root = rotate_right(root)
            root.right = delete(root.right, key)
        else:
            root = rotate_left(root)
            root.left = delete(root.left, key)

    return root

def search(node, key):
    if not node or key == node.key:
        return node
    return search(node.left if key < node.key else node.right, key)

def print_tree(node, indent=0):
    if node:
        print_tree(node.right, indent + 4)
        print(" " * indent + f"{node.key} (p={node.priority})")
        print_tree(node.left, indent + 4)

if __name__ == "__main__":
    random.seed(42)
    vals = random.sample(range(100), 20)
    root = None
    for v in vals:
        root = insert(root, v)
    print("Initial tree:")
    print_tree(root)
    q = vals[5]
    print(f"\nSearching for {q}:")
    if found := search(root, q):
        print(f"Found {found.key} (p={found.priority})")
    else:
        print("Not found")
    print(f"\nDeleting {q}:")
    root = delete(root, q)
    print_tree(root)
