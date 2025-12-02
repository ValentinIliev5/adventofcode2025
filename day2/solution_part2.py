with open(r".\aoc25\day2\input.txt",'r') as f:
# with open(r".\aoc25\day2\test_input.txt",'r') as f:
    ranges = f.read().split(',')

print(ranges)
invalid = 0
for id_range in ranges:
    ids = [int(item) for item in id_range.split('-')]
    for i in range(ids[0],ids[1]+1):
        num = str(i)
        num_len = len(num)
        for chunk_size in range(1,int(num_len/2)+1):
            chunks = [num[j:j+chunk_size] for j in range(0,num_len,chunk_size)]
            is_invalid = True

            for chunk in chunks[1:]:
                if chunk!=chunks[0]:
                    is_invalid = False
            
            if is_invalid:

                print(num)
                invalid+=int(num)
                break

print(invalid)