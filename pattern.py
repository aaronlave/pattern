# Create a program that outputs a pattern of stars
# The pattern should print each row adding 1 star until a certain point
# When the determined point is reached, the pattern will then reduce by 1 star per row.

# Create variable for number of rows in pattern
rows = 9

# For loop to iterate through rows to create pattern
for i in range(1, rows +1):
    # Determine number of stars in row of pattern to determine how to output
    number_of_stars = i if i <= 5 else rows - i +1
    # Output pattern
    print("*" * number_of_stars)