import sys

N = int(sys.stdin.readline().strip())
tree = {}

for n in range(N):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]

def preorder(root):
    if root != '.':
        print(root, end='')  # root
        preorder(tree[root][0])  # left
        preorder(tree[root][1])  # right
        return


def inorder(root):
    if root != '.':
        inorder(tree[root][0])  # left
        print(root, end='')  # root
        inorder(tree[root][1])  # right
        return

def postorder(root):
    if root != '.':
        postorder(tree[root][0])  # left
        postorder(tree[root][1])  # right
        print(root, end='')  # root
        return

preorder('A')
print()
inorder('A')
print()
postorder('A')
