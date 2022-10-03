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
    change_all_profits = []
    # set up variables
    total_months = 0
    total_profit_loss = 0
    last_profit_loss = 0
    

    for row in budget_data:

        # sum months & profit/loss

        total_months = total_months + 1
        d = total_months - 1
        total_profit_loss = total_profit_loss + int(row[1])
        profit_loss = int(row[1])
        change_month = str(row[0])

        # add profit/loss value to table
        all_profit_loss.append(profit_loss)
        
        change_all_months.append(change_month)

        # get change in profits for each month
        change_profit = profit_loss - last_profit_loss

        # collect all changes to obtain average, maximum, and minimum values
        change_all_profits.append(change_profit)
        # reset last profit
        last_profit_loss = all_profit_loss[d]
    # remove change in profits for first month as it is picking up the profit and not truly reflecting the change.  
    change_all_months.pop(0)
    change_all_profits.pop(0)
        
    # define variables
    max_change = max(change_all_profits)
    min_change = min(change_all_profits)

    average_change = sum(change_all_profits)/len(change_all_profits)

    # zip change in profits to months for reference
    max_min = dict(zip(change_all_profits,change_all_months))

    for i in max_min:
        if i == max_change:
            max_month = max_min[i]
        elif i == min_change:
            min_month = max_min[i]

    print("Financial Analysis")
    print(total_months)
    print(total_profit_loss)
    print(average_change)
    print(max_month)
    print(max_change)
    print(min_month)
    print(min_change)
    
    
    

    