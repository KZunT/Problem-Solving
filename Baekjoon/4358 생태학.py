import sys

input = sys.stdin.readline

tree = dict()

cnt = 0

while True:
    name = input().rstrip()
    if not name:
        break
    tree[name] = tree.get(name, 0) + 1
    cnt += 1

for key, value in sorted(tree.items()):
    ratio = value / cnt * 100
    print('%s %.4f' % (key, ratio))
