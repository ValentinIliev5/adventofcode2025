with open(r".\aoc25\day2\input.txt",'r') as f:
# with open(r".\aoc25\day2\test_input.txt",'r') as f:
    ranges = f.read().split(',')

print(ranges)
invalid = 0
for id_range in ranges:
    ids = [int(item) for item in id_range.split('-')]
    print(ids)
    for i in range(ids[0],ids[1]+1):
        num = str(i)
        if num[:int(len(num)/2)]==num[int(len(num)/2):]:
            invalid+=int(num)

print(invalid)