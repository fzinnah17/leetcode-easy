#Ques: A phrase is a palindrome if, after converting all uppercase letters 
# into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include 
# letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

#I solved it using iterative approach
class Solution:
    def isPalindrome(s):
        if not s:
            return True
        
        left, right = 0, len(s)-1
        while left < right:
            while not s[left].isalnum() and left<right:
                left += 1
            while not s[right].isalnum() and left<right:
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left, right = left+1, right-1
        return True

        #TC: O(n) and SC: O(1)
        