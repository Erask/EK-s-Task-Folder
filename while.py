# Define list variable 
sum_all_num = 0
num_count = 0

while True:
    #input request 
    num = float(input("Enter a number (-1 to exit): "))

    # Check if entry is -1 to break the loop
    if num == -1:
        break
    #check if entry is zero
    if num == 0:
        print("Zero is not valid number entry. Please input a valid number.")

        continue
    # increment all_num and num_count
    sum_all_num += num
    num_count += 1
    # Average calculation and output
    average = sum_all_num / num_count
    print(f"The average of valid entered numbers is: {average}")

else:
    print("No valid numbers were entered.")

