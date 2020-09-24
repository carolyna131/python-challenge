#Import the file and file path
import os
import csv

# Path to collect data from the Resources folder
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

#Print csv to look at the data
with open(budget_data_csv) as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  next(csvreader)

# prepare lists
  months = []
  revenue = []
  revenue_change_values = []
  avg_change = []

#In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company.

# Loop through the data
  for row in csvreader:
    #insert csv values into lists
    months.append(row[0])
    revenue.append(row[1])
  
  #Calculate The total number of months included in the dataset
  total_months = len(months)

  #The net total amount of "Profit/Losses" over the entire period
  revenue_int = map(int,revenue)
  total_revenue = '${:}'.format(sum(revenue_int))
  
    
  #The loop through the data set to calculate average of the changes in "Profit/Losses" over the entire period
  i = 0
  for i in range(len(revenue) -1):
    profit_loss = int(revenue[i+1]) - int(revenue[i])
    revenue_change_values.append(profit_loss)

  #calculate average change  
  total = sum(revenue_change_values)
  avg_change = total / len(revenue_change_values)

  #format monthly_change to include $ sign, commas, and cents
  avg_change = '${:.2f}'.format(avg_change)

#The greatest increase in profits (date and amount) over the entire period
  profit_increase = max(revenue_change_values)
  j = revenue_change_values.index(profit_increase)
  month_increase = months [j+1]
  max_val = '${:}'.format(max(revenue_change_values))
  
 #The greatest decrease in losses (date and amount) over the entire period
  profit_decrease = min(revenue_change_values)
  k = revenue_change_values.index(profit_decrease)
  month_decrease = months [k+1]
  min_val = '${:}'.format(min(revenue_change_values))


  #Print Analysis Results
print('Financial Analysis')
print('_------------------------------')
print(f'Total Months: ', total_months)
print(f'Total: ',total_revenue)
print(f'Average Change: ', avg_change)
print(f'Greatest Increase in Profits: ', month_increase,'('+max_val+')')
print(f'Greatest Decrease in Profits: ', month_decrease, '('+min_val+')')

#output analysis to file
output_path = os.path.join("..","Analysis", 'analysis.txt')

#Open the file using "write" mode. Specify the variable to hold the contents
with open('analysis.txt', 'w') as text:
  text.write("Financial Analysis\n")
  text.write("------------------------------\n")
  text.write("Total Months: " + str(total_months)+"\n")
  text.write("Total: " + str(total_revenue)+"\n")
  text.write("Average Change: " + str(avg_change)+"\n")
  text.write("Greatest Increase in Profits: " + str(month_increase) + "("+str(max_val)+")"+"\n")
  text.write("Greatest Decrease in Profits: " + str(month_decrease) + "("+str(min_val)+")"+"\n")
