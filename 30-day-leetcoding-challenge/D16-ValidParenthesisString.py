def checkValidString(s):
    l = len(s)
    c = 0
    for i in range(l):
        if s[i] in "(*":
            c += 1
        else:
            c -= 1
            
        if c < 0:
            return False
    
    if c == 0:
        return True
    
    c = 0
    for i in reversed(range(l)):
        if s[i] in "*)":
            c += 1
        else:
            c -= 1
        
        if c < 0:
            return False
        
    return True

print(checkValidString('(*))'))