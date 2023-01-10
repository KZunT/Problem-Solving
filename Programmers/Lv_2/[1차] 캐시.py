from collections import deque


# def solution(cacheSize, cities):
#     answer = 0

#     cache = []

#     if cacheSize == 0:  # 캐시가 없는경우 예외처리
#         return len(cities) * 5

#     for i in range(len(cities)):
#         cities[i] = cities[i].lower()

#     for city in cities:
#         if len(cache) == 0: # 캐시에 아무것도 없으면 miss
#             cache.append(city)
#             answer += 5
#         else:
#             if len(cache) < cacheSize: # 캐시의 자리가 남아있을때
#                 if city in cache:   # hit 하면 도시 순서만 교체
#                     cache.append(cache.pop(cache.index(city)))
#                     answer += 1
#                 else:   # miss면 도시만 추가
#                     cache.append(city)
#                     answer += 5
#             else: # 캐시의 자리가 없을때
#                 if city in cache:   # hit하면 도시 순서를 교체
#                     cache.append(cache.pop(cache.index(city)))
#                     answer += 1
#                 else:  # miss면 처음 도시를 빼고 새로 페이지 추가
#                     cache.pop(0)
#                     cache.append(city)
#                     answer += 5
#     return answer

# 깔끔한 코드 추가..

def solution(cacheSize, cities):
    cache = deque(maxlen=cacheSize)  # 덱의 최대 크기를 설정 가능. 초과하게 된다면 큐 처럼 맨 앞 원소가 제거되소 맨 뒤에 새로운값이 추가됨
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time