#Your task is to create a Python script that analyzes the records to calculate each of the following:
    #The total number of months included in the dataset
    # The net total amount of "Profit/Losses" over the entire period
    # The average of the changes in "Profit/Losses" over the entire period
    # The greatest increase in profits (date and amount) over the entire period
    # The greatest decrease in losses (date and amount) over the entire period
#In addition, your final script should both print the analysis to the terminal and export a text file with the results

import os
import csv

Bank_csv = os.path.join("PyBank", "Resources", "Bank_Resources_budget_data.csv")

#number of months includedd
with open(Bank_csv) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    lines = len(list(csvreader))
print ("number of months:", (lines))
# sum of Profit/losses
with open(Bank_csv) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    total = sum(float(row[1]) for row in csvreader)
print("sum of profits/lossts:", (total))
#avg of change between each line 
with open(Bank_csv) as csvfile:
    csv_header = next(csvreader)
    df.diff()
