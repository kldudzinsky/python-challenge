#You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
    #The total number of votes cast
     # sum of rows
    # A complete list of candidates who received votes
        #loop for duplicates in Candidate column and print names 
    # The percentage of votes each candidate won

    # The total number of votes each candidate won
        
    # The winner of the election based on popular vote.
#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import os
import csv

Bank_csv = os.path.join("PyBank", "Resources", "Pypoll_Resources.csv")
#names of candidates
candidates = []
#list of number of votes for each candidate 
num_votes = []
#list of percentage of total votes each candidate gets 
percent_votes = []

total_votes = 0

csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    for row in csvreader
        total_votes += 1 

