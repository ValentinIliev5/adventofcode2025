# with open(r'./day3/test_input.txt','r') as f:
with open(r'./day3/input.txt','r') as f:
    battery_banks = f.read().split('\n')

end_sum = 0
for bank in battery_banks:
    max_num = 0
    for i in range(0,len(bank)):
        for j in range(i+1,len(bank)):
            number = int(''.join([bank[i],bank[j]]))
            if number > max_num:
                max_num = number
    end_sum+=max_num


print(end_sum)
