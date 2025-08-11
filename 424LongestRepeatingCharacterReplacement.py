'''

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length

'''
from collections import defaultdict

# Brute Force Approach 
# time Complexity : O(N^2)
# Space Complexity : O(26)
class Solution:
        def characterReplacement(self, s: str, k: int) -> int:
            max_len,n=0,len(s)
            for i in range(n):
                hash_map=defaultdict(int)
                max_freq=0
                for j in range(i,n):
                    hash_map[s[j]]+=1
                    max_freq=max(max_freq,hash_map[s[j]])
                    if (j-i+1)-max_freq<=k:
                        max_len=max(max_len,j-i+1)
                    else:
                        break 
            return max_len
        
# Optimized approach using sliding window 
# Time Complexity : O((N+N)*26)
# Space Complexity : O(26)
class Solution:
      def characterReplacement(self, s: str, k: int) -> int:
            max_len,n=0,len(s)
            left=right=max_freq=0
            hash_map=defaultdict(int)
            while right<n:
                  hash_map[s[right]]+=1
                  max_freq=max(max_freq,hash_map[s[right]])
                  changes=(right-left+1)-max_freq
                  while changes>k:
                        hash_map[s[left]]-=1
                        if hash_map[s[left]]==0:
                            del hash_map[s[left]]
                        max_freq=max(hash_map.values())
                        left+=1
                        changes=(right-left+1)-max_freq
                  max_len=max(max_len,right-left+1)
                  right+=1
            return max_len
# Optimized Approach using Sliding window 
# Time Complexity : O(N)
# space Complexity : O(26)
class Solution:
      def characterReplacement(self, s: str, k: int) -> int:
            max_len,n=0,len(s)
            left=right=max_freq=0
            hash_map=defaultdict(int)
            while right<n:
                  hash_map[s[right]]+=1
                  max_freq=max(max_freq,hash_map[s[right]])
                  changes=(right-left+1)-max_freq
                  if changes>k:
                        hash_map[s[left]]-=1
                        if hash_map[s[left]]==0:
                            del hash_map[s[left]]
                        max_freq=0
                        left+=1
                  max_len=max(max_len,right-left+1)
                  right+=1
            return max_len      
 
class TestApp:
      def testing_case_one(self):
          assert Solution().characterReplacement("ABAB",2)==4
      def testing_case_two(self):
          assert Solution().characterReplacement("AABABBA",1)==4
      def testing_case_three(self):
          assert Solution().characterReplacement("AAABBCCD",2)==5
      def testing_case_four(self):
          assert Solution().characterReplacement("AAAAAAA",2)==7
      def testing_case_five(self):
          assert Solution().characterReplacement("BBBBBBBBC",0)==8