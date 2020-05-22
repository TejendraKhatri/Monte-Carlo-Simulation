'''
Monte Carlo simulation to estimate the frequency 
of the different types of rolls of 5 5-sided dice
'''
__author__ = "Tejendra Khatri"
__date__ = "5/21/2020"

import random

class Roll:
    def __init__(self):
        self.__die = [0]*5              # what is the face value of each die
        self.__count = [0]*6            # how many of each face value
        self.__categoryCount = dict()   # how many occurances of each category
        self.__categoryCount['straight'] = 0
        self.__categoryCount['5ofakind'] = 0
        self.__categoryCount['4ofakind'] = 0
        self.__categoryCount['fullhouse'] = 0
        self.__categoryCount['3ofakind'] = 0
        self.__categoryCount['2pair'] = 0
        self.__categoryCount['pair'] = 0
        self.__categoryCount['unknown'] = 0    # this should remain 0

    def toss(self):
        self.__count = [0]*6            # zero the counters
        for d in range(len(self.__die)):
            roll = random.randint(1,5)
            self.__die[d] = roll        # save the face value
            self.__count[roll] += 1     # increment the count for that face value

    def __str__(self):
        self.__die.sort()
        return "%d %d %d %d %d" %(self.__die[0],self.__die[1],self.__die[2],self.__die[3],self.__die[4])

    def evaluate(self):
        '''
        what category of roll is this?
        increment the appropriate counter and return the category
        '''
        
        # you may want to add some code here
        category = 'unknown'
        tmpList = self.__die
        tmpList.sort()
        # replace False in the following statements with appropriate conditions
        if tmpList[0]<tmpList[1]<tmpList[2]<tmpList[3]<tmpList[4]:
            category = 'straight'
        elif tmpList[0]==tmpList[1]==tmpList[2]==tmpList[3]==tmpList[4]:
            category = '5ofakind'
        elif (tmpList[1]==tmpList[2]==tmpList[3]==tmpList[4]) or \
             (tmpList[0]==tmpList[1]==tmpList[2]==tmpList[3]):
            category = '4ofakind'
        elif ((tmpList[0]==tmpList[1]==tmpList[2])and(tmpList[3]==tmpList[4])) or \
             ((tmpList[2]==tmpList[3]==tmpList[4])and(tmpList[0]==tmpList[1])):
            category = 'fullhouse'
        elif (tmpList[0]==tmpList[1]==tmpList[2]) or \
             (tmpList[2]==tmpList[3]==tmpList[4]) or \
             (tmpList[1]==tmpList[2]==tmpList[3]):
            category = '3ofakind'
        elif ((tmpList[0]==tmpList[1])and(tmpList[2]==tmpList[3])) or\
             ((tmpList[0]==tmpList[1])and(tmpList[3]==tmpList[4])) or\
             ((tmpList[1]==tmpList[2])and(tmpList[3]==tmpList[4])):
            category = '2pair'
        elif (tmpList[0]==tmpList[1]) or \
              (tmpList[1]==tmpList[2]) or \
              (tmpList[2]==tmpList[3]) or \
              (tmpList[3]==tmpList[4]):
            category = 'pair'

        self.__categoryCount[category] += 1
        return category
        
    def printStats(self):
        for item in self.__categoryCount:
            print("%5d  %s"%(self.__categoryCount[item], item))
            
if __name__ == "__main__":
    trials = int(input("How many trials? "))
    random.seed()
    r = Roll()
    for trial in range(trials):
        r.toss()
        cat = r.evaluate()
        print(r, cat)
    
    r.printStats()
