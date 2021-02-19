#python script that analyzes the records to calculate each of the following:
import os
import csv
import numpy as np

csvpath = os.path.join("Resources", "budget_data.csv")
print(csvpath)
#The total number of months included in the dataset
num_of_months = 0
data = []
proloss = []

with open(csvpath,'r') as csvfile:
    csv_reader_obj = csv.reader(csvfile)
    if csv.Sniffer().has_header:
        next(csv_reader_obj)
        for row in csv_reader_obj:
            data.append(row)
        
    for i in range(len(data)):
        proloss.append(float(data[i][1]))
        num_of_months += 1       
    print('Financial Analysis')
    print('--------------------------------------------')

#The total number of months included in the dataset
    print('Total Months: = ',str(num_of_months)+' months')

#The net total amount of "Profit/Losses" over the entire period
    print('Total = $',format((np.sum(proloss)), ".2f"))
 
#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    print('Average  Change = $',format((np.mean(proloss)), ".2f"))

#The greatest increase in profits (date and amount) over the entire period
    print('Greatest Increase in Profits = ',format((np.max(proloss)), ".2f"))

#The greatest decrease in losses (date and amount) over the entire period
    print('Greatest Decrease in Profits = ',format((np.min(proloss)), ".2f"))
    print('--------------------------------------------')
