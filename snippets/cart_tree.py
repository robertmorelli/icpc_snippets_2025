import random

class Treap:
    def __init__(self, key, ortho):
        self.key = key              # x / index
        self.priority = ortho       # value stored (max-heap here)
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

def insert(root, key, ortho):
    if not root:
        return Treap(key, ortho)
    if key < root.key:
        root.left = insert(root.left, key, ortho)
    else:
        root.right = insert(root.right, key, ortho)
    return treapify(root)

def delete(root, key):
    if not root:
        return None

    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        # found node
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        # both children: rotate higher-priority child up
        if root.left.priority > root.right.priority:
            root = rotate_right(root)
            root.right = delete(root.right, key)
        else:
            root = rotate_left(root)
            root.left = delete(root.left, key)

    return root

def range_search(root, L, R):
    """
    Return node with maximal priority whose key is in [L, R].

    Uses Cartesian-tree / RMQ invariant:
    - If [L, R] is left of root.key: go left.
    - If [L, R] is right of root.key: go right.
    - Else: root.key in [L, R] and root is the max in that range.
    """
    node = root
    while node:
        if L <= node.key <= R:
            return node
        if R < node.key:
            node = node.left
        elif L > node.key:
            node = node.right
    return None

def print_tree(node, indent=0):
    if node:
        print_tree(node.right, indent + 4)
        print(" " * indent + f"{node.key} (prio={node.priority})")
        print_tree(node.left, indent + 4)

if __name__ == "__main__":
    # Example: keys = indices, priority = value (max-heap RMQ)
    vals = [5, 1, 9, 3, 7, 2, 8]
    root = None
    for i, v in enumerate(vals):
        root = insert(root, i, v)

    print("Tree:")
    print_tree(root)

    L, R = 3, 5
    res = range_search(root, L, R)
    if res:
        print(f"\nRange [{L}, {R}] -> index {res.key}, value {res.priority}")
    else:
        print(f"\nRange [{L}, {R}] -> no result")
