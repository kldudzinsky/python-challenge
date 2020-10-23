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

PyPoll_csv = os.path.join("PyPoll", "Resources", "Pypoll_Resources.csv")
#names of candidates
candidate_unique=[]
#list of number of votes for each candidate 
candidate_num_votes = []
#list of percentage of total votes each candidate gets 
percent_votes = []

total_votes = 0

with open(PyPoll_csv) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    for row in csvreader:
    #add to total votes
        total_votes += 1 
    #read names from row 2 of csv file
        candidate_in = (row[2])
    #create list of candidates who recieved votes
    #if candidate is in list then locate the candidate by index # & add vote 
        if candidate_in in candidate_unique:
            candidate_index = candidate_unique.index(candidate_in)
            candidate_num_votes[candidate_index] = candidate_num_votes[candidate_index] + 1
        else:
            #if candidate not in candidates_unique list then append to list & add vote
            candidate_unique.append(candidate_in)
            candidate_num_votes.append(1)
            #check if working 
            # print(f'Total votes {total_votes}')
            # print(f'Each candidate: {candidate_unique}')
            # print(f'Index: {candidate_unique.index(candidate_in)}')
    #The percentage of votes each candidate won
    perc_vote_list = []
    votes_recieved = candidate_num_votes[0]
    votes_index =0
    # 'x' is loop value
    for x in range(len(candidate_unique)):
        vote_percentage = round(candidate_num_votes[x]/total_votes*100,2)
        perc_vote_list.append(vote_percentage)
        if candidate_num_votes[x]>votes_recieved:
            votes_recieved= candidate_num_votes
            votes_index = x
    election_winner = candidate_unique[votes_index] 
print ("Election Results")
print("------------------------")
print(f'Total Votes: {total_votes}')
print("------------------------")
for x in range(len(candidate_unique)):
    print(f'{candidate_unique[x]} : {perc_vote_list[x]}% ({candidate_num_votes[x]})')
print("------------------------")
print(election_winner)
print("------------------------")
#output to results.txt under pypoll analysis
output_path = os.path.join("PyPoll", "Analysis", "Results.txt")
with open(output_path, 'w', newline = '') as datafile:
    datafile.write ('Election Results\n')
    datafile.write ('------------------------\n')
    datafile.write (f'Total Votes: {total_votes}\n')
    datafile.write ('------------------------\n')
    for x in range(len(candidate_unique)):
        datafile.write(f'{candidate_unique[x]} : {perc_vote_list[x]}% ({candidate_num_votes[x]})\n')
    datafile.write ('------------------------\n')
    datafile.write(f'Winner: {election_winner} \n')
    datafile.write('------------------------')
