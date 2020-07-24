def allPathsSourceTarget(graph):
    def move(index, path):
        if index == len(graph) - 1: ans.append(path)
        for i in graph[index]: move(i, path + [i])
        return ans

    ans = []
    return move(0, [0])


# ref - https://www.youtube.com/watch?v=CYnvDzMprdc
def allPathsSourceTarget1(graph):
    paths = [[0]]
    ans = []

    while paths:
        path = paths.pop()
        for i in graph[path[-1]]:
            if i == len(graph) - 1:
                ans.append(path + [i])
            else:
                paths.append(path + [i])
    return ans
    

print(allPathsSourceTarget1([[1,2], [3], [3], []]))