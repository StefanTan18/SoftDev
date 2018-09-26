'''
Team Track -- Addison Huang and Stefan Tan
SoftDev1 pd6
K10 -- Jinja Tuning
2018-09-21
'''

import csv, random

def occReader():
    reader = csv.reader(open('data/occupations.csv')) #opens and reads the csv file
    next(reader) # skips the headers
    d={} #intialized the dictionary
    for row in reader: #iterates through the csv file and updates the dictionary accordingly
        d[row[0]]=float(row[1])
    d.pop("Total")
    return d

def randomizer(dic):    
    occupations = list(dic.keys()) #makes a list of all the occupations
    percentages = list(dic.values()) #makes a list of all the occuaption
    result = random.choices(occupations, percentages)
    #returns a list of size 1 with a random occupation choosen based on the percentages
    return result.pop()
