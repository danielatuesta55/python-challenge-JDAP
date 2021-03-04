# This is the python scrip I created to analyze the data

# Part 1: Import modules 'OS' and 'CVS'
import os
import csv

    #using the open with, create the path
with open ('budget_data.cvs') as cvs_file:

    # Now that I have the file path I want to start cvs file handling
    # I am specifying the variable that holds the contents 
    cvs_reader = cvs.reader(cvs_file, delimiter = ',')
    #I need to direct python to read the header row first
    header = next(cvsreader)

# Part 2: I need to tackle the first challange count the number of months in column 'DATE'

    #Create a variable with the counter for the months and set it to 0
    monthCounter = 0
    # Create the empty list for months
    months = []


    # I need to create a for loop that reads in each row of data after the header and writes the data into assigned lists
    for row in cvs_reader:
        #Assing the column 'Date' that is index 0 as month
        month = row[0]
        #using the append function add a list to a new list in this case I am adding list month to months to be able to later on count the number of items in the list
        months.append(month)

    # now outside the for loop I am going to count how many items in the list with the len function
    monthCounter = len(months)
     # I want to print monthcounter and check if the loop did what I wanted
    print(monthCounter)
    

