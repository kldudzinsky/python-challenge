# Import Dependencies

import os
import csv

Bank_csv = os.path.join("PyBank", "Resources", "Bank_Resources_budget_data.csv")

# Create empty lists to iterate through specific rows for the following variables
total_months = []
total_profit = []
monthly_profit_change = []
 
with open(Bank_csv) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)

    for row in csvreader: 

        # Append months and profit 
        total_months.append(row[0])
        total_profit.append(int(row[1]))
    
    # Iterate through the profits in order to get the monthly change in profits
    for i in range(len(total_profit)-1):
        
        # Take the difference between two months and append to monthly profit change
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
        
# Obtain the max and min of the the montly profit change list
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

# Correlate max and min to the proper month using month list and index from max and min
#We use the plus 1 at the end since month associated with change is the + 1 month or next month
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 
 

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${max_increase_value})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${max_decrease_value})")

# # Output files
# output_file = Path("Homework 3 Python", "Financial_Analysis_Summary.txt")

# with open(output_file,"w") as file:
    
# # # Write methods to print to Financial_Analysis_Summary 
#     print("Financial Analysis")
#     print("\n")
#     print("----------------------------")
#     print("\n")
#     print(f"Total Months: {len(total_months)}")
#     print("\n")
#     print(f"Total: ${sum(total_profit)}")
#     print("\n")
#     print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
#     print("\n")
#     print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
#     print("\n")
#     print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
