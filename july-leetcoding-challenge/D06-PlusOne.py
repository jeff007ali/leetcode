def plusOne(digits):
    digits[-1] += 1
    for i in range(len(digits) - 1, 0, -1):
        if digits[i] != 10:
            break
        digits[i] = 0
        digits[i - 1] += 1

    if digits[0] == 10:
        digits[0] = 0
        return [1] + digits

    return digits

def plusOne1(digits):
    return map(int, str(int(''.join(map(str, digits))) + 1))

print(plusOne1([1,2,3]))
# print(plusOne1([4,3,2,1]))
# print(plusOne1([4,3,9,9]))
# print(plusOne1([9,9,9,9]))
