'''

Given an integer array nums and an integer k, return the number of good 
subarrays of nums.

A good array is an array where the number of different integers
in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
Example 2:

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
 

Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i], k <= nums.length

'''

from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        count=0
        n=len(nums)
        for i in range(n):
            hash_map=defaultdict(int)
            for j in range(i,n):
                hash_map[nums[j]]+=1
                if len(hash_map)==k:
                    count+=1
        return count 
class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        return self.countSubarrays(nums,k)-self.countSubarrays(nums,k-1)
        pass
    def countSubarrays(self,nums:list[int],k:int):
        count=left=right=0
        n=len(nums)
        hash_map=defaultdict(int)
        while right<n:
              hash_map[nums[right]]+=1
              while len(hash_map)>k:
                    hash_map[nums[left]]-=1
                    if hash_map[nums[left]]==0:
                        del hash_map[nums[left]]
                    left+=1
              count+=right-left+1
              right+=1
        return count
class TestApp:
      def testing_case_one(self):
          assert Solution().subarraysWithKDistinct([1,2,1,2,3],2)==7 
      def testing_case_two(self):
          assert Solution().subarraysWithKDistinct([1,2,1,3,4],3)==3 
