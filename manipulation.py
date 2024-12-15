# Requesting a sentence input
str_manip = input("Please enter a sentence: ")
print("You entered:", str_manip )

# Calculating the length of the input sentence
length_str = len(str_manip)
print("Your sentence string length is:", length_str)

# Accessing the last letter in the input sentence and replacing it with @ symbol
str_manip = str_manip[:-1] + '@'
print("Edited sentence:", str_manip)

# Outputing last three characters backwards 
backwards_str = str_manip[-1:-4:-1]
print("Last three characters backwards:", backwards_str)

# Slicing a new five letter word from the input sentence
new_slice = str_manip[:3] + str_manip[-2:]
print(new_slice)

