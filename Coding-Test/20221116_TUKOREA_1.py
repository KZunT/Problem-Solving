N = int(input())
seat = input()

seat = seat.replace('S', '*S*')
seat = seat.replace('LL', '*LL*')
seat = seat.replace('**' , '*')

print(seat.count('*'))
