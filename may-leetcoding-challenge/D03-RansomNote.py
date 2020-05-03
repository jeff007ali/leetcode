def canConstruct(ransomNote, magazine):
        for c in set(ransomNote):
            if ransomNote.count(c) > magazine.count(c):
                return False
        
        return True

print(canConstruct("a", "b"))
print(canConstruct("aa", "ab"))
print(canConstruct("aa", "aab"))