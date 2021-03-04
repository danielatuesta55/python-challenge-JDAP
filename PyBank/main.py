# This is the python scrip I created to analyze the data

# Part 1: Import modules 'OS' and 'CVS'
import os
import csv

csv_path = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    for row in csv_reader:
        print(row)



