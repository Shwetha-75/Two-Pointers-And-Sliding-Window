'''

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?

'''

import sys
from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_len=sys.maxsize 
        result=""
        n=len(s)
        for i in range(n):
            hash_map=defaultdict(int)
            for j in range(len(t)):
                hash_map[t[j]]+=1
            count=0
            for j in range(i,n):
                if hash_map[s[j]]>0:
                    count+=1
                hash_map[s[j]]-=1
                if count==len(t):
                   length=j-i+1
                   if length<min_len:
                       min_len=length 
                       result=s[i:j+1:]
        return result 
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count=left=right=0
        n,m=len(s),len(t)
        min_len=sys.maxsize 
        hash_map=defaultdict(int)
        result=""
        for char in t:
            hash_map[char]+=1
        while right<n:
            if hash_map[s[right]]>0:
                count+=1
            hash_map[s[right]]-=1
            while count==m:
                  if min_len>(right-left+1):
                      min_len=right-left+1
                      result=s[left:right+1]
                  hash_map[s[left]]+=1
                  if hash_map[s[left]]>0:
                      count-=1
                  left+=1
            right+=1
        return result
        
        
        
class TestApp:
      def testing_case_one(self):
          assert Solution().minWindow("ADOBECODEBANC","ABC")=="BANC"
      def testing_case_two(self):
          assert Solution().minWindow("a","a")=="a"
      def testing_case_three(self):
          assert Solution().minWindow("a","aa")==""
        