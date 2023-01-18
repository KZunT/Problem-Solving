import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)  # 힙으로 만들어 준다.
    while scoville[0] < K:
        mix = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, mix)
        answer += 1

        if len(scoville) == 1 and scoville[0] < K:
            return -1

    return answer
