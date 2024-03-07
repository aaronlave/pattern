rows = 9

for i in range(1, rows +1):

    number_of_stars = i if i <= 5 else rows - i +1

    print("*" * number_of_stars)