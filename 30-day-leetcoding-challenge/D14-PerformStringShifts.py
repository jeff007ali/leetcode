def stringShift(s, shift):
    for sh in shift:
        direction = sh[0]
        amount = sh[1]

        if direction == 0:
            s = s[amount:] + s[:amount]
        else:
            s = s[-amount:] + s[:-amount]

    return s


print(stringShift("abcdefg", [[1,1],[1,1],[0,2],[1,3]]))