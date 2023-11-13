#Financial Analyis.  Must be run from the PyBank folder to which the "analysis" and "Resource" folders 
# are children.

# Modules
import os
import csv

# Open the CSV using the UTF-8 encoding

# Set CSV path for file to the Resource Folder
csvpath = os.path.join(".", "Resources", "budget_data.csv")

#set up some Variables for processing
periodChange = [] #list to store the change in profit/loss column from one row to the next
myMonths = [] # list for storing month the period change is for
lastMonth = "" # to track the name of the last month processed
lastBalance = 0 #the last balance processed
FirstRow = True #flag to track when first row has been processed
countMonth = 0 #variable to count the monts as they change
netTotal = 0 #variable to store the running netTotal

# Open the CSV using the UTF-8 encoding
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
        if FirstRow: #if the first row just store the periods balance
             lastBalance = int(myRow[1])
             FirstRow = False
        else: #if succeeding rows calculate the period change and store it to a list do the same with the month name
             periodChange.append(int(myRow[1])-lastBalance) #add the change in balance to the periodChange list
             lastBalance = int(myRow[1]) #update the last balance for the next loop
             myMonths.append(myRow[0]) # track what month the balance change applies to

    maxIncrease = max(periodChange) #find the value of the period with the greatest increase
    maxDecrease = min(periodChange) #find the value of the period with the greatest decrease
    maxIndex = periodChange.index(maxIncrease) #store the periods index
    minIndex = periodChange.index(maxDecrease) #store the periods index
    
    #use the index to find the corresponding month strings
    maxMonth = myMonths[maxIndex] 
    minMonth = myMonths[minIndex]
    
    #calculate the average change using the properties of the period change list.    
    avgChange = sum(periodChange)/len(periodChange)

    #lets print the results out to the terminal
    print("Financial Analysis")
    print("-------------------------------------")
    print(f"Total Months: {countMonth}")
    ptotal="Total ${:.0f}"
    print(ptotal.format(netTotal))
    pavgchg="Average Change: ${:.2f}"
    print(pavgchg.format(avgChange))
    pmaxin="Greatest Increase in Profits: {:.0f}"
    print(f"Greatest Increase in Profits: {maxMonth} (${maxIncrease})")
    print(f"Greatest Decrease in Profits: {minMonth} (${maxDecrease})")
    
    #lets write it out again to a text file
    txtfile = open(".\\analysis\\financial_analysis.txt","w")
    txtfile.write("Financial Analysis\n")
    txtfile.write("-------------------------------------\n")
    txtfile.write(f"Total Months: {countMonth}\n")
    ptotal="Total ${:.0f}\n"
    txtfile.write(ptotal.format(netTotal))
    pavgchg="Average Change: ${:.2f}\n"
    txtfile.write(pavgchg.format(avgChange))
    pmaxin="Greatest Increase in Profits: {:.0f}\n"
    txtfile.write(f"Greatest Increase in Profits: {maxMonth} (${maxIncrease})\n")
    txtfile.write(f"Greatest Decrease in Profits: {minMonth} (${maxDecrease})\n")
    
        
