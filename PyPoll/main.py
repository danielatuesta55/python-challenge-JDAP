# This is the python scrip I created to analyze the PyPoll data

# Part 1: Import modules 'OS' and 'CVS' - Dependencies
import os
import csv

#Part 2: Creting file path as well as file out out for my txt file at the end
csvpath = os.path.join('Resources', 'budget_data.csv')
output_file = os.path.join("analysis", "election_analysis.txt")
