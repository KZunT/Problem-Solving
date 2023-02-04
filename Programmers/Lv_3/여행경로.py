# from collections import deque

# def solution(tickets):
#     answer = ['ICN']
#     tickets.sort(key = lambda x: x[1] , reverse = True)

#     queue = deque()

#     #print(tickets)

#     visited = [False for _ in range(len(tickets))]

#     for i in range(len(tickets)):
#         if tickets[i][0] == 'ICN':
#             queue.append(tickets[i])
#             visited[i] = True
#             #print(tickets[i])
#             break


#     while queue:
#         start, arrive = queue.popleft()
#         answer.append(arrive)
#         for i in range(len(tickets)):
#             if tickets[i][0] == arrive and visited[i] == False:
#                 #print(tickets[i])
#                 queue.append(tickets[i])
#                 visited[i] = True
#                 #break

#     return answer

## dfs가 유리하다..
def solution(tickets):
    graph = {i[0]: [] for i in tickets}
    for i in tickets:
        graph[i[0]].append(i[1])

    for i in graph.keys():
        graph[i].sort(reverse=True)

    result = []
    stack = ["ICN"]
    while stack:
        top = stack[-1]

        if top not in graph or len(graph[top]) == 0:
            result.append(stack.pop())
        else:
            stack.append(graph[top].pop())

    result.reverse()
    return result
