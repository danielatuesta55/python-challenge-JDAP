## Python-challenge-JDAP

## Python Homework - Py Me Up, Charlie

### Intention of the Repository

This Repository has been made to summit the homework assignment for my Data Science Bootcamp at Northwestern University

Python

Student: Jorge Daniel Atuesta

March, 2021

---

### Inside of this repository

On this repository the reader will encounter my solution to the homework assignment Python. The repository is organized in folders and a README.md (The file you are currently reading). Here is the list of the folders and its contents so you can navigate through them.

1. Images: In this folder you will find the images for the instructions provided by the institution. You can skip this folder if you want.
2. PyBank: In this folder you will find all the solutions for the PyBank excercise. Insided the folder you will find two other folders: 1. Resources: This fodler contains the CSV files I used. 2. analysis: This folder holds my text file that has the results from my analysis.
3. Pypoll In this folder you will find all the solutions for the PyPoll excercise. Insided the folder you will find two other folders: 1. Resources: This fodler contains the CSV files I used. 2. analysis: This folder holds my text file that has the results from my analysis.

I hope you find my work to not only be complete but displaying all the knowledge learned throughout this portion of the Data Science Bootcamp at Northwestern University.

---

## PyBank Excercise

### Project's Aim

For this portion of the homework I had to create a Python script to analyze the financial records of my made-up company. The data was provided in a file called budget_data.csv (attached to the PyBank folder under resources).

#### Project's Challanges

The Python script I created accomplished the following tasks:

1. Calculate the total number of months included in the dataset
   * Total month's = 86
2. Calculate the net total amount of "Profit/Losses" over the entire peridod
   * Total amount of "Profit/Losses" = $38382578
3. Calculate the average of the changes in profits (date and amount) over the entire period
   * Average of the changes in profits =$-2315.12
4. Calculate the greatest increase in profits (date and amount) over the entire period
   * Greatest increase in profits = Feb-2012($1926159)
5. Calculate the greatest decrease in losses (date and amount) over the entire period
   * Greatest decrease in losses = Sep-2013($-2196167)

An additional challanged faced was to make sure that the Python script printed the analysis to the terminal and exported a text file with the results.

---

## PyPoll Excercise

### Project's Aim

For this task I was asked to picture myself helping a small, rural town modernize its vote counting process. In order to do this the file election_data.cvs was provided (you can take a look at this file under the folder PyPoll and then access the Resources folder).

#### Project's Challanges

The task at hand was to creat a Python script that analyzed the votes and calculates each of the following:

1. The total number of votes cast
   * Total number of votes =
2. A complete list of candidates who received votes
   * List of candidates that recevied votes =
3. The percentage of votes each candidate won
   * Percentage of votes per candidate =
4. The total number of votes each candidate won
   * Total number of votes per candidate =
5. The winner of the election based on popular vote.
   * Winner of election =

An additional challanged faced was to make sure that the Python script printed the analysis to the terminal and exported a text file with the results.

Here is the election results table:


---

## References

Fincher, J. (2019). Reading and Writing CSV Files in Python. Retrieved from Real Python: https://realpython.com/python-csv/#:~:text=Reading%20from%20a%20CSV%20file,which% 0does%20the%20heavy%20lifting.

**Please note: I am new to .md files and I cant seem to indent the reference following the APA guidelines**

## Assignment instructions provided by Northwestern Data Science Bootcamp

Python Homework - Py Me Up, Charlie

### Background

Well... you've made it!

It's time to put away the Excel sheet and join the big leagues. Welcome to the world of programming with Python. In this homework assignment, you'll be using the concepts you've learned to complete the **two** Python Challenges, PyBank and PyPoll.

Both of these challenges encompasses a real-world situation where your newfound Python scripting skills can come in handy. These challenges are far from easy so expect some hard work ahead!

#### Before You Begin

* Create a new repository for this project called `python-challenge`. **Do not add this homework to an existing repository**.
* Clone the new repository to your computer.
* Inside your local git repository, create a directory for both of the  Python Challenges. Use folder names corresponding to the challenges: **PyBank** and  **PyPoll**.
* Inside of each folder that you just created, add the following:

  * A new file called `main.py`. This will be the main script to run for each analysis.
  * A "Resources" folder that contains the CSV files you used. Make sure your script has the correct path to the CSV file.
  * An "analysis" folder that contains your text file that has the results from your analysis.
* Push the above changes to GitHub or GitLab.

### PyBank

![Revenue](Images/revenue-per-lead.png)

* In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)
* Your task is to create a Python script that analyzes the records to calculate each of the following:

  * The total number of months included in the dataset
  * The net total amount of "Profit/Losses" over the entire period
  * The average of the changes in "Profit/Losses" over the entire period
  * The greatest increase in profits (date and amount) over the entire period
  * The greatest decrease in losses (date and amount) over the entire period
* As an example, your analysis should look similar to the one below:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```
* In addition, your final script should both print the analysis to the terminal and export a text file with the results.

### PyPoll

![Vote Counting](Images/Vote_counting.png)

* In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
* You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

  * The total number of votes cast
  * A complete list of candidates who received votes
  * The percentage of votes each candidate won
  * The total number of votes each candidate won
  * The winner of the election based on popular vote.
* As an example, your analysis should look similar to the one below:

  ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```
* In addition, your final script should both print the analysis to the terminal and export a text file with the results.

### Hints and Considerations

* Consider what we've learned so far. To date, we've learned how to import modules like `csv`; to read and write files in various formats; to store contents in variables, lists, and dictionaries; to iterate through basic data structures; and to debug along the way. Using what we've learned, try to break down your tasks into discrete mini-objectives. This will be a _much_ better course of action than spending all your time looking for a solution on Stack Overflow.
* As you will discover, for some of these challenges, the datasets are quite large. This was done purposefully, as it showcases one of the limits of Excel-based analysis. While our first instinct, as data analysts, is often to head straight into Excel, creating scripts in Python can provide us with more robust options for handling "big data".
* Write one script for each dataset provided. Run your script separately to make sure that the code works for its respective dataset.
* Feel encouraged to work in groups, but don't shortchange yourself by copying someone else's work. You get what you put in, and the art of programming is extremely unforgiving to moochers. Dig your heels in, burn the night oil, and learn this while you can! These are skills that will pay dividends in your future career.
* Start early, and reach out for help often! Challenge yourself to identify _specific_ questions for your instructors and TAs. Don't resign yourself to simply saying, "I'm totally lost." If you need help, reach out because we're happy to help. But, come prepared and show us what you have done and your thought process.
* Always commit your work and back it up with GitHub pushes. You don't want to lose hours of your work because you didn't push it to GitHub every half hour or so.

  * Ensure your repository has regular commits (i.e. 20+ commits) and a thorough README.md file

### Copyright

Trilogy Education Services © 2019. All Rights Reserved.
