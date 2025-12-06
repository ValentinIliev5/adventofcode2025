# UNSOLVED
# with open(r'./day5/test_input_ranges.txt','r') as f:
with open(r'./day5/input_ranges.txt','r') as f:
    ranges = f.read().split('\n')


ranges = [(int(range_input.split('-')[0]),int(range_input.split('-')[1])) for range_input in ranges]
ranges = sorted(ranges,key=lambda x: (x[0], x[1]))
for range_ in ranges:
    print(range_[0],len(str(range_[0])),range_[1],len(str(range_[1])))
merged_ranges = [ranges[0]]
for range_ in ranges[1:]:
    if range_[0] <= merged_ranges[-1][1]:
        merged_ranges[-1] = (merged_ranges[-1][0], range_[1])
    else:
        merged_ranges.append(range_)
print()
for range_ in merged_ranges:
    print(range_[0],len(str(range_[0])),range_[1],len(str(range_[1])))

fresh_products = 0
for m_range in merged_ranges:
    fresh_products += (m_range[1] - (m_range[0]-1))

print(fresh_products)