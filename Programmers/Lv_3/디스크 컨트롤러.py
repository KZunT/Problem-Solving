import heapq


def solution(jobs):
    answer, now, i = 0, 0, 0  # now 는 현재 시간
    start = -1
    heap = []

    while i < len(jobs):
        # 현재 시점에서 처리할 수 있는 작업을 heap에 저장
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])

        if len(heap) > 0:  # 처리할 작업이 있는 경우
            cur = heapq.heappop(heap)
            print(start, "작업가능시간", now)
            print("처리한작업", cur[0], cur[1])
            start = now
            now += cur[0]
            answer += now - cur[1]  # 작업 요청시간부터 종료시간까지의 시간 계산
            i += 1  # 처리한 작업 카운트
        else:  # 처리할 작업이 없는 경우 다음 시간을 넘어감
            now += 1

    return answer // len(jobs)