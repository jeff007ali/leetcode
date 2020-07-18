def findOrder(numCourses, prerequisites):
    inDegree = [0] * numCourses
    
    for i in range(len(prerequisites)):
        inDegree[prerequisites[i][0]] += 1

    stack = []
    for i in range(len(inDegree)):
        if inDegree[i] == 0:
            stack.append(i)

    count = 0
    order = []
    while stack:
        learned = stack.pop()
        order.append(learned)
        count += 1

        for i in range(len(prerequisites)):
            if prerequisites[i][1] == learned:
                inDegree[prerequisites[i][0]] -= 1

                if inDegree[prerequisites[i][0]] == 0:
                    stack.append(prerequisites[i][0])
    
    return order if count == numCourses else []

# this one is faster one
from collections import defaultdict  
def findOrder1(num, p):
    e = defaultdict(list)
    d = defaultdict(int)
    
    for b, a in p:
        e[a].append(b)
        d[b] += 1
    
    res = []
    for i in range(num):
        if not d[i]:
            res.append(i)
    
    for ele in res:
        for end in e[ele]:
            d[end] -= 1
            if not d[end]:
                res.append(end)
    
    return (res if len(res) == num else [])


print(findOrder(2, [[1,0]]))
print(findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))