# Iterative method
def addDigits(num):
    digital_root = 0
    while num > 0:
        digital_root += num % 10
        num //= 10

        if num == 0 and digital_root > 9:
            num = digital_root
            digital_root = 0
    
    return digital_root

# Recursive method
def addDigits1(num):
    if num < 9:
        return num

    digital_root = 0
    while num > 0:
        digital_root += num % 10
        num //= 10

    return addDigits1(digital_root)

# Mathematics solution
def addDigits2(num):
    if num == 0:
        return 0
    elif num % 9 == 0:
        return 9
    else:
        return num % 9

# one liner solution for addDigits2
def addDigits3(num):
    return (num % 9 or 9) if num else 0

# If we combine last 2 cases of mathematics solution
def addDigits4(num):
    if num == 0:
        return 0
    else:
        return 1 + (num - 1) % 9

# One liner solution for addDigits4
def addDigits5(num):
    return 1 + (num - 1) % 9 if num else 0
     

print(addDigits5(38))