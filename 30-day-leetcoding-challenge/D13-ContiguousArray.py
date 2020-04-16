def findMaxLength(nums):     
    count = 0
    max_length=0
    table = {0: 0}
    for index, num in enumerate(nums, 1):
        if num == 0:
            count -= 1
        else:
            count += 1
        
        if count in table:
            max_length = max(max_length, index - table[count])
        else:
            table[count] = index

        # print(table)
        # print(max_length)
    
    return max_length
        
        

print(findMaxLength([0,1]))
print(findMaxLength([0,1,0]))