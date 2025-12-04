with open(r'./day4/test_input.txt','r') as f:
# with open(r'./day4/input.txt','r') as f:
    rows = f.read().split('\n')

def get_count_of_papers_around_spot(rows,i,j):
    count_of_papers_around = 0
    for k in range(-1,2):
        for l in range(-1,2):
            if not (k == 0 and l == 0):
                if i-k >=0 and j - l>= 0 and i-k < len(rows) and j-l < len(rows[1]) and rows[i-k][j-l]=='@':
                    count_of_papers_around +=1
    
    return count_of_papers_around

test_arr=[]
count = 0
for i in range(0,len(rows)):
    test_arr.append([])
    # print(rows[i])
    for j in range(0,len(rows[i])):
        count_of_papers = get_count_of_papers_around_spot(rows,i,j)
        if count_of_papers < 4 and rows[i][j] == '@':
            test_arr[i].append('x')
            count+=1
        else:
            test_arr[i].append(rows[i][j])
    
        
        
# print(test_arr)
# print(rows)
print()
print()
for row in test_arr:
    print(''.join(row))
print(count)