#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

#Example 1:
#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

class Two:

    @staticmethod
    def two_sum( array, target):


        for i in range(len(array)):
            j = i+1
            while j <len(array):
                print(j, i)
                if array[i]+array[j] == target:
                    return [i,j]
                j += 1

        return [0,0]







new = Two()
print(new.two_sum([1,2,3,4,5], 9))






