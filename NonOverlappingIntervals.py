# Same as - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
# Same as - https://leetcode.com/problems/merge-intervals/

def eraseOverlapIntervals(intervals):
    # sort with end
    intervals = sorted(intervals, key=lambda i:i[1])
    
    res = 0
    end = -float('inf')
    
    for interval in intervals:
        if interval[0] >= end:
            res += 1
            end = interval[1]
            
    return len(intervals) - res

def eraseOverlapIntervals1(intervals):
    # sort with end
    intervals = sorted(intervals, key=lambda i:i[1])
    
    res = 0
    end = -float('inf')
    
    for interval in intervals:
        if interval[0] >= end:
            end = interval[1]
        else:
            res += 1
            
    return res

print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(eraseOverlapIntervals([[1,2],[2,3]]))