import os
import csv

election_input_file = os.path.join('Resources/', 'election_data.csv')
election_output_file = os.path.join("analysis/", "election_analysis.txt")
total_votes = 0
candidate1 = "Khan"
candidate2 = "Correy"
candidate3 = "Li"
candidate4 = "O'Tooley"
candidate1_counter = 0
candidate2_counter = 0
candidate3_counter = 0
candidate4_counter = 0
cnt = 1

with open(election_input_file,'r') as election_input_file_filehandler:
    election_voting_file = csv.reader(election_input_file_filehandler,delimiter=',')
    next
    print(election_voting_file)
    for voter_record in election_voting_file:
        #print(voter_record)
        voter_id = voter_record[0]
        voter_country = voter_record[1]
        voter_candidate = voter_record[2]
        total_votes = total_votes + int(cnt)
        cnt = cnt + 1
        if voter_candidate == candidate1:
            candidate1_counter = candidate1_counter + 1
        elif voter_candidate == candidate2:
            candidate2_counter = candidate2_counter + 1
        elif voter_candidate == candidate3:
            candidate3_counter = candidate3_counter + 1
        elif voter_candidate == candidate4:
            candidate4_counter = candidate4_counter + 1


print(f'{candidate1} votes :{candidate1_counter}')
print(f'{candidate2} votes :{candidate2_counter}')
print(f'{candidate3} votes :{candidate3_counter}')
print(f'{candidate4} votes :{candidate4_counter}')

        

