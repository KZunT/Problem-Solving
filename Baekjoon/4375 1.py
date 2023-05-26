while True:
    try:
        N = int(input())
        answer = '1'
        while True:
            if int(answer) % N == 0:
                print(len(answer))
                break
            answer += '1'

    except EOFError:
        break
