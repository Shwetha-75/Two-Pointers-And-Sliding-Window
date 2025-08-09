'''

Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

'''
# Brute Force approach 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0
        n=len(s)
        for i in range(n):
            for j in range(i,n):
                if self.checkRepeatedCharacters(s[i:j+1:]):
                    max_len=max(max_len,j-i+1)
        return max_len 
    def checkRepeatedCharacters(self,string:str):
        hash_map={}
        for char in string:
            if char in hash_map:
                return False
            hash_map[char]=1
        return True
# Sliding window with while loop
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map={}
        left=right=max_len=0
        n=len(s)
        while right<n:
              
              while s[right] in hash_map:
                    del hash_map[s[left]]
                    left+=1
              hash_map[s[right]]=1
              max_len=max(max_len,right-left+1)    
              right+=1
        return max_len
# sliding window without while loop, hashmap=[key,value]=[character,index]
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map={}
        left=right=max_len=0
        n=len(s)
        while right<n:
              if s[right] in hash_map and hash_map[s[right]]>=left:
                  left=hash_map[s[right]]+1
              hash_map[s[right]]=right
              max_len=max(max_len,right-left+1)    
              right+=1
        return max_len  
        
class TestApp:
      def testing_case_one(self):
          assert Solution().lengthOfLongestSubstring("abcabcbb")==3 
      def testing_case_two(self):
          assert Solution().lengthOfLongestSubstring("bbbbb")==1
      def testing_case_three(self):
          assert Solution().lengthOfLongestSubstring("pwwkew")==3
      def testing_case_four(self):
          assert Solution().lengthOfLongestSubstring("abba")==2
