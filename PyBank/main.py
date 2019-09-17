## This is main.py in PyBank
## Python script for analyzing the financial records of your company
## Financial data: budget_data.csv. Data Columns: Date and Profit/Losses. 
## Tasks to calculate: Total Months of Data, Net amount Profit/Loss, 
##   Average Profit/Loss, Greatest increase in Profit, Greatest decrease in losses.

# Modules
import os
import csv

# Set path for data file
csv_path = os.path.join("..", "..", "Resources", "budget_data.csv")

# Open the CSV
with open(csv_path, newline="") as csv_file:
    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csv_reader)

    # set statistical variables
    total_months = 0 # Total Month of financial data
    total_PnL_amount = 0   # Net Profit / Loss
    great_inc_profit_month = ""    # Month of greatest increase in profits
    great_inc_profit_amount = float("-inf")    # greatest increase in profits by value

    great_dec_losses_month = ""    # Month of greatest decrease in losses
    great_dec_losses_amount = float("inf")    # greatest decrease in losses by value

    # reading each row of data, after header, each row is a "List"
    for row in csv_reader:
        fin_month = row[0]  # Holds the Month Value of the Row
        fin_PnL_amount = float(row[1])   # Holds the Profit / Loss amount

        #Task 1: The total number of months included in the dataset
        total_months = total_months + 1
        
        #Task 2: The net total amount of "Profit/Losses" over the entire period
        total_PnL_amount = total_PnL_amount + fin_PnL_amount
        
        #Task 4: The greatest increase in profits (date and amount) over the entire period
        if great_inc_profit_amount < fin_PnL_amount:
            great_inc_profit_amount = fin_PnL_amount
            great_inc_profit_month = fin_month

        #Task 5: The greatest decrease in losses (date and amount) over the entire period
        if great_dec_losses_amount > fin_PnL_amount:
            great_dec_losses_amount = fin_PnL_amount
            great_dec_losses_month = fin_month


#Task 3: The average of the changes in "Profit/Losses" over the entire period
if total_months != 0:
    average_change_amount = total_PnL_amount / total_months
else:
    average_change_amount = 0

#Task 5: Result Display
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print("Total: ${:,}".format(int(total_PnL_amount)))
print("Average  Change: ${:,.2f}".format(average_change_amount))
print("Greatest Increase in Profits: {} (${:,})".format(great_inc_profit_month, int(great_inc_profit_amount)))
print("Greatest Decrease in Profits: {} (${:,})".format(great_dec_losses_month, int(great_dec_losses_amount)))

#Task6: Result exported to Text File. 
# Create text file, PyBank.txt, w(for write, Overwrite existing), + for create if file not exist
txt_path = open("PyBank_Output.txt","w")
txt_path.write("Financial Analysis\n")
txt_path.write("----------------------------\n")
txt_path.write(f"Total Months: {total_months}\n")
txt_path.write("Total: ${:,}\n".format(int(total_PnL_amount)))
txt_path.write("Average  Change: ${:,.2f}\n".format(average_change_amount))
txt_path.write("Greatest Increase in Profits: {} (${:,})\n".format(great_inc_profit_month, int(great_inc_profit_amount)))
txt_path.write("Greatest Decrease in Profits: {} (${:,})\n".format(great_dec_losses_month, int(great_dec_losses_amount)))
txt_path.close()

# Notes: 
# Total rows of data, excluding the header will give the total number of months. 
# Alternate Code to find sum. totalMonths = sum(1 for row in csvreader)