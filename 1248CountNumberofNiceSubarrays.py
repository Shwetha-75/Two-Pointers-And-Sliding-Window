'''

Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

 

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
 

Constraints:

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length

'''
class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        count=0
        n=len(nums)
        for i  in range(n):
            sum=0
            for j in range(i,n):
                sum+=nums[j]%2
                if sum==k:
                    count+=1
        return count
class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        return self.countOfSubarrays(nums,k)-self.countOfSubarrays(nums,k-1)
    def countOfSubarrays(self,nums:list[int],k:int):
        right=left=count=sum=0
        n=len(nums)
        while right<n:
              sum+=nums[right]%2
              while sum>k:
                    sum-=nums[left]%2 
                    left+=1
              count+=right-left+1
              right+=1
        return count
              
class TestApp:
      def testing_case_one(self):
          assert Solution().numberOfSubarrays([1,1,2,1,1],3)==2
      def testing_case_two(self):
          assert Solution().numberOfSubarrays([2,4,6], 1)==0
      def testing_case_three(self):
          assert Solution().numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2)==16 