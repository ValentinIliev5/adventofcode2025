# with open(r'./day5/test_input_ranges.txt','r') as f:
with open(r'./day5/input_ranges.txt','r') as f:
    ranges = f.read().split('\n')

# with open(r'./day5/test_input_numbers.txt','r') as f:
with open(r'./day5/input_numbers.txt','r') as f:
    numbers = f.read().split('\n')

ranges = [(int(range_input.split('-')[0]),int(range_input.split('-')[1])) for range_input in ranges]
print(ranges)
fresh_products = 0
for number in numbers:
    for range_ in ranges:
        if int(number) >= range_[0] and int(number) <= range_[1]:
            print(number)
            fresh_products += 1
            break


print(fresh_products)