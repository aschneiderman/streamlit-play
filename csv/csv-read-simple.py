import csv
import os

current_directory = os.path.abspath(__file__)
print( "\n\n", current_directory)
core_data = "amounts.csv"

with open(current_directory + '/' + core_data, "r") as f:
    print("we did it!")

    reader = csv.reader(f)
    for i, line in enumerate(reader):
        print 'line[{}] = {}'.format(i, line)