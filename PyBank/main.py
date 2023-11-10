# Modules
import os
import csv

# Open the CSV using the UTF-8 encoding

# Set CSV path for file to the Resource Folder
csvpath = os.path.join(".", "Resources", "budget_data.csv")
#Create two lists one list of integers to store Candidate Vote Counts and one list of strings of Candidate Names
#setup some lists
periodchange = [] 
maxIncrease = 0
maxDecrease = 0
netTotal = 0.0
myMonths = []
lastMonth = ""
countMonth=0
rowCount=0
lastBalance = 0
with open(csvpath, encoding='UTF-8') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    #Read the first header row.
    listheader = csv_header
    #read through the rest of the file by row.
    for myRow in csvreader:
        netTotal = netTotal + float(myRow[1])
        #count the months in the list
        if lastMonth != myRow[0]: 
                countMonth+=1 #add a new month
                lastMonth = myRow[0]
        if rowCount == 0: #if the first row just store the periods balance
             lastBalance = int(myRow[1])
             rowCount +=1
        else: #if succeeding rows calculate the period change and store it to a list do the same with the month name
             periodchange.append(int(myRow[1])-lastBalance) #add the change in balance to the periodchange list
             lastBalance = int(myRow[1]) #update the last balance for the next loop
             myMonths.append(myRow[0]) # track what month the balance change applies to

    maxIncrease = max(periodchange) #find the value of the period with the greatest increase
    maxDecrease = min(periodchange) #find the value of the period with the greatest decrease
    maxIndex = periodchange.index(maxIncrease) #store the periods index
    minIndex = periodchange.index(maxDecrease) #store the periods index

    maxMonth = myMonths[maxIndex] #use the index to find the corresponding month strings
    minMonth = myMonths[minIndex]
    #calculate the average change using the properties of the period change list.    
    avgChange = sum(periodchange)/len(periodchange)

    #lets print it out
    print("Financial Analysis\n")
    print("-------------------------------------\n")
    print(f"Total Months: {countMonth}\n")
    ptotal="Total {:.0f}\n"
    print(ptotal.format(netTotal))
    pavgchg="Average Change: ${:.2f}\n"
    print(pavgchg.format(avgChange))
    pmaxin="Greatest Increase in Profits: {:.0f}\n"
    print(f"Greatest Increase in Profits: {maxMonth} (${maxIncrease})\n")
    print(f"Greatest Decrease in Profits: {minMonth} (${maxDecrease})\n")
    
    #lets write it out again to a text file
    txtfile = open(".\\analysis\\financial_analysis.txt","w")
    txtfile.write("Financial Analysis\n")
    txtfile.write("-------------------------------------\n")
    txtfile.write(f"Total Months: {countMonth}\n")
    ptotal="Total {:.0f}\n"
    txtfile.write(ptotal.format(netTotal))
    pavgchg="Average Change: ${:.2f}\n"
    txtfile.write(pavgchg.format(avgChange))
    pmaxin="Greatest Increase in Profits: {:.0f}\n"
    txtfile.write(f"Greatest Increase in Profits: {maxMonth} (${maxIncrease})\n")
    txtfile.write(f"Greatest Decrease in Profits: {minMonth} (${maxDecrease})\n")
    
        
