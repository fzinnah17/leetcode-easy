#Ques: The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
# Given two integers x and y, return the Hamming distance between them.

class Solution(object):
    def hammingDistance(self, x, y):
        
        x = format(x, '0b')
        y = format(y, '0b')
        
        short = max(len(x),len(y))
          
        x = x.zfill(short)
        
        y = y.zfill(short)
        count = 0
        
        for valOne, valTwo in zip(x,y):
            if valOne is not valTwo:
                count += 1

        return count