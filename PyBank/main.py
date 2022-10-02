# ## PyBank Instructions

# In this challenge, you are tasked with creating a Python script to analyze the financial records of your company. 
# You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). 
# The dataset is composed of two columns: "Date" and "Profit/Losses".
#  (Thankfully, your company has rather lax standards for accounting, so the records are simple.)

# Your task is to create a Python script that analyzes the records to calculate each of the following:

# * The total number of months included in the dataset

# * The net total amount of "Profit/Losses" over the entire period

# * The changes in "Profit/Losses" over the entire period, and then the average of those changes

# * The greatest increase in profits (date and amount) over the entire period

# * The greatest decrease in profits (date and amount) over the entire period

# Your analysis should look similar to the following:

#   ```text
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $22564198
#   Average Change: $-8311.11
#   Greatest Increase in Profits: Aug-16 ($1862002)
#   Greatest Decrease in Profits: Feb-14 ($-1825558)
#   ```
#

# import CSV data

import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")


with open (csvpath) as csvfile:
    budget_data = csv.reader(csvfile, delimiter = ",")
    # skip header
    header = next(budget_data)

    # set up lists
    all_profit_loss = []
    change_all_months = []
    # set up variables
    total_months = 0
    total_profit_loss = 0
    last_profit_loss = 0
    

    for row in budget_data:

        # sum months & profit/loss

        total_months = total_months + 1
        i = total_months - 1
        total_profit_loss = total_profit_loss + int(row[1])
        profit_loss = float(row[1])

        # add profit/loss value to table
        all_profit_loss.append(profit_loss)

        # get change in profits for each month
        change_month = profit_loss - last_profit_loss

        # collect all changes to obtain average, maximum, and minimum values
        change_all_months.append(change_month)
        # reset last profit
        last_profit_loss = all_profit_loss[i]
        
    average_change = sum(change_all_months)/i
    max_change = max(change_all_months)
    min_change = min(change_all_months)


    # average_change = sum(change_months)/len(change_months)

    print(total_months)
    print(total_profit_loss)
    # print(change_months)
    # print(average_change)
    # print(i)
       
    # print(all_profit_loss)
    # print(change_all_months)
    # print(average_change)
    print(max_change)
    print(min_change)
    
    
    

    