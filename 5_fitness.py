activities = ['Dancing', 'Swimming', 'Biking']
durations = [10, 20, 15]


cal_burn = [duration * 3.5 for duration in durations]


total = sum(cal_burn)
print()
print("Total Calories Burned: ", total)