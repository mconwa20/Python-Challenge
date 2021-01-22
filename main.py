# imports
import os
import csv

# PYBANK PYBANK PYBANK PYBANK PYBANK

# budget_data.csv path

budget_data = os.path.join ('PyBank','Analysis', 'Resources', 'budget_data.csv')

# create empty lists
date = []
profit_loss = []

# read budget_data

with open(budget_data, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #convert column 2 to list
    for n, row in enumerate(csvreader):
        if not n: #skip header
            continue
        date.append(row[0])
        profit_loss.append(row[1])

# count number of months (ie rows)
row_count = sum(1 for row in csv.reader(open(os.path.join ('PyBank','Analysis', 'Resources', 'budget_data.csv')))) - 1
#print(row_count)

# converting profit_loss to a list of integers
for i in range(0, len(profit_loss)): 
    profit_loss[i] = int(profit_loss[i])
#print(profit_loss)

# sum of profit_loss
total = sum(profit_loss)
#print(total)

#average difference

difference_list = []

i = 1
for i in range(1, len(profit_loss)):
    difference = 0
    difference = profit_loss[i] - profit_loss[i - 1]
    difference_list.append(int(difference))
    i + 1
#print(difference_list)

# finding greatest increase in profits
maximum = max(difference_list)
maximum_formatted = "%.2f" % maximum
#print(maximum_formatted)

# finding greatest decrease in profits
minimum = min(difference_list)
minimum_formatted = "%.2f" % minimum
#print(minimum_formatted)

# average change
change = sum(difference_list)/(len(difference_list)-1)
change_formatted = "%.2f" % change
#print(change_formatted)

# print to terminal
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(row_count))
print("Total: $" + str(total))
print("Average Change: $ " + str(change_formatted))
print("Greatest Increase in Profits: " + "$" + str(maximum_formatted))
print("Greatest Decrease in Profits: " + "$" + str(minimum_formatted))

# WRITING OUTPUT.CSV

import csv

# save the output file path
output_file = os.path.join('PyBank', 'Analysis', 'output.csv')

# write to output.csv
with open(output_file, mode='w') as output:
    output_writer = csv.writer(output)

    output_writer.writerow(["Financial Analysis"])
    output_writer.writerow(["----------------------------"])
    output_writer.writerow(["Total Months: " + str(row_count)])
    output_writer.writerow(["Total: $" + str(total)])
    output_writer.writerow(["Average Change: $ " + str(change_formatted)])
    output_writer.writerow(["Greatest Increase in Profits: " + "$" + str(maximum_formatted)])
    output_writer.writerow(["Greatest Decrease in Profits: " + "$" + str(minimum_formatted) ])


#PYPOLL PYPOLL PYPOLL PYPOLL

# election_data.csv path

election_data = os.path.join ('PyPoll','Resources', 'election_data.csv')

# create empty lists

voter_id = []
county = []
candidate = []

#read election_data

with open(election_data, newline = '') as csvfile2:
    csvreader2 = csv.reader(csvfile2, delimiter=',')

    for b, row in enumerate(csvreader2):
        if not b: #skip header
            continue
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

#count number of votes

row_count2 = sum(1 for row in csv.reader(open(os.path.join ('PyPoll','Resources', 'election_data.csv')))) - 1
#print(row_count2)

#print unique candidates

unique_candidate = []
for x in candidate:
    if x not in unique_candidate:
        unique_candidate.append(x)
#print(unique_candidate)

# assign unique candidates

uckhan = unique_candidate[0]
uccorrey = unique_candidate[1]
ucli = unique_candidate[2]
uctooley = unique_candidate[3]

# stats for each candidate

khan = candidate.count('Khan')
khanperc = (khan / row_count2) * 100
khanperc_formatted = "%.3f" % khanperc
#print(khanperc_formatted)

correy = candidate.count('Correy')
correyperc = (correy / row_count2) * 100
correyperc_formatted = "%.3f" % correyperc
#print(correyperc_formatted)

tooley = candidate.count("O'Tooley")
tooleyperc = (tooley / row_count2) * 100
tooleyperc_formatted = "%.3f" % tooleyperc
#print(tooleyperc_formatted)

li = candidate.count('Li')
liperc = (li / row_count2) * 100
liperc_formatted = "%.3f" % liperc
#print(liperc_formatted)

# print to terminal

print("*******************************************")
print("Election Results")
print("----------------------------")
print("Total Votes: " + str(row_count2))
print("----------------------------")
print(uckhan + ": " + khanperc_formatted + "%  " + "(" + str(khan) + ")")
print(uccorrey + ": " + correyperc_formatted + "%  " + "(" + str(correy) + ")")
print(ucli + ": " + liperc_formatted + "%  " + "(" + str(li) + ")")
print(uctooley + ": " + tooleyperc_formatted + "%  " + "(" + str(tooley) + ")")
print("----------------------------")
print("Winner: " + uckhan)


# writing output2.csv

import csv

# save the output file path
output2_file = os.path.join('PyPoll', 'Analysis', 'output2.csv')

# write to output2
with open(output2_file, mode='w') as output:
    output2_writer = csv.writer(output)

    output2_writer.writerow(["*******************************************"])
    output2_writer.writerow(["Election Results"])
    output2_writer.writerow(["----------------------------"])
    output2_writer.writerow(["Total Votes: " + str(row_count2)])
    output2_writer.writerow(["----------------------------"])
    output2_writer.writerow([uckhan + ": " + khanperc_formatted + "%  " + "(" + str(khan) + ")"])
    output2_writer.writerow([uccorrey + ": " + correyperc_formatted + "%  " + "(" + str(correy) + ")"])
    output2_writer.writerow([ucli + ": " + liperc_formatted + "%  " + "(" + str(li) + ")"])
    output2_writer.writerow([uctooley + ": " + tooleyperc_formatted + "%  " + "(" + str(tooley) + ")"])
    output2_writer.writerow(["----------------------------"])
    output2_writer.writerow(["Winner: " + uckhan])
    
# done!