def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False

    list1 = [0] * 26
    list2 = [0] * 26

    for i in range(len(s1)):
        list1[ord(s1[i]) - ord('a')] += 1

    for i in range(len(s2)):
        list2[ord(s2[i]) - ord('a')] += 1

        if i >= len(s1):
            list2[ord(s2[i - len(s1)]) - ord('a')] -= 1

        if list1 == list2:
            return True
 
    return False


print(checkInclusion("ab", "eidbaooo"))
print(checkInclusion("ab", "eidboaoo"))