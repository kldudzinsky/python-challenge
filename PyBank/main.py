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

#create empty lists
date = []
profit_loss= []
monthly_profit_change =[]
#number of months includedd
with open(Bank_csv) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    lines = len(list(csvreader))
 # sum of Profit/losses
    total_months = sum(float(row[1]) for row in csvreader)
#avg of change between each line 
    for row in csvreader:
        date.append(row[0])
        profit_loss.append(int(row[1]))
    #loop to get monthly changes in profits
    for i in range(len(profit_loss)-1):
        monthly_profit_change.append (int)
        [profit_loss[i+1]-profit[i]] 

        avg_change =round((sum(monthy_profit_change)/85),2)
# max and min of monthly profit 
great_increase= max(monthly_profit_change)
great_decrease= min(monthly_profit_change)
# Correlate max and min to month with month list and index from greatest inc and greatest dec. 
#add + 1 at end b/c month with the change is next month
great_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
great_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

#print
print (f"number of months: {lines}") 
print(f"sum of profits/lossts: {total_months}")
print (f"Average change: $ {avg_change}" )
print (f"Greatest Increase in Profits: {date[great_increase_month]} (${(str(great_increase))})")
print(f"Greatest Decrease in Profits: {date[great_decrease_month]} (${(str(great_decrease))})")