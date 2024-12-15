# program initiation with time input for each triathlon sport
swimming_time = float(input("Enter swimming time in minutes: "))
cycling_time = float(input("Enter cycling time in minutes: "))
running_time = float(input("Enter running time in minutes: "))

# Triathlon total time calculation
triathlon_time = sum([swimming_time, cycling_time, running_time])

# Award determination based on meeting the set time threshold 
if triathlon_time <= 100:
    award = "Honorary colours"
elif 105 <= triathlon_time:
    award = "Honorary half colours"
elif 110 <= triathlon_time:
    award = "Honorary scroll"
else:
    award = "No award"

# Display of the award based on triathlon time attained 
print(f"Triathlon time: {triathlon_time} minutes")
print(f"Award:{award}")






