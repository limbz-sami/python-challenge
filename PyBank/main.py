import csv
file = open("resources/budget_data.csv")
datafile = csv.reader(file, delimiter=',')
header = next(datafile)
totalpfloss = 0
totalmonths = 0
previous = 0
change = 0
changes = []
months = []
for row in datafile:
    totalmonths = totalmonths + 1
    totalpfloss = totalpfloss + int(row[1])
    change = int(row[1])-previous
    previous = int(row[1])
    changes.append(change)
    months.append(row[0])
changes.remove(changes[0])
count= len(changes)
#print(count)
sum = 0 
for number in changes:
    sum = sum + number
average = round((sum/count),2)
#print(average)
greatest_profit_increase = max(changes)
#print(greatest_profit_increase)
greatest_loss = min(changes)
#print(greatest_loss)
greatest_index = changes.index(greatest_profit_increase)
losses_index = changes.index(greatest_loss)
months.remove(months[0])
#print(months[greatest_index])
#print(months[losses_index])
print("Financial Analysis")
print('---------------------------------')
print(F"Total Months : {totalmonths}")
print(F'Total : {totalpfloss}')
print(F'Average Change : {average}')
print(F'Greatest Increase in Profits : {(months[greatest_index])} ({greatest_profit_increase})')
print(F'Greatest decrease in Profits : {(months[losses_index])} ({(greatest_loss)})')