# 1. Let us find the place, where hour hand is. First, whe have 12 hours in total, for 360 degrees, that means 30 degrees per hour. Also, for every 60 minutes, our hour hand rotated by 1 hour, that is 30 degrees, so for every minute, it is rotated by 0.5 degrees. So, final place for hour hand is 30*hour + 0.5*minutes
# 2. Let us find the place, where minute hand is: every 60 minutes minute hand makes full rotation, that means we have 6 degrees for each minute.
# 3. Finally, we evaluate absolute difference between these two numbers, and if angle is more than 180 degrees, we return complementary angle.


def angleClock(hour, minutes):
    hour_deg = (360 / 12) * hour + (30 / 60) * minutes
    minute_deg = (360 / 60) * minutes

    angle = abs(hour_deg - minute_deg)
    
    if angle > 180:
        angle = 360 - angle

    return angle

    # Oneliner solution
    # return min(abs(30*hour-5.5*minutes),360-abs(30*hour-5.5*minutes))


print(angleClock(12, 30))
print(angleClock(3, 30))
print(angleClock(3, 15))
print(angleClock(4, 50))
print(angleClock(12, 0))