import os
import csv
import math

#Variable list
total_months = 0
net_total = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_month_increase = 0
greatest_decrease = 0
greatest_month_decrease = 0

csvpath = os.path.join('..',  'resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:

   csvreader = csv.reader(csvfile, delimiter=',')
   csv_header = next(csvreader)
   row = next(csvreader)
   
   previous_row = int(row[1])
   total_months += 1  
   net_total += int(row[1])
   greatest_increase = int(row[1])
   greatest_month_increase = row[0]

   for row in csvreader:
      #The total number of months included in the dataset
      total_months += 1
      #The net total amount of "Profit/Losses" over the entire period
      net_total += int(row[1])
      #The average of the changes in "Profit/Losses" over the entire period
      profit_change = int(row[1]) - previous_row
      monthly_change.append(profit_change)
      previous_row = int(row[1])
      month_count.append(row[0])
      #The greatest increase in profits (date and amount) over the entire period
      if int(row[1]) > greatest_increase:
         greatest_increase = int(row[1])
         greatest_month_increase = row[0]
      #The greatest decrease in losses (date and amount) over the entire period
      if int(row[1]) < greatest_increase:
         greatest_decrease = int(row[1])
         greatest_month_decrease = row[0]
      
      average_change = sum(monthly_change) / len(monthly_change)
      highest = max(monthly_change)
      lowest = min(monthly_change)
      
   

#Final Analysis
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(net_total))
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_month_increase}, (${highest})")
print(f"Greatest Decrease in Profits:, {greatest_month_decrease}, (${lowest})")

output_file = os.path.join('..', 'analysis', 'Financial_Analysis.text')
with open(output_file, 'w',) as txtfile:
   txtfile.write(f"Financial Analysis\n")
   txtfile.write(f"----------------------------\n")
   txtfile.write(f"Total Months: {total_months}\n")
   txtfile.write(f"Total: ${net_total}\n")
   txtfile.write(f"Average Change: ${average_change:.2f}\n")
   txtfile.write(f"Greatest Increase in Profits:, {greatest_month_increase}, (${highest})\n")
   txtfile.write(f"Greatest Decrease in Profits:, {greatest_month_decrease}, (${lowest})\n")