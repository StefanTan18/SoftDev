#Boomerang - Angela Tom & Stefan Tan
#SoftDev1 pd6
#K06 -- StI/O: Divine your Destiny!
#2018-09-13

import csv
import random


reader = csv.reader(open('occupations.csv')) #opens and reads the csv file
next(reader) # skips the headers
d={} #intialized the dictionary
for row in reader: #iterates through the csv file and updates the dictionary accordingly
    d[row[0]]=float(row[1])
d.pop('Total') # gets rid of the last row

#print(d) for testing

#Returns a randomly selected occupation where the results are weighted by the percentage given.
def selectRandOccupation(dic):
    occupations = list(dic.keys()) #makes a list of all the occupations
    percentages = list(dic.values()) #makes a list of all the occuaption
    result = random.choices(occupations, percentages)
    #returns a list of size 1 with a random occupation choosen based on the percentages
    print(occupations)
    print(percentages)
    return result.pop() #returns the only element in the list


print('The random occupation selected is... ' + selectRandOccupation(d))
