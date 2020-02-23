import os
import csv 

election_csv = os.path.join('/Users/seanperez/Desktop/election_data.csv')


        
def candidate_list = [ 'Khan', 'Correy', 'Li', "O'Tooley" ]
            candidate_1 = 'Khan'
            candidate_2 = 'Correy'
            candidate_3 = 'Li'
            candidate_4 = 'OTooley'

            votes_1 = election_cell[2].count('Khan')
            votes_2 = election_cell[2]('Correy')
            votes_3 = election_cell[2]('Li')
            votes_4 = election_cell[2].count("O'Tooley")

        
        Total_Votes = sum(election_csv)
        Vote_Percentage_1 = (votes_1 / Total_Votes) * 100
        Vote_Percentage_2 = (votes_2 / Total_Votes) * 100
        Vote_Percentage_3 = (votes_3 / Total_Votes) * 100
        Vote_Percentage_4 = (votes_4 / Total_Votes) * 100
            Max_Votes = max(Vote_Percentage_1, Vote_Percentage_2, Vote_Percentage_3, Vote_Percentage_4)


    print(f"Election Results")
        print(f'-------------')
    print(f"Total Votes: {str(Total_Votes)}")
        print(f'-------------')
    print(f"{candidate_1}: {Vote_Percentage_1} ({votes_1})")
    print(f"{candidate_2}: {Vote_Percentage_2} ({votes_2})")
    print(f"{candidate_3}: {Vote_Percentage_3} ({votes_3})")
    print(f"{candidate_4}: {Vote_Percentage_4} ({votes_4})")
         print(f'-------------')
    print(f"Winner: {Max_Votes")

    




    








