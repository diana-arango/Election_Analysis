# Add our dependencies.
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Election_Analysis","Resources","election_results.csv")
# Write to files in python
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Election_Analysis","analysis","election_analysis.txt")
# Using the with statement with the "w" mode will open the file as a text file.
with open(file_to_save,"w") as txt_file:
# Write some data to the file.
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
#1. Initialize a total vote counter. The total number of votes cast
total_votes = 0
# Initialize a candidate list called: candidate_options 
candidate_options=[]
# Declare an empty dictionary for candidate votes
candidate_votes = {}
# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0 
# Open the election results and read the file.
with open(file_to_load) as election_data:
# To do: read and analyze the data here.
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
# Print the header row, using the next method()
    headers = next(file_reader)
# Print each row in the CSV file
    for row in file_reader:
    #2. Add the total vote count.
        total_votes += 1
#2. A complete list of candidates who received votes
# Print the candidate name from each row
        candidate_name = row[2]
# If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
# Add candidate_name to candidate_options which is the candidate list
            candidate_options.append(candidate_name)
# Begin tracking the candidates votes count
            candidate_votes[candidate_name] = 0 
# Add a vote to that candidates' count
        candidate_votes[candidate_name] += 1
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results,end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
#3. Determine the percentage of votes for each candidate by looping through the counts
#1. Iterate through the candidate list
    for candidate_name in candidate_votes:
    #2. Retreive vote count of a candidate
        votes=candidate_votes[candidate_name]
    #3. Calculate the percentage votes.
        vote_percentage = float(votes)/float(total_votes)*100
    #4. Print the candidate name and percentage of votes.
        candidate_results = (f"{candidate_name}:{vote_percentage:.1f}% ({votes:,})\n")
     # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
    #  Save the candidate results to our text file.
        txt_file.write(candidate_results)    
    # Determine winning vote count and candidate
        if(votes>winning_count) and (vote_percentage>winning_percentage):
            #2.If true then set winning_count = votes and winning_percent = vote_percentage
            winning_count=votes
            winning_percentage=vote_percentage
            #3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name   
#5. The winner of the election based on pupular vote.Print out the winning candidate summary.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary, end="")
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)
