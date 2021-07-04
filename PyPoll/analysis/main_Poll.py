import os
import csv
import math

#Variable list
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

csvpath = os.path.join('..', 'resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:

   csvreader = csv.reader(csvfile, delimiter=',')
   csv_header = next(csvfile)
   
   #calculating number of votes for each candidate
   for row in csvreader:
      total_votes += 1
      if (row[2] == "Khan"):
         khan_votes += 1
      elif (row[2] == "Correy"):
         correy_votes += 1
      elif (row[2] == "Li"):
         li_votes += 1
      elif (row[2] == "O'Tooley"):
         otooley_votes += 1
      else:
         print(winner_name)
      
   #calculate percentage of votes
   khan_percent = (khan_votes / total_votes) 
   correy_percent = (correy_votes / total_votes) 
   li_percent = (li_votes / total_votes) 
   otooley_percent = (otooley_votes / total_votes) 

   winner = max(khan_votes, correy_votes, li_votes, otooley_votes)

   if winner == khan_votes:
      winner_name = "Khan"
   elif winner == correy_votes:
      winner_name = "Correy"
   elif winner == li_votes:
      winner_name = "Li"
   elif winner == otooley_votes:
      winner_name = "O'Tooley"
   else:
      winner_name = "We need some new candidates..."

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
print(f"Khan: {khan_percent:.3%} ({khan_votes})")
print(f"Correy: {correy_percent:.3%} ({correy_votes})")
print(f"Li: {li_percent:.3%} ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3%}({otooley_votes})")
print("-------------------------")
print("Winner: " + winner_name)
print("-------------------------")

output_file = os.path.join('..', 'analysis', 'election_results.text')
with open(output_file, 'w',) as txtfile:
   txtfile.write(f"Election Results\n")
   txtfile.write(f"----------------------------\n")
   txtfile.write(f"Total Votes: {total_votes}\n")
   txtfile.write(f"----------------------------\n")
   txtfile.write(f"Khan: {khan_percent:.3%} ({khan_votes})\n")
   txtfile.write(f"Correy: {correy_percent:.3%} ({correy_votes})\n")
   txtfile.write(f"Correy: {correy_percent:.3%} ({correy_votes})\n")
   txtfile.write(f"Correy: {correy_percent:.3%} ({correy_votes})\n")
   txtfile.write(f"----------------------------\n")
   txtfile.write(f"Winner: {winner_name}\n")
   txtfile.write(f"----------------------------\n")
   
