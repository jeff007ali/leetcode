def removeKdigits(num, k):
    stack = []
    for n in num:
        while k and stack and stack[-1] > n:
            stack.pop()
            k -= 1
        stack.append(n)
    
    return ''.join(stack[:-k or None]).lstrip("0") or "0"

print(removeKdigits("1432219", 3))
print(removeKdigits("10200", 1))
print(removeKdigits("10", 2))