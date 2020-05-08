# The slope for a line through any 2 points (x0, y0) and (x1, y1) is (y1 - y0) / (x1 - x0); 
# Therefore, for any given 3 points (denote the 3rd point as (x, y)), if they are in a straight line, the slopes of the lines from the 3rd point to the 2nd point and the 2nd point to the 1st point must be equal:

# (y - y1) / (x - x1) = (y1 - y0) / (x1 - x0)

# In order to avoid being divided by 0, use multiplication form:

# (x1 - x0) * (y - y1) = (x - x1) * (y1 - y0)

# Now imagine connecting the 2nd points respectively with others one by one, Check if all of the slopes are equal.

def checkStraightLine(coordinates):
    (x1, y1), (x2, y2) = coordinates[:2]

    for x, y in coordinates:
        if (y2 - y1) * (x - x2) != (x2 - x1) * (y - y2):
            return False
    return True

print(checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
print(checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))
