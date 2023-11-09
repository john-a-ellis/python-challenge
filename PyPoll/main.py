#Election Results Analyis.  Must be run from the PyPoll Folder.

# Modules
import os
import csv

# Open the CSV using the UTF-8 encoding

# Set CSV path for file to the Resource Folder
csvpath = os.path.join(".", "Resources", "election_data.csv")
#Create two lists one list of integers to store Candidate Vote Counts and one list of strings of Candidate Names
intCandidateVotes = []
strCandidates = []


with open(csvpath, encoding='UTF-8') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    #Read the first header row.
    listheader = csv_header
    #read through the rest of the file by row.
    for myRow in csvreader:
        #Check to see if the Candidate name appearing on the row can be found in the list of Candidates. 
        #If the Candidate isn't found in the current list append them to it and add an entry in the Votes list
        #counting one vote.
        if myRow[2] not in strCandidates:
            strCandidates.append(myRow[2])
            intCandidateVotes.append(1)
        else:
            # if the Candidate is found in the Candidate list add the vote to the corresponding vote tally in the
            # Candidates vote count.
            foundCandidate=myRow[2]          
            iVote = strCandidates.index(foundCandidate) #find the index for the candidate
            cVotes=intCandidateVotes[iVote]+1 #add the vote to the candidates tally
            intCandidateVotes[iVote] = cVotes #return the updated canadidates tally to the list.
    
    iWinner = max(intCandidateVotes) #once file is processed find the index of the candidate with the most votes
    
    sWinner = strCandidates[intCandidateVotes.index(iWinner)] #use that index to identify the winner
    
    totalvotes=0 #create a storate for the total votes.
    #lets sum up the voltes for all candidates to determine the total voted.
    for Candidate in range(len(strCandidates)):
        totalvotes += intCandidateVotes[Candidate]
    print ("Election Results \n")
    print ("-------------------------------------\n")
    print (f"Total Votes: {totalvotes}\n")
    print ("-------------------------------------\n")
    #Print out the results for each candidate and make sure they're formatted correctly.
    for Candidate in range(len(strCandidates)):
        print(strCandidates[Candidate] + ": {0:.3%} ({1})\n".format(intCandidateVotes[Candidate]/totalvotes, intCandidateVotes[Candidate]) )
        
    print("--------------------------------------\n")
    print(f"Winner: {sWinner}\n")
    print("--------------------------------------\n")

#Write it out again to the Text File 
txtfile = open(".\\analysis\election_analysis.txt","w")
txtfile.write("Election Results \n")
txtfile.write("-------------------------------------\n")
txtfile.write(f"Total Votes: {totalvotes}\n")
txtfile.write("-------------------------------------\n")
for Candidate in range(len(strCandidates)):
    txtfile.write(strCandidates[Candidate] + ": {0:.3%} ({1})\n".format(intCandidateVotes[Candidate]/totalvotes, intCandidateVotes[Candidate]) )

txtfile.write("-------------------------------------\n")
txtfile.write(f"Winner: {sWinner}\n")
txtfile.write("-------------------------------------\n")

txtfile.close()
        


                              
    




   