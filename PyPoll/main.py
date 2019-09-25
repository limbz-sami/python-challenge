import csv 
file =open("Resources/election_data.csv")
datafile = csv.reader(file, delimiter=',')
Khan = 0
Correy = 0
Li = 0
Tooley = 0 
Total = 0
for row in datafile:
    Total = Total + 1
    if row[2] == "Khan":
        Khan = Khan + 1
    if row [2] == "Correy":
        Correy = Correy + 1
    if row [2] == "Li":
        Li = Li + 1
    if row [2] == "O'Tooley":
        Tooley =Tooley + 1
Khanpercent = "{0:.3%}".format(Khan/Total)
Correypercent ="{0:.3%}".format(Correy/Total)
Lipercent = "{0:.3%}".format(Li/Total)
Tooleypercent = "{0:.3%}".format(Tooley/Total)
print('Election Results')
print('----------------------------')
print(F'Total Votes:{Total}')
print('----------------------------')
print(F'Khan: {Khanpercent} ({Khan})')
print(F'Correy: {Correypercent} ({Correy})')
print(F'Li: {Lipercent} ({Li})')
print("O'Tooley:"F'{Tooleypercent} ({Tooley})')
print('-------------------------------')

if Khan > Correy and Khan > Li and Khan > Tooley:
    print('Winner: Khan')
elif Correy > Khan and Correy >Li and Correy > Tooley:
    print ('Winner: Correy')
elif Li > Khan and Li > Correy and Li > Tooley:
    print('Winner Li')
else:
    print('Winner Tooley')
print('----------------------------------')
