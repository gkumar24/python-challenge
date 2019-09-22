# This is main.py in PyPoll
## Python script for analyzing the poll data
##Poll data: election_data.csv, Data Columns: Voter ID, County, and Candidate 
## Tasks to calculate: Total votes casted, List of candidates who received votes, 
##      percentage of votes each candidate won, total number of votes each candidate won, 
##      winner of the election based on popular vote, 
##      Print Output, and export to text file.

# Modules
import os
import csv

# Set path for data file
csv_path = os.path.join("Resources", "election_data.csv")

# Open the CSV
with open(csv_path, newline="") as csv_file: 
    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csv_reader)

    # set statistical variables
    total_votes = 0     # Total Votes casted
    candidate_list = {} # Dictionary that holds the Candidates and their votes
    winner_name = ""    # For storing the winner
    winner_count = 0    # for storing and comparing the votes
    
    # reading each row of data, after header, each row is a "List"
    for row in csv_reader:
        voter_id = row[0]
        county_name = row[1]
        candidate_name = row[2]

        #Count each vote for total votes
        total_votes = total_votes + 1

        #Check if Candidate exist in dictionary
        if candidate_name in candidate_list:
            #if canditate is in list, keep keep adding the votes
            candidate_list[candidate_name] = candidate_list[candidate_name] + 1
        else:
            #if candidate not in list, add new key for the canditate, and the initial count
            candidate_list.update({candidate_name : 1})

        # Compare the count, to set the winner.
        # Commented the code, since the comparision can be done, once the counts are final. 
        #if no winner, assume the first canditate as the winner
        #if winner_name == "":
        #    winner_name = candidate_name 
        #if float(candidate_list[winner_name]) < float(candidate_list[candidate_name]):
        #    winner_name = candidate_name

#Print the result
print("Election Results")
print("-------------------------")
print("Total Votes: {:,}".format(total_votes))
print("-------------------------")
for (key, value) in candidate_list.items():
    if winner_count < value:
        winner_name = key
        winner_count = value
    print("{}: {:.2%} ({:,})".format(key,float(value)/total_votes,value))
print("-------------------------")
print(f"Winner: {winner_name}")
print("-------------------------")

#create the text file, with the results. 
txt_path = open("PyPoll_Output.txt","w")
txt_path.write("Election Results\n")
txt_path.write("-------------------------\n")
txt_path.write("Total Votes: {:,}\n".format(total_votes))
txt_path.write("-------------------------\n")
for (key, value) in candidate_list.items():
    txt_path.write("{}: {:.2%} ({:,})\n".format(key,float(value)/total_votes,value))
txt_path.write("-------------------------\n")
txt_path.write(f"Winner: {winner_name}\n")
txt_path.write("-------------------------\n")
txt_path.close()









