# If you start to calculate cell combination then you will find that there are pattern in cell list.
# After some interval pattern is getting repeated.

# Store cell list as string in dictionary e.g., [0,1,0,1,1,0,0,1] (list) --> "01011001" (string)
# When you find same pattern in dictionary, you can find minimun value for N,
# Using this formula, N = N % size of pattern

# For example, there is string A B C D A B C D A B C D A B C D
#                                                        14
# now if you want to find what is the char at position 14?
# Then first calculate size of pattern, which is 4 in this case(A B C D)
# now use upper formula, N = N % size of pattern = 14 % 4 = 2
# so the result is character at 2nd position, which is B.

def prisonAfterNDays(cells, N):
    seen = {str(cells): N}
    while N:
        seen.setdefault(str(cells), N)
        N -= 1
        cells = [0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in range(1, 7)] + [0]
        if str(cells) in seen:
            N %= seen[str(cells)] - N
    return cells


print(prisonAfterNDays([0,1,0,1,1,0,0,1], 7))
print(prisonAfterNDays([1,0,0,1,0,0,1,0], 1000000000))