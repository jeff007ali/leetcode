# Fastest solution - Using Deque
from collections import deque
def minDistance(word1, word2):
    visited = set()
    q = deque([(word1, word2, 0)])
    
    while q:
        w1, w2, dist = q.popleft()
        
        if (w1, w2) not in visited:
            visited.add((w1, w2))

            if w1 == w2:
                return dist

            while w1 and w2 and w1[0] == w2[0]:
                w1 = w1[1:]
                w2 = w2[1:]

            dist += 1
            q.extend([(
                w1[1:], w2[1:], dist), 
                (w1, w2[1:], dist), 
                (w1[1:], w2, dist)])


# Reference link - https://leetcode.com/problems/edit-distance/discuss/159295/Python-solutions-and-intuition
# Recusion method
def minDistance1(word1, word2):
    if not word1 and not word2:
        return 0
    if not word1:
        return len(word2)
    if not word2:
        return len(word1)
    if word1[0] == word2[0]:
        return minDistance1(word1[1:], word2[1:])
    insert = 1 + minDistance1(word1, word2[1:])
    delete = 1 + minDistance1(word1[1:], word2)
    replace = 1 + minDistance1(word1[1:], word2[1:])
    return min(insert, replace, delete)


# Dynamic programming solution
def minDistance2(word1, word2):
    m = len(word1)
    n = len(word2)
    table = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        table[i][0] = i
    for j in range(n + 1):
        table[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                table[i][j] = table[i - 1][j - 1]
            else:
                table[i][j] = 1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])
    return table[-1][-1]


print(minDistance2("horse", "ros"))
print(minDistance2("intention", "execution"))