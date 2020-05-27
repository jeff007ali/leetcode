import collections

def possibleBipartition(N, dislikes):
    graph = collections.defaultdict(list)
    for u, v in dislikes:
        graph[u].append(v)
        graph[v].append(u)

    # print("Graph: {}".format(graph))

    color = {}
    def dfs(node, c = 0):
        # print("node: {} and color: {} and c: {}".format(node, color, c))
        if node in color:
            return color[node] == c
        color[node] = c
        return all(dfs(nei, c ^ 1) for nei in graph[node])             

    return all(dfs(node)
                for node in range(1, N+1)
                if node not in color)



print(possibleBipartition(4, [[1,2],[1,3],[2,4]]))
print(possibleBipartition(3, [[1,2],[1,3],[2,3]]))
print(possibleBipartition(5, [[1,2],[2,3],[3,4],[4,5],[1,5]]))