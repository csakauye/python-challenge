# PyBank Python Script - analyzing the financial data of a company
# Goal: To create a Python script that analyzes budget_data.csv to calculate different values 

# os is a Python module that allows us to change paths 
import os

# csv is another Python module that allows us to read and write to a csv file 
import csv

# statistics is another Python module that allows statistics functions to be called 
import statistics

# Setting up the correct file path using the os module to allow us to access the csv file 
budget_path = os.path.join('PyBank', 'Resources', 'budget_data.csv')

# Opening and reading the csv file using the previously defined budget_path. Also creating a new variable to open the file 
with open(budget_path) as budget_file:

    # Defined budget_file as the file to open, stating that we want to read the file and identifying the data separators/delimiters as a comma  
    budget_reader = csv.reader(budget_file, delimiter=',')

    # Storing the header row
    budget_header = next(budget_reader)

    # Creating empty lists to store data from the csv file 
    # Stores the column listing out the months 
    total_months = []
    # Stores the column listing out the different values for each day 
    total_amount = []
    # Stores the differences between the values for each day, used to calculate average change, greatest increase and greatest decrease
    total_difference = []
    # Stores the differences between the values for each day, starting at index 2 to account for all the changes between days
    total_difference2 = []
    # Creating a for loop to cycle through each row of data 
    for rows in budget_reader:
        
        # Identifying the first column, index 0, that holds the months 
        months = rows[0]
        
        # Making the column of dates into one list 
        total_months.append(months)
        
        # Identifying the second column, index 1, that holds the Profit/Losses and changing it from a string to an integer, so it can be summed 
        amount = int(rows[1])

        # Making the column of Profit/Losses into a list
        total_amount.append(amount)

        # Storing the numbers for values with even indexing, will use later in average change, greatest increase and decrease calculations
        even = total_amount[::2]

        # Storing the numbers for values with odd indexing, will use later in average change, greatest increase and decrease calculations
        odd = total_amount[1::2]

        # Storing even numbers starting at index 2, will use later in average change, greatest increase and decrease calculations
        even2 = total_amount[2::2]

    # Calculating the net total amount of "Profit/Losses" over the entire period 
    total = sum(total_amount)

    # Calculating the changes in "Profit/Losses" over the entire period, and then the average of those changes 

    # Combining the even and odd lists to get the changes between days, starting with day 0 and day 1
    for(a, b) in zip(even, odd):
        total_difference.append(b - a)
    # Combining the odd and even2 lists to get the changes between days, starting with day 1 and day 2
    for(c, d) in zip(odd, even2):
        total_difference2.append(d-c)
   
    # Getting total list of differences for all days 
    net_differences = total_difference + total_difference2
    
   # Getting the sum of the total differences 
    sum_nd = sum(net_differences)

    # Calculating the average change using the sum of the total differences and the length of the list 
    avg_change = sum_nd/len(net_differences)
    
    # Rounding the average change to 2 decimal places
    avg_change_rd = "{:.2f}".format(avg_change)

    # Calculating the greatest increase in profits (date and amount) over the entire period
    grt_increase = max(net_differences)

    # Calculating the greatest decrease in profits (date and amount) over the entire period
    grt_decrease = min(net_differences)

    # Printing out the information so it can appear in the terminal 
    print("Financial Analysis")
    print("------------------------------")

    # Including the len() function to count the number of months in the column 
    print(f"Total Months: {len(total_months)}")
    
    print(f"Total: ${total}")

    print(f"Average Change: ${avg_change_rd}")

    print(f"Greatest Increase in Profit: (${grt_increase})")
    
    print(f"Greatest Decrease in Profit: (${grt_decrease})")
    

# Setting up the path to access the text file to write to
txt_path = os.path.join("PyBank", "analysis", "pybank.txt")

# Printing the calcualted analysis from above in a text file using write, need to use \n to get the data to print on separate lines
with open(txt_path, 'w') as txt_file:
  txt_file.writelines("Financial Analysis\n")
  txt_file.writelines("------------------------------\n")
  txt_file.writelines(f'Total Months: {len(total_months)}\n')
  txt_file.writelines(f'Total: ${total}\n')
  txt_file.writelines(f"Average Change: ${avg_change_rd}\n")
  txt_file.writelines(f'Greatest Increase in Profit: (${grt_increase})\n')
  txt_file.writelines(f'Greatest Decrease in Profit: (${grt_decrease})\n')
    
    