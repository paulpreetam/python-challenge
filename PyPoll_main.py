# GPP python script that analyzes the rural town modernize its vote counting process:
import os
import csv
import collections as ct

csvpath = os.path.join("Resources", "election_data.csv")
#print(csvpath)
tot_num_of_votes = 0
candidate_unique = []
candidate_vote_count = []

with open(csvpath,'r') as csvfile:
    votes = ct.Counter()
    reader = csv.reader(csvfile)
    next(reader)
    for line in reader:
        candidate = line[-1]
        votes[candidate] += 1
        tot_num_of_votes += 1
        candidate_in = (line[2])
#    print('Candidate and Votes', votes)
    print('Election Results')
    print('--------------------------------')
    print('Total Votes: ',str(tot_num_of_votes)+' votes')
    print('--------------------------------')
    # for each_candidate in votes:
    #     print(each_candidate)
    for candidate_name, num_votes in sorted(votes.items(),key=lambda kv: kv[1]):
        print(candidate_name,'-', num_votes)
        
        if candidate_in in candidate_unique:
            candidate_index = candidate_unique.index(candidate_in)
            candidate_vote_count[candidate_index] = candidate_vote_count[candidate_index] + 1
        else:
            candidate_unique.append(candidate_in)
            candidate_vote_count.append(1)
            
        pct = []
        max_votes = candidate_vote_count[0]
        max_index = 0
    
        for x in range(len(candidate_unique)):
            vote_pct = round(candidate_vote_count[x]/tot_num_of_votes*100, 2)
            pct.append(vote_pct)
            
            if candidate_vote_count[x] > max_votes:
                max_votes = candidate_vote_count[x]
                max_index = x
                print(max_votes)
                print(max_index)

            election_winner = candidate_unique[max_index]
           # print(election_winner)
