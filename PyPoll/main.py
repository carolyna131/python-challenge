# Import modules os and csv
import os
import csv

# Set the path for the CSV file in PyPollcsv

election_data_csv = os.path.join("Resources","election_data.csv")

# Create the lists to store data. 

count = 0
candidatelist = []
candidates = []
vote_count = []
vote_percent = []

# Open the CSV using the set path PyPollcsv

with open(election_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        # Count the total number of votes
        count = count + 1

        # Set the candidate names to candidate list
        candidatelist.append(row[2])
        
    #Create a set from the candidate list to get the unique candidate names
    
    for x in set(candidatelist):
        candidates.append(x)
        # y is the total number of votes per candidate
        y = candidatelist.count(x)
        vote_count.append(y)
        # z is the percent of total votes per candidate
        z = round(((y/count)*100),3)
        vote_percent.append(z)
        
    
    winning_vote_count = max(vote_count)
    winner = candidates[vote_count.index(winning_vote_count)]

    
# Print to terminal
 
print(f"Election Results")   
print(f"-------------------------")
print(f"Total Votes: {count}")    
print(f"-------------------------")
for i in range(len(candidates)):
    print(candidates[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
print(f"-------------------------")
print(f"The winner is: " + winner)
print(f"-------------------------")

# Print to a text file: election_results.txt
#output analysis to file
output_path = os.path.join("..","Analysis", 'election_results.txt')

#Open the file using "write" mode. Specify the variable to hold the contents
with (open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(candidates))):
        text.write(candidates[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")