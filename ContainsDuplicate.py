# 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

#Example 1:
#Input: nums = [1,2,3,1]
#Output: true
#Explanation:
# The element 1 occurs at the indices 0 and 3.

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict_num = { }
        for i in nums:
            if i in dict_num:
                return True
            else:
                dict_num[i] = 0
        return False


new = Solution()
print(new.containsDuplicate([1,2,3]))