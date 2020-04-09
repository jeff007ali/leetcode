def backspaceCompare(S, T):
        
    def typedString(text):
        res = ""
        for i in range(len(text)):
            if text[i] == "#":
                res = res[:-1]
            else:
                res += text[i]
        return res
    
    typedS = typedString(S)
    typedT = typedString(T)
    
    print(typedS)
    print(typedT)
    
    return typedS == typedT



def backspaceCompare1(S, T):

    def typedString(text):
        res = []
        for char in text:
            if res and char == '#':
                res.pop()
            elif char != '#':
                res.append(char)
        return res

    return typedString(S) == typedString(T)


# print(backspaceCompare1("ab#c", "ad#c"))
# print(backspaceCompare1("ab##", "c#d#"))
# print(backspaceCompare1("a##c", "#a#c"))
# print(backspaceCompare1("a#c", "b"))
print(backspaceCompare1("y#fo##f", "y#f#o##f"))

