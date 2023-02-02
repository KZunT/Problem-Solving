def solution(routes):
    answer = 1

    routes.sort(key=lambda x: x[1])

    camera = routes[0][1]

    print(routes)

    for i in range(len(routes)):
        if routes[i][0] <= camera <= routes[i][1]:
            pass
        else:
            camera = routes[i][1]
            answer += 1
        print(camera)

    return answer