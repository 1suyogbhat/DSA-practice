class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #given an array nums we need to return a new array "output" that
        #output[i] is the product of all elements in nums, EXCEPT nums[i]

        #Input: nums = [1,2,4,6]
        #Output: [48,24,12,8]

        #brute force solution
        #make a new array
        #multiply all elements together in nums by looping through each one
        #take that number and divide it by i, which would mean all numbers but i contributed
        #i++
        #add that number to new array
        #start again
        #now i is incremented so do the same thing again and it should work
        #verify sizes are same (redundant)

        output = []
        res = 1
        for n in nums:
            res = res * n   #we have res
        for i in nums:
            output.append(res//i)
        
        return output

            
            

