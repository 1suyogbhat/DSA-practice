class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #given an array nums we need to return a new array "output" that
        #output[i] is the product of all elements in nums, EXCEPT nums[i]

        #Input: nums = [1,2,4,6]
        #Output: [48,24,12,8]

        #start from the left, if its ismultiplay each element together until i
        #so basically, if i is the next one

        output = []
        left = 1
        left_arr = []
        right_arr = [] 
        for n in nums:
            left_arr.append(left)
            left = left * n   #we have left res

        right = 1
        for i in range(len(nums) - 1, -1, -1):
            right_arr.append(right)
            right = right * nums[i]
        right_arr.reverse()

        for i in range(len(nums)):
            output.append(left_arr[i] * right_arr[i])

        return output

            
            
