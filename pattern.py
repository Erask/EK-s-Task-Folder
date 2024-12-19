# Row input to design pattern
rows = int(input("Enter the number of rows: "))

# loop to create pattern
for i in range(1, 2 * rows):
    if i <= rows:
        #print top side 
        print('*' * i)
    else:
        #print bottom side
        print('*' * ((2* rows) - i))
