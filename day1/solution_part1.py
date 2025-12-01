with open(r'./day1/input_part1.txt','r') as f:
    commands = f.read().split('\n')

start = 50
times = 0
current = start
for command in commands:
    # print(current,command)
    direction = command[0]
    moves = int(command[1:])
    number = moves*(-1 if direction=='L' else 1)
    current = current + number
    while current < 0:
        current = 100 + current
    while current >= 100:
        current = current - 100
    # print(current)
    if current == 0:
        times +=1
        # break


print(times)