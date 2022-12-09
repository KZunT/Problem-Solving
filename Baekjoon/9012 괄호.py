N = int(input())

for i in range(N):
    stack = []
    order = input()

    for j in order:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else:  # 스택에 괄호가 없을경우 NO
                print("NO")
                break
    else:  # for else 문 사용, break 에 걸리지 않았을 때
        if not stack:  # break문으로 안끊기고 스택이 비어있다면 괄호가 다 맞는거다.
            print("YES")
        else:  # break안 걸렸더라도 스택에 괄호가 들어있다면 NO이다.
            print("NO")
