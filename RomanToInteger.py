def romanToInt(s):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    ans = 0

    for i in range(0, len(s) - 1):
        if roman[s[i]] < roman[s[i + 1]]:
            ans -= roman[s[i]]
        else:
            ans += roman[s[i]]

    return ans + roman[s[-1]]


def romanToInt1(s):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    s = s.replace("IV", "IIII").replace("IX", "VIIII")
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

    ans = 0

    for c in s:
        ans += roman[c]

    return ans


print(romanToInt1("III"))
print(romanToInt1("IV"))
print(romanToInt1("IX"))
print(romanToInt1("LVIII"))
print(romanToInt1("MCMXCIV"))