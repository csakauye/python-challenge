# PyPoll Script - analyzing votes 
# Goal: To create a Python script that analyzes and calculates the votes of a small town 

# Import os module to allow for the path to be set 
import os

# Import csv module to help interface with csv file 
import csv

# Creating path to get to the csv file, using os module 
vote_path = os.path.join('PyPoll', 'Resources', 'election_data.csv')

# Opening the csv file, identifying the delimiter as a comma and storing the header 
with open(vote_path) as vote_file: 
    vote_reader = csv.reader(vote_file, delimiter=',')
    vote_header = next(vote_reader)

    # Creating list to hold the vote count 
    total_votes = []
    # Creating a list to hold all the candidates names, repeats included 
    total_candidates = []
    # Creating a list to hold only unique names, doesn't include candidate name repeats 
    unique_candidates = []
    # Creating a list to hold the ballots with votes for Charles, Diana and Raymon 
    charles_votes = []
    diana_votes = []
    raymon_votes = []
    # Creating a list to hold all candidates' voter information
    all_info_list = []
   
   # For loop cycling through all the data
    for rows in vote_reader:
        
        # Identifying the ballots in column 1, index 0
        votes = rows[0]
       
       # Adding all the votes/ballots to the total_votes list 
        total_votes.append(votes)
        
        # Identifying the candidate names in column 3, index 2
        candidates = rows[2]

        # Adding all the candidate names to a list. This list pulls in the candidate name for each row, therefore there are many duplicates 
        total_candidates.append(candidates)

    # Calculating the total number of votes based on the count of ballots 
    total_votes_num = len(total_votes)

    # Creating a for loop to loop through the total_candidates list. If any names aren't in the unique_candidates list, they will be added. Because this starts as an empty list, all three of the candidates names will be added but only once        
    for names in total_candidates:
        if names not in unique_candidates:
            unique_candidates.append(names)

    # Identifying the number of votes per candidate. Using a for loop to cycle through the total_candidates list and storing any votes associated with each name in individual lists   
    for votes_name in total_candidates:
        if votes_name == "Charles Casper Stockham":
           charles_votes.append(candidates)
        elif votes_name == "Diana DeGette":
            diana_votes.append(candidates)
        else:
            raymon_votes.append(candidates)
   
   # Getting the number/count of votes from each candidate vote list 
    charles_num = len(charles_votes)
    diana_num = len(diana_votes)
    raymon_num = len(raymon_votes)

    # Creating a list with each number of votes per candidate, will use to print out results in Terminal/file 
    votes_assigned = [charles_num, diana_num, raymon_num]

    # Determining each candidate's voter percentage by dividing their number of votes by the total votes 
    percent_charles = charles_num/total_votes_num
    percent_diana = diana_num/total_votes_num
    percent_raymon = raymon_num/total_votes_num

    # Changing the percents calculated above into actual percentages, reported out to the third decimal place 
    per_charles = "{0:.3%}".format(percent_charles)
    per_diana = "{0:.3%}".format(percent_diana)
    per_raymon = "{0:.3%}".format(percent_raymon)

    # Creating a list with each percentage per candidate, will use to print out results in Terminal/file 
    per_all = [per_charles, per_diana, per_raymon]

    # Printing out Election Results and Total Votes in the Terminal 
    print("Election Results")
    print("----------------------------------")
    print(f"Total Votes: {total_votes_num}")
    print("----------------------------------")

    # In order to print out the list, created for loops to show each value in its own separate line
    # Setting up the for loop to pull each candidate's name 
    for politician in unique_candidates:
        # Setting up for loop to pull the number of votes per candidate (assigned votes)
        for assigned in votes_assigned:
            # Setting up the portion/percentage of the votes that belongs to each candidate 
            for portion in per_all:
                # Concatenating the information 
                all_info = politician + ":" + " " + str(portion) + " " + "(" + str(assigned) + ")"
                # Creating a list by appending each concatenated iteration. This gives a list with a lot of repeats     
                all_info_list.append(all_info)
    # Since the all_info_list has a lot of repeats, I tried to find a way to pull out only the information needed. The way I was able to get my code to work was using the del function to delete out the pieces of information I didn't want by their index
    del all_info_list[1:13]
    # The del function was more of a manual way of deleting out the unneeded information because it required me to count the indexes. I could pull the individual numbers by themselves, but in order to get it to read out alongside the candidate name and percentage, this is what I came up with 
    del all_info_list[2:14]
    # Prints out new list 
    for each in all_info_list:
        print(each)
    
    print("----------------------------------")
    
    # If statement determining who won based on number of votes 
    if charles_num > diana_num and raymon_num:
        print("Winner: Charles Casper Stockham")
    elif diana_num > charles_num and raymon_num:
        print("Winner: Diana DeGette")
    else:
        print("Winner: Raymon Anthony Doane")
    
    print("----------------------------------")

# Setting up the path to access the text file to write to
txt_path = os.path.join("PyPoll", "analysis", "pypoll.txt")

# Printing the calculated analysis from above in a text file using write, need to use \n to get the data to print on separate lines
with open(txt_path, 'w') as txt_file:
    txt_file.writelines("Election Results\n")
    txt_file.writelines("----------------------------------\n")
    txt_file.writelines(f'Total Votes: {len(total_votes)}\n')
    txt_file.writelines("----------------------------------\n")
    # Had to copy the for loops and if statements from earlier in the code in order to get the data in the text file 
    for politician in unique_candidates:
        for assigned in votes_assigned:
            for portion in per_all:
                all_info = politician + ":" + " " + str(portion) + " " + "(" + str(assigned) + ")"
                all_info_list.append(all_info)
    del all_info_list[1:16]
    del all_info_list[2:14]
    for each in all_info_list:
        txt_file.writelines(f' {each}\n')
    txt_file.writelines("----------------------------------\n")
    if charles_num > diana_num and raymon_num:
        txt_file.writelines("Winner: Charles Casper Stockham\n")
    elif diana_num > charles_num and raymon_num:
        txt_file.writelines("Winner: Diana DeGette\n")
    else:
        txt_file.writelines("Winner: Raymon Anthony Doane\n")
    txt_file.writelines("----------------------------------\n")
  
    