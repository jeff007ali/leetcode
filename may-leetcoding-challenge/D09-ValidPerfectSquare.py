def isPerfectSquare(num):
    if num < 2:
        return True
    
    left = 1
    right = num // 2
    
    while left <= right:
        mid = (left + right) // 2
        
        if mid * mid == num:
            return True
        elif mid * mid < num:
            left = mid + 1
        else:
            right = mid - 1
            
    return False

print(isPerfectSquare(16))
print(isPerfectSquare(14))