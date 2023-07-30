#python code to analyze profit/loss data 

# import module to create file paths
import os

# Module for read/write CSV files
import csv

file_path = '../Resources/budget_data.csv'

# lists to store data
Date = []
Profit_Loss = []


#Read in CSV 
with open(file_path) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)
        #add info in lists
        Date.append(row[0])
        Profit_Loss.append(row[1])


print(Date)
print("Financial Analysis  Total Months: " + str(len(Date)))
print(f"Total: $" + (sum(Profit_Loss[0]-[86])))


 
# function that returns the arithmetic average for a list of numbers
#def average(numbers):
 #   length = len(numbers)
 #   total = 0.0
 #   for number in numbers:
  #      total += number
  #  return total / length


# Test your function with the following:
#print(average([1, 5, 9]))
#print(average(range(11)))
#----------------------------------------------------------------


#----------------------------------------------------------------
#write to the output file
#output_path = r"C:\Users\kwlay\python-chall\PyBank\analysis\PyBank_results.csv"

#open the file using 'write' mode
#with open(output_path, 'w') as csvfile

  #initialize csv.writer
 # csvwriter = csv.writer(csvfile, delimiter=',')

