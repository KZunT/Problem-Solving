k = int(input())

rope_list = []

for i in range(k):
    rope_list.append(int(input()))

rope_list.sort(reverse=True)

for i in range(len(rope_list)):
    rope_list[i] = rope_list[i] * (i + 1) # 로프 * 연결된 로프 길이

print(max(rope_list)) # 그중 가장 큰 수가 정답

