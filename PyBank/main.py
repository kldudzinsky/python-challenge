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

# Create empty lists
total_months = []
total_profit = []
monthly_profit_change = []
 
with open(Bank_csv) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter = ',')
    #skip header 
    csv_header = next(csvreader)

    for row in csvreader: 

        # Append total_months and total_profit to correct lists in csv file
        total_months.append(row[0])
        total_profit.append(int(row[1]))
        #total number of Months
        number_months = len(total_months)
        #total net of profits and loss
        net_profit= sum(total_profit)

    # loop through to get monthly avg change (-1 not 86 change, only 85)
    for i in range(len(total_profit)-1):
        
        #append list for profit change. profit(i+1) - previous profit 
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
    #set avg_change
    avg_change= round(sum(monthly_profit_change)/len(monthly_profit_change),2)
#greatest increase and greatest decrease from monthly_profit_change list
gr_increase_value = max(monthly_profit_change)
gr_decrease_value = min(monthly_profit_change)

# connect gr increase and gr decrease value with correct month. 
 #use +1 at end b/c month with change is actually the next month
gr_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
gr_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

#Print results! 
print(f"Total Months: {number_months}")
print(f"Total: $ {net_profit}")
print(f"Average Change: $ {avg_change}")
print(f"Greatest Increase in Profits: {total_months[gr_increase_month]} $ ({gr_increase_value})")
print(f"Greatest Decrease in Profits: {total_months[gr_decrease_month]} $ ({gr_decrease_value})")


#output to results.txt under pybank analysis 
#remember to add \n to continue writing on next line
output_path = os.path.join("PyBank", "Analysis", "Results.txt")
with open(output_path, 'w', newline = '') as datafile:
    datafile.write('Financial Analysis\n')
    datafile.write('--------------------- \n')
    datafile.write(f'Total Months: {number_months} \n')
    datafile.write(f'Total: $ {net_profit}\n')
    datafile.write(f'Average Change: $ {avg_change}\n')
    datafile.write(f"Greatest Increase in Profits: {total_months[gr_increase_month]} $({gr_increase_value})\n")
    datafile.write(f'Greatest Decrease in Profits: {total_months[gr_decrease_month]} $({gr_decrease_value}) \n' )