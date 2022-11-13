# Question: You are given a 0-indexed integer array nums. An index i is part of a hill in nums if the closest non-equal neighbors of i are smaller than nums[i]. Similarly, an index i is part of a valley in nums if the closest non-equal neighbors of i are larger than nums[i]. Adjacent indices i and j are part of the same hill or valley if nums[i] == nums[j].

# Note that for an index to be part of a hill or valley, it must have a non-equal neighbor on both the left and right of the index.

# Return the number of hills and valleys in nums.

def countHillValley(self, nums):
    #[5,7,7,1,7]
    hill = valley = 0
    for i in range(1,len(nums)-1):
        left = i-1
        right = i+1
        if nums[i] == nums[right]: #only if right value is same, then replace the current value with it's previous value
            #so, nums[1] = 5 when the code is checking nums[2] = 7 so that 5< 7 (left)  1 < 7 (right)
            nums[i] = nums[left]
        if nums[i] != nums[right]:
            if nums[i] > nums[left] and nums[i] > nums[right]:
                hill += 1
            if nums[i] < nums[left] and nums[i] < nums[right]:
                valley += 1
    ans = hill + valley
    return ans
    #TC: O(n) SC: O(1)