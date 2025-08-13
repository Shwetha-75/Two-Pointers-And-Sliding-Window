'''

Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

 

Example 1:

Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
Example 2:

Input: nums = [0,0,0,0,0], goal = 0
Output: 15
 

Constraints:

1 <= nums.length <= 3 * 104
nums[i] is either 0 or 1.
0 <= goal <= nums.length

'''

class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        count,n=0,len(nums)
        for i in range(n):
            sum=0
            for j in range(i,n):
                sum+=nums[j]
                if sum==goal:
                    count+=1
        return count 
from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        n=len(nums)
        count=prefix_sum=0
        hash_map=defaultdict(int)
        hash_map[0]=1
        for i in range(n):
            prefix_sum+=nums[i]
            curr=prefix_sum-goal 
            if curr in hash_map:
                count+=hash_map[curr]
            hash_map[prefix_sum]+=1
        return count
class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        return self.countOfSubArrays(nums,goal)-self.countOfSubArrays(nums,goal-1)
    def countOfSubArrays(self,nums:list[int],k:int):
        if k<0:
            return 0
        left=right=count=sum=0 
        n=len(nums)
        while right<n:
              sum+=nums[right]
              while sum>k:
                    sum-=nums[left]
                    left+=1
              count+=right-left+1
              right+=1
        return count 
                         


    
class TestApp:
    
      def testing_case_one(self):
          assert Solution().numSubarraysWithSum([1,0,1,0,1],2)==4
      def testing_case_two(self):
          assert Solution().numSubarraysWithSum([0,0,0,0,0],0)==15 
    