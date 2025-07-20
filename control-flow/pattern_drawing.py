# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer while loop to go through each row
while row < size:
    # Inner for loop to print stars in each column of the row
    for col in range(size):
        print("*", end="")  # print without new line
    print()  # move to the next line after each row
    row += 1  # go to the next row
