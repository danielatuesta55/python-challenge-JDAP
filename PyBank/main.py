# This is the python scrip I created to analyze the data

# Part 1: Import modules 'OS' and 'CVS' - Dependencies
import os
import csv

#Part 2: Creting file path as well as file out out for my txt file at the end
csvpath = os.path.join('Resources', 'budget_data.csv')
output_file = os.path.join("analysis", "budget_analysis.txt")

#Part 3: Creat parameters with variables such as lists and counters
TotalMonths = 0
MonthOfChange= []
NetChange = []
GreatestIncrease = ["",0]
GreatestDecrease = ["", 9999999999999] #avoids overflow
TotalNet = 0

#Part 4: Read csv file and open it 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Part 5: I need it to read the header row
    header = next(csvreader)

    #Part 6: Since I created NetChange I need to extract the first row so that it dosent append to it 
    first_row = next(csvreader)
    TotalMonths = TotalMonths + 1
    TotalNet = TotalNet + int(first_row[1])
    PreviouseNet = int(first_row[1])

    #Part 7: create my iteration with a for loop
    for row in csvreader:
       # print(row) to check if the file is reading
       #7.1 Extract the total months
       TotalMonths =   TotalMonths + 1
       TotalNet = TotalNet + int(row[1])

       #7.2 Extract the net change of the sample
       NetChangeValue = int(row[1]) - PreviouseNet
       PreviouseNet = int(row[1])
       NetChange = NetChange + [NetChangeValue]
       MonthOfChange = MonthOfChange + [row[0]]

       #7.3 Extracting the Greatest Increase by using a nested if
       if NetChangeValue> GreatestIncrease [1]:
           GreatestIncrease[0] = row[0]
           GreatestIncrease[1] = NetChangeValue
        #7.4 Extracting the Greatest decrease by using a nested if
       if NetChangeValue < GreatestDecrease[1]:
            GreatestDecrease[0] = row[0]
            GreatestDecrease [1] = NetChangeValue
    #Part 8: I need to calculate the average net change (AverageNetChange)
    MonthlyAverage = sum(NetChange)/ len(NetChange)

    #Part 9: Creating the output summary table 
    output = (
        f"\nFinancial Analysis\n"
        f"--------------------------\n"
        f"Total Months: {TotalMonths}\n"
        f"Total: ${TotalNet}\n"
        f"Average Change: ${MonthlyAverage:.2f}\n"
        f"Greatest Increase in Profits: {GreatestIncrease[0]}(${GreatestIncrease[1]})\n"
        f"Greatest Decrease in Profits: {GreatestDecrease[0]}(${GreatestDecrease[1]})\n")

    #Part 10: I need to print the out put to terminal
    print(output)

    #Part 11: I need to export the financial analysis to text file
    with open(output_file,"w") as txt_file:
        txt_file.write(output)








