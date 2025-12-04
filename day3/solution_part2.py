# with open(r'./day3/test_input.txt','r') as f:
with open(r'./day3/input.txt','r') as f:
    battery_banks = f.read().split('\n')

def get_max_digit_between_indexes(bank,start_index,end_index):
    max_digit = 0
    index = -1
    for i in range(start_index,end_index+1):
        if int(bank[i]) > max_digit:
            max_digit = int(bank[i])
            index = i
    
    return str(max_digit), index


end_sum = 0
MAX_NUMBER_LEN = 12

for bank in battery_banks:
    max_digit , index = 0,-1
    max_num = ''
    for i in range(0,MAX_NUMBER_LEN):
        # print(bank,max_digit,index,len(bank)-(MAX_NUMBER_LEN - i))
        max_digit , index = get_max_digit_between_indexes(bank,index+1,len(bank)-(MAX_NUMBER_LEN - i))
        max_num += max_digit

    print(bank,max_num)
    end_sum += int(max_num)



print(end_sum)




    # for a in range(0,len(bank)):
    #     for b in range(a+1,len(bank)):
    #         for c in range(b+1,len(bank)):
    #             for d in range(c+1,len(bank)):
    #                 for e in range(d+1,len(bank)):
    #                     for f in range(e+1,len(bank)):
    #                         for g in range(f+1,len(bank)):
    #                             for h in range(g+1,len(bank)):
    #                                 for i in range(h+1,len(bank)):
    #                                     for j in range(i+1,len(bank)):
    #                                         for k in range(j+1,len(bank)):
    #                                             for l in range(k+1,len(bank)):
    #                                                 number = int(''.join(
    #                                                     [bank[a]
    #                                                      ,bank[b]
    #                                                      ,bank[c]
    #                                                      ,bank[d]
    #                                                      ,bank[e]
    #                                                      ,bank[f]
    #                                                      ,bank[g]
    #                                                      ,bank[h]
    #                                                      ,bank[i]
    #                                                      ,bank[j]
    #                                                      ,bank[k]
    #                                                      ,bank[l]
    #                                                      ]))
# Consider again the example from before:

# 987654321111111
# 811111111111119
# 234234234234278
# 818181911112111

# Now, the joltages are much larger:

#     In 987654321111111, the largest joltage can be found by turning on everything except some 1s at the end to produce 987654321111.
#     In the digit sequence 811111111111119, the largest joltage can be found by turning on everything except some 1s, producing 811111111119.
#     In 234234234234278, the largest joltage can be found by turning on everything except a 2 battery, a 3 battery, and another 2 battery near the start to produce 434234234278.
#     In 818181911112111, the joltage 888911112111 is produced by turning on everything except some 1s near the front.

# The total output joltage is now much larger: 987654321111 + 811111111119 + 434234234278 + 888911112111 = 3121910778619.