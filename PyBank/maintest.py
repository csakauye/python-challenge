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
    total_months = []
    all_data = []
    for columns in budget_reader:
        months = columns[0]
        total_months.append(months)
        amount = int(columns[1])
        total_amount.append(amount)

    




  
  
 
    # Calculating the changes in "Profit/Losses" over the entire period, and then the average of those changes 

    # Printing the calcualted analysis from above in a text file using write 