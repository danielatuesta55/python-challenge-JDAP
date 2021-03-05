# This is the python scrip I created to analyze the PyPoll data

# Part 1: Import modules 'OS' and 'CVS' - Dependencies
import os
import csv

#Part 2: Creting file path as well as file out out for my txt file at the end
csvpath = os.path.join('Resources', 'election_data.csv') #Asked classmate JD to take a look at why this portion of the code wasnt running, he debuged and found out I was spelling CVS not CSV.
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

#Part 11: I need to print the results from above in the terminal and wirte the txt file with the results
with open(output_file, "w") as txt_file:
    #11.1 total vote count to terminal
    ElectionResults = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes {TotalVotes}\n"
        f"-------------------------\n")
    print(ElectionResults, end="")

    #Part 12: Save current Election results onto txt file
    txt_file.write(ElectionResults)

    #Part 13: Create an iteration with a for loop to count total vote count per candidate
    for NameCandidate in CandidateVotes:
        votes = CandidateVotes.get(NameCandidate)
        PercentageOfVotes= float(votes) / float(TotalVotes) * 100
        
        #Part 14: Create an if statment to determine the winning number of votes and candidate
        if (votes > WinnerCount):
            WinnerCount = votes
            Winner = NameCandidate
        #Part 15: retrive candidates voter count and percentage to print in terminal
        OutputVoter = f"{NameCandidate}: {PercentageOfVotes:.3f}% ({votes})\n"
        print(OutputVoter, end ="")
        
        #Part 16: Upload the information to txt file
        txt_file.write(OutputVoter)

    #Part 17: I need to print the winner candidate into the terminal
    SummaryForWinner = ( 
        f"-------------------------\n"
        f"Winner: {Winner}\n"
        f"-------------------------\n")
    print(SummaryForWinner)

    #Part 18: Finish code by saving summary for winner in txt file
    txt_file.write(SummaryForWinner)






