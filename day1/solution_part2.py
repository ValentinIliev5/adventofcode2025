with open(r'./day1/input_part1.txt','r') as f:
# with open(r'./day1/test.txt','r') as f:
    commands = f.read().split('\n')

start = 50
times = 0
current = start
for command in commands:
    print(current,command)

    direction = command[0]
    moves = int(command[1:])
    number = moves*(-1 if direction=='L' else 1)
    prev = current
    current = current + number
    
    if current == 0:
        times += 1
    
    if current >= 100:
        times += int(current/100)
        current = current % 100

    if current < 0:
        if prev == 0:
            times += int((current*-1) / 100)
            current = current % 100

        else:
            times += (1 + int((current*-1) / 100))
            current = current % 100

    print(current,times)

print(times)