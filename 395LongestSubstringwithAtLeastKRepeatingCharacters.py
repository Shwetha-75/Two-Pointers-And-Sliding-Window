'''

Given a string s and an integer k, return the length of the longest 
substring of s such that the frequency of each character in this substring 
 is greater than or equal to k.

if no such substring exists, return 0.

 

Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
 

Constraints:

1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 105

'''
from collections import defaultdict
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        return self.helper(s,k)
    def helper(self,s:str,k:int):
        if not s:
            return 0 
        hash_map=defaultdict(int)
        for char in s:
            hash_map[char]+=1
        for i in range(len(s)):
            if hash_map[s[i]]<k:
               return max(self.helper(s[:i:],k),self.helper(s[i+1:],k))
        return len(s) 
class TestApp:
      def testing_case_one(self):
          assert Solution().longestSubstring("ababbc",2)==5 
      def testing_case_two(self):
          assert Solution().longestSubstring("aaabb",3)==3 
      def testing_case_three(self):
          assert Solution().longestSubstring("ababacb",5)==0
