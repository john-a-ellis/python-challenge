# Modules
import os
import csv

# Open the CSV using the UTF-8 encoding

# Set CSV path for file to the Resource Folder
csvpath = os.path.join(".", "Resources", "election_data.csv")
# Set the output path to the Analysis Folder
# outpath = os.path.join(".", "analysis", "election_analysis.txt")


with open(csvpath, encoding='UTF-8') as csvfile:
    intCandidateVotes = []
    strCandidates = []

    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    listheader = csv_header
    # print(listheader)

    for myRow in csvreader:

        if myRow[2] not in strCandidates:
            strCandidates.append(myRow[2])
            intCandidateVotes.append(1)
        else:
            foundCandidate=myRow[2]
            # print(foundCandidate)
            
            iVote = strCandidates.index(foundCandidate)
            cVotes=intCandidateVotes[iVote]+1
           
            intCandidateVotes[iVote] = cVotes
    
    iWinner = max(intCandidateVotes)
    
    sWinner = strCandidates[intCandidateVotes.index(iWinner)]
    
    totalvotes=0
    for Candidate in range(len(strCandidates)):
        totalvotes += intCandidateVotes[Candidate]
    print ("Election Results \n")
    print ("-------------------------------------\n")
    print (f"Total Votes: {totalvotes}\n")
    print ("-------------------------------------\n")

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
        


                              
    




   