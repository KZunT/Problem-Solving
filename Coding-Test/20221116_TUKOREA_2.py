N = int(input())

p1 = []
p2 = []

for _ in range(N):
    first, second = map(int, input().split(' '))
    p1.append(first)
    p2.append(second)

max_lead = 0
lead_p = 0
p1_sum = 0
p2_sum = 0

for f, s in zip(p1, p2):

    p1_sum += f
    p2_sum += s

    lead = abs(p1_sum - p2_sum)

    if f > s and lead > max_lead:
        max_lead = lead
        lead_p = 1

    if f < s and lead > max_lead:
        max_lead = lead
        lead_p = 2

print(lead_p, max_lead)
