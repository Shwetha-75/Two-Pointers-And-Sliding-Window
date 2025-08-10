'''

Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
Example 3:

Input: s = "abc"
Output: 1
 

Constraints:

3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.

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
