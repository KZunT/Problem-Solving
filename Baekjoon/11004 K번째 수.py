N, K = map(int, input().split())
s = list(map(int, input().split()))
s.sort()

print(s[K - 1])