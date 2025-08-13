'''
# Not a siding window concept but base for binary subarrays with sum 

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107


'''

class Solution:
      def subarraySum(self, nums: list[int], k: int) -> int:
          count,n=0,len(nums)
          for i in range(n):
              sum=0
              for j in range(i,n):
                  sum+=nums[j]
                  if sum==k:
                      count+=1
          return count
from collections import defaultdict 
class Solution:
      def subarraySum(self, nums: list[int], k: int) -> int:
          hash_map=defaultdict(int)
          hash_map[0]=1
          n=len(nums)
          count=right=prefix_sum=0 
          while right<n:
                prefix_sum+=nums[right]
                curr=prefix_sum-k 
                if curr in hash_map:
                    count+=hash_map[curr]
                hash_map[prefix_sum]+=1
                right+=1
          return count
class TestApp:
      def testing_case_one(self):
          assert Solution().subarraySum([1,1,1],2)==2 
      def testing_case_two(self):
          assert Solution().subarraySum([1,2,3],3)==2
      def testing_case_three(self):
          assert Solution().subarraySum([1,2,3,-3,1,1,1,4,2,-3],3)==8