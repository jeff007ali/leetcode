# Using topological sort
# 1. Calculate incoming arrow to every node(inDegree - list)
# 2. If any node is having ZERO incoming arrow, then add that node to stack
# 3. Iterate over stack until it's empty
# 4. In loop, pop last element from stack and remove every connection from that node and update inDegree(list)
# 5. After update, check if any node is having ZERO incoming arrow, then again add that node to stack
# 6. After every element pop, increase COUNT by one
# 7. Compare COUNT and num of courses
# Reference - https://www.youtube.com/watch?v=0LjVxtLnNOk

def canFinish(numCourses, prerequisites):
    inDegree = [0] * numCourses
    count = 0

    for i in range(len(prerequisites)):
        inDegree[prerequisites[i][0]] += 1

    stack = []

    for i in range(len(inDegree)):
        if inDegree[i] == 0:
            stack.append(i)
    
    while stack:
        learned = stack.pop()
        count += 1

        for i in range(len(prerequisites)):
            if prerequisites[i][1] == learned:
                inDegree[prerequisites[i][0]] -= 1

                if inDegree[prerequisites[i][0]] == 0:
                    stack.append(prerequisites[i][0])
    
    return count == numCourses


print(canFinish(2, [[1,0]]))
print(canFinish(2, [[1,0],[0,1]]))