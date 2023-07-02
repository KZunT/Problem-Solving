N = int(input())

name = [input() for _ in range(N)]

if sorted(name) == name:
    print("INCREASING")
elif sorted(name, reverse=True) == name:
    print("DECREASING")
else:
    print("NEITHER")
