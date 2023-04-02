# PyBank Python Script - analyzing the financial data of a company
# Goal: To create a Python script that analyzes budget_data.csv to calculate different values 

# os is a Python module that allows us to change paths 
import os

# csv is another Python module that allows us to read and write to a csv file 
import csv

import statistics

from statistics import mean 

# Setting up the correct file path using the os module to allow us to access the csv file 
budget_path = os.path.join('PyBank', 'Resources', 'budget_data.csv')

# Opening and reading the csv file using the previously defined budget_path. Also creating a new variable to open the file 
with open(budget_path) as budget_file:

    # Defined budget_file as the file to open, stating that we want to read the file and identifying the data separators/delimiters as a comma  
    budget_reader = csv.reader(budget_file, delimiter=',')

    # Storing the header row
    budget_header = next(budget_reader)
    
    # Creating a for loop to cycle through each row of data 
    total_amount = []
    total_diff = []
    total_diff2 = []
    for columns in budget_reader:
        amount = int(columns[1])
        total_amount.append(amount)
        even = total_amount[::2]
        odd = total_amount[1::2]
        even2 = total_amount[2::2]
    for(x, y) in zip(even, odd):
        total_diff.append(y - x)
    for(w, z) in zip(odd, even2):
        total_diff2.append(w-z)
    net = total_diff2 + total_diff
    avgchange = sum(net)/len(net)
    increase = max(net)
    decrease = min(net)
    for row in budget_reader: 
        if row[1] == increase:
            print("Greatest Increase in Profits: " + row[0] + {increase})
        elif row[1] == decrease:
            print("Greatest Decrease in Profits: " + row[0] + {decrease})
      

    #print(f"Greatest Increase in Profits: (${increase})"
    #print(f"Greatest Decrease in Profits: (${decrease})")
    #print(avgchange)
    #print(even)



  
  
 

    #change = total_amout[0] - total_amount[1]
    #print(change)
    
     

    
    # Calculating the changes in "Profit/Losses" over the entire period, and then the average of those changes 

    # Calculating the greatest increase in profits (date and amount) over the entire period

    # Calculating the greatest decrease in profits (date and amount) over the entire period 

    # Printng the calcualted analysis from above in the terminal 

    # Printing the calcualted analysis from above in a text file using write 