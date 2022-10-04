import os
import csv
from collections import Counter

csvpath = os.path.join("Resources","election_data.csv")

with open(csvpath) as csvfile:
    election_data = csv.reader(csvfile, delimiter = ",")
    # skip header
    header = next(election_data)

    candidate_list = []
    candidate_results = []
    candidate_votes = {}
    total_votes = 0
    
      

    for row in election_data:
        
        total_votes = total_votes + 1
        candidate = str(row[2])
        candidate_list.append(candidate)

    candidate_votes = Counter(candidate_list)
filepath = os.path.join("analysis","analysis.txt")
with open(filepath, "w") as text:

    text.write("\n")
    text.write("Election Results\n")
    text.write("\n")
    text.write("-------------------------\n")
    text.write("\n")
    text.write(f"Total Votes: {total_votes}\n")
    text.write("\n")
    text.write("-------------------------")
    text.write("\n")


    
    for i in candidate_votes:
        candidate_percentage = ((candidate_votes[i])/total_votes)
        text.write(f"{i}:{'{:.3%}'.format(candidate_percentage)} ({candidate_votes[i]})\n")
    
        
    text.write("\n")
    text.write("-------------------------\n")

    winner = max(candidate_votes, key=candidate_votes.get)

    text.write(f"Winner: {winner}\n")
    text.write("\n")
    text.write("--------------------------")


        
    

        
        
       
    