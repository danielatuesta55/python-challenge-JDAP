# This is the python scrip I created to analyze the PyPoll data

# Part 1: Import modules 'OS' and 'CVS' - Dependencies
import os
import csv

#Part 2: Creting file path as well as file out out for my txt file at the end
csvpath = os.path.join('Resources', 'budget_data.csv')
output_file = os.path.join("analysis", "election_analysis.txt")

#Part 3: Variable assigment for list dict and counters
TotalVotes = 0
CandidatePool = []
CandidateVotes = {}
#3.1: Winning candidate variable and counter for number of votes
Winner = ""
WinnerCount = 0

#Part 4: Read csv file and open it 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Part 5: I need it to read the header row
    header = next(csvreader)

    #Part 6: Create and iteration with for statement
    for row in csvreader:
        
        #Part 7: I need to add the values for the number of votes
        TotalVotes = TotalVotes + 1
        
        #Part 8: create new list from original that only outputs the candidate names
        NameCandidate = row[2]

        #Part 9: create an iteration with and if not in function to create new list candidate pool 
        if NameCandidate not in CandidatePool:
            #9.1 Create the list of candidates
            CandidatePool.append(NameCandidate)
           
            #9.2 keep track of the votes per candidate
            CandidateVotes[NameCandidate] = 0
       
    #Part 10: Add votes
     CandidateVotes[NameCandidate] = CandidateVotes[NameCandidate] + 1




