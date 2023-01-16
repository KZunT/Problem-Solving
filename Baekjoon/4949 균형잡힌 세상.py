# while True:
#     string = input()
#     if string == '.':
#         break
#
#     word = list(string)
#
#     stack = []
#
#     blank = {')':'(',']':'['}
#
#     for w in word:
#         if w in [')',']','(','[']:
#             if w in ['(','[']:
#                 stack.append(w)
#             elif stack != []:
#                 if w in [')',']'] and stack[-1] == blank[w]:
#                     stack.pop()
#                 elif w in [')',']'] and stack[-1] != blank[w]:
#                     break
#
#     if stack == []:
#         print('yes')
#
#     else:
#         print('no')


while True:
    s = input()
    if s == '.':
        break
    stack = []
    temp = True
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] == '[':
                temp = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif i == ']':
            if not stack or stack[-1] == '(':
                temp = False
                break
            elif stack[-1] == '[':
                stack.pop()
    if temp == True and not stack:
        print('yes')
    else:
        print('no')