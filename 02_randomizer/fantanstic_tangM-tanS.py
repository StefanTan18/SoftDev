#fanTANstic -- Stefan Tan & Michelle Tang
#SoftDev1 pd6
#K02 -- NO-body expects the Spanish Inquisition!
#2018-09-07  

import random

KREWES = {

        'w': ['William Lu', 'Qian', 'Peter', 'Ahnaf', 'Kenny', 'Sophia', 'Sajed', 'Emily', 'Hasif', 'Brian ', 'Dennis', 'Jiayang', 'Shafali ', 'Isaac ', 'Tania', 'Derek', 'Shin', 'Vincent', 'Ricky', 'Puneet', 'Wei Wen', 'Tim', 'Jeffrey', 'Joyce ', 'Mohtasim', 'Simon', 'Thomas', 'Ray', 'Jack', 'Karen', 'Robin', 'Jabir', 'Johnny ', 'Matthew', 'Johnson Li', 'Angela', 'Crystal', 'Jiajie', 'Theodore (Don\'t really care)', 'Anton', 'Max', 'Bo', 'Andrew', 'Kendrick', 'Kevin', 'Kyle', 'Jamil', 'Mohammed', 'Ryan', 'Jason'],

        'm': ['Daniel', 'Aleksandra', 'Addison', 'Hui Min', 'Aaron', 'Rubin', 'Raunak', 'Stefan', 'Cheryl', 'Cathy', 'Mai', 'Claire ', 'Alex', 'Bill', 'Daniel', 'Jason'],

        'x': ['Derek', 'Britni', 'Joan', 'Vincent', 'Jared', 'Ivan', 'Thomas', 'Maggie', 'Damian', 'Tina', 'Fabiha', 'John', 'Susan ', 'Kaitlin', 'Michelle', 'Clara', 'Rachel', 'Amit', 'Jerry', 'Raymond', 'Zane', 'Soojin', 'Maryann', 'Adil', 'Josh', 'Imad']

}

#Asks user to choose a team to have a randomly-selected student
team = input("Choose a team ('w', 'm', 'x'): ")

#Pre-condition: User has provided a letter through input
#Post-condition: A random member on the team  selected, if the team exists, has been returned.
def randomTeam():
        #If user enters a team name that does not exist, return error message
	if team != 'w' and team != 'm' and team != 'x':
		return ("Team " + team + " does not exist")
	list = KREWES[team]
	#generates random index 
	index= random.randint(0,len(list))
	#returns value at the random index
	return list[index]

#Prints the returned value  
print (randomTeam())
