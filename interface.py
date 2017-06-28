from trackerscript import *

# input number you want to search
number = raw_input('Enter number to find\n')

# read csv, and split on "," the line
csv_file = csv.reader(open('output.csv', "rb"), delimiter=",")


# loop through csv list
for row in csv_file:
    # if current rows 2nd value is equal to input, print that row
    if number == row[2][4]:
        print row
