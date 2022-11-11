#Question: You are given a 2D integer array logs where each logs[i] = [birthi, deathi] indicates the birth and death years of the ith person. The population of some year x is the number of people alive during that year. The ith person is counted in year x's population if x is in the inclusive range [birthi, deathi - 1]. Note that the person is not counted in the year that they die. Return the earliest year with the maximum population.

def maximumPopulation(self, logs):
    dates = []
    for birth, death in logs:
        dates.append((birth, 1))
        dates.append((death, -1))
    dates.sort()
    print(dates) #[(1993, 1), (1999, -1), (2000, 1), (2010, -1)] -> This is my year, change
    maxPop, currPop, earliestYear = 0,0,0
    for year, change in dates:
        currPop += change
        if currPop > maxPop:
            maxPop = max(maxPop,currPop)
            earliestYear = year
    return earliestYear
    
    #Idea: 
    #1. Create a hashMap to show the starting year means population increase by 1, ending year decreases by 1
    #2. Sorting helps to sort it based on the year
    #3. current population should be 1 more than previous to update the maximum
    #4. I can return the year

    #TC: O(n) SC: O(nlogn)
