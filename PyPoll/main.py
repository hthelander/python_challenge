# import csv data
import os
import csv

csvpath = os.path.join("Resources","election_data.csv")

with open(csvpath) as csvfile:
    election_data = csv.reader(csvfile, delimiter = ",")
    # skip header
    header = next(election_data)

    candidate_list = []
    # candidate_votes = 

    total_votes = 0

      

    for row in election_data:
        
        total_votes = total_votes + 1
        candidate = str(row[2])


        
        for i in candidate_list:
            if candidate != i:
                candidate_list.append(candidate)
        candidate_list.append(candidate)
                

    print(total_votes)
    print(candidate_list[2])
                  
        

        
        



        
        

    print(total_votes)

    print(candidate_list)





