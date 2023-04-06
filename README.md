# python-challenge
Module 3 Weekly Challenge 
# Hello

# For the PyBank and PyPoll challenges, I coded in Visual Studio Code and used the Python terminal add-in instead of running it in Git Bash. 

# I found some of this challenge to be relatively straight forward and other parts more difficult. 

# In PyBank, I found it challenging to calculate the average change and then to pull the dates of the greatest increase and decrease from that data set. Getting the actual greatest increase and decrease was easier to do with the statistics module. 

# In order to find the average change I created three different lists based on the indexing and subtracted them from each other using the zip() function. This wasn't something we learned in class but I looked it up and applied it to my code. I wasn't sure if functions we looked up needed to be cited, so I did so just in case. 
    # Entechin. “How to Subtract Two Lists in Python - (with Examples).” Entechin, 13 July 2022, https://www.entechin.com/subtract-two-lists-python/. 
    # The zip() function in used in PyBank on lines 65 and 68

# Another piece of code I looked up online was how to round decimal places. When I first got the average change calculation to work it produced $-8311.11 with a lot of trailing decimals. I wasn't sure how to round but used syntax from the website below. This can be found in my PyBank code on line 81. I also used it again in PyPoll to round the percentage votes for the candidates, lines 77 - 79. 
    # “Here Is How to LLIMIT Floats to Two Decimal Points in Python.” Here Is How to Limit Floats to Two Decimal Points in Python, https://pythonhow.com/how/limit-floats-to-two-decimal-points/#:~:text=To%20limit%20a%20float%20to,resulting%20in%20the%20value%203.14. 

# Lastly for PyBank, I struggled on how to pull the corresponding dates for the greatest increase/decrease. Originally, I tried to pull the date and increase/decrease simultaneously but couldn't figure it out. Instead, I ended up determining the indexes of the increase and decrease. Then, I created a list using the months in the same way I did the values. From there, I plugged in the index and had the date returned. 

# For PyPoll, I wasn't sure how to pull the candidates' names into a list without the data repeating itself. I looked up how to pull only unique data and used the following website as a resource. Lines 50 - 52 are where I applied this logic.
    # Mulani, Safa. “Get Unique Values from a List in Python.” DigitalOcean, DigitalOcean, 3 Aug. 2022, https://www.digitalocean.com/community/tutorials/get-unique-values-from-a-list-in-python. 

# Lastly in PyPoll, I was able to pull the individual information for each candidate relatively easily but struggled in printing out the information all together. Ultimately, the way I ended up compiling the information was by using a list. I recognize that the way I did this was inefficient. My list concatenated all the data but in doing so it ended up stringing together incorrect sequences, like listing Diana DeGette with Charles' and Raymon's numbers. To get rid of this data, I printed out the lists, counted the indexing and then deleted out the incorrect concatenations. 

# Overall, I learned a lot about Python and despite coding things in a possibly inefficient manner, I was able to find a way that worked for me as a new coder. 

# Thanks! 