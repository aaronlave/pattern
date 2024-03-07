rows = int(input("How long would you like the pattern to be? "))

for i in range(1, rows +1):

    number_of_stars = i if i <= (rows / 2) else rows - i +1

    print("*" * number_of_stars)