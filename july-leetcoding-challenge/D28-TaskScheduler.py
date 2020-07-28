import collections
def leastInterval(tasks, n):
    task_counts = list(collections.Counter(tasks).values())
    print(task_counts)

    max_count = max(task_counts)
    print(max_count)

    max_count_tasks = task_counts.count(max_count)
    print(max_count_tasks)

    return max(len(tasks), (max_count - 1) * (n + 1) + max_count_tasks)


print(leastInterval(["A","A","A","B","B","B"], 2))
# print(leastInterval(["A","A","A","B","B","B"], 0))
# print(leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))