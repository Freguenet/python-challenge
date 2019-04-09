import os
import csv
# Import File
pybankpath = os.path.join("..", "Pypoll", "election_data.csv")

exportfile = "voteannalysis.txt"
# Define variables
total_votes = 0
votes = 0
percentage = 0
name_row = 0
all_candidate_list = []
candidate_names = []
vote_dictionary = {}

with open (pybankpath, newline="") as election_data:
    csv_reader = csv.reader (election_data)
    csv_header = next(csv_reader)
   

    for row in csv_reader:
       total_votes = total_votes + 1
       all_candidate_list.append(row[2])

    print (str("Election Results"))
    print (str("---------------------"))
    print (f"Total Votes: ", total_votes)
    print (str("---------------------"))
    
    for row in all_candidate_list:
        if row not in candidate_names:
            candidate_names.append(row)
    
    for row in candidate_names:
        name = str(candidate_names[name_row])
        votes = all_candidate_list.count(name)
        percentage = "{0:.0f}%".format((int(votes) / int (total_votes)) * 100)
        vote_dictionary.update({name: [votes, percentage]})
        print (name, ":", percentage, "(",votes,")")
        name_row = name_row + 1

    print (f"Winner of the Election is: ", max(percentage))

with open(exportfile, 'w') as file:
    file.write("Vote Annalysis \n"
    f"Election Results\n"
    f"---------------------\n"
    f"Total Votes: {total_votes}\n"
    f"---------------------\n"
    f"{name}: {percentage} ({votes})")
    file.close()


