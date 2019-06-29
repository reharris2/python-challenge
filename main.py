# Import the os module
import os

# Import the csv module
import csv

#Import the statistics module
import statistics

total_months=0
total_profit=0
csv_values=[]
date=[]
date=0


csvpath = os.path.join("budget_data.csv")

with open(csvpath, 'r', newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

# calculate the number of months in the dataset
    
    for row in csvreader:
        total_months+=1
    
  
# calculate the net total amount of "profit/losses" over the entire period

with open(csvpath, 'r', newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    numbers=(int(row[1]) for row in csvreader)
    total=sum(numbers)
   

with open(csvpath, 'r', newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        csv_values.append(list(row))
          


# add average change between each month column

with open(csvpath, 'w', newline='') as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=",")

# add new header row
    del csv_values[0]
    csvwriter.writerow(['Date','Profit/Losses','Avg Change'])

    i = 0

    for row in csv_values:
        
        if i == 0:
            avg_change = 0
        else:
            avg_change = int(csv_values[i][1]) - int(csv_values[i-1][1]) 

        csvwriter.writerow([csv_values[i][0], csv_values[i][1], avg_change])

        i+=1

# calculate the average of the changes over the entire period

with open(csvpath, 'r', newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    delta=(float(row[2]) for row in csvreader)
    avg_change=round(statistics.mean(delta),2)
    
# The greatest increase in profits (date and amount) over the entire period

with open(csvpath, 'r', newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    price=(int(row[2]) for row in csvreader)
    great_increase=max(price)
        

# The greatest decrease in profits (date and amount) over the entire period

with open(csvpath, 'r', newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    loprice=(int(row[2]) for row in csvreader)
    great_decrease=min(loprice)
     
with open(csvpath, 'r', newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        if str(great_decrease) in row:
            great_decrease_date = row[0]
        if str(great_increase) in row:
            great_increase_date = row[0]

#Export a text file with the results
pybank_results = (
    " \n"
    "Financial Analysis\n"
    " \n"
    "--------------------------------------------------------------------\n"
    " \n"
    f'Total Months:{total_months}\n'
    f'Total:{total}\n'
    f'Average Change:{avg_change}\n'
    f'Greatest Increase in Profits: {great_increase_date} {great_increase}\n'
    f'Greatest Decrease in Profits: {great_decrease_date} {great_decrease}\n')

print(pybank_results)

file_to_output = "pybank_results.txt"
with open(file_to_output,"w") as txt_file:
    txt_file.write(pybank_results)