# Same as - https://leetcode.com/problems/merge-intervals/
# just append newInterval and then same as merge intervals
# O(nlgn) time, logn because of sort
def insert(intervals, newInterval):

    intervals.append(newInterval)
    
    if not intervals:
        return []
    
    # sort with start
    intervals = sorted(intervals, key=lambda i:i[0])
    
    res = [intervals[0]]
    
    for interval in intervals[1:]:
        if interval[0] <= res[-1][1]:
            res[-1][1] = max(interval[1], res[-1][1])
        else:
            res.append(interval)
            
    return res

# O(n) time, Considering that the intervals are initially sorted 
# according to their start times
def insert1(intervals, newInterval):
    res = []
        
    for i, interval in enumerate(intervals):
        if interval[1]  < newInterval[0]:
            res.append(interval)
        elif newInterval[1] < interval[0]:
            res.append(newInterval)
            return res + intervals[i:] # newInterval is added we can return from here
        else: # overlap case
            newInterval[0] = min(newInterval[0], interval[0])
            newInterval[1] = max(newInterval[1], interval[1])
            
    res.append(newInterval)
    return res


print(insert([[1,3],[6,9]], [2,5]))
print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
print(insert([], [5,7]))
print(insert([[1,5]], [2,3]))
print(insert([[1,5]], [2,7]))