'''

You are given a string s consisting only lowercase alphabets and an integer k. 
Your task is to find the length of the longest substring that contains exactly 
k distinct characters.

Note : If no such substring exists, return -1. 

Examples:

Input: s = "aabacbebebe", k = 3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
Output: 7
Explanation: The longest substring with exactly 3 distinct characters is "cbebebe", which includes 'c', 'b', and 'e'.
Input: s = "aaaa", k = 2
Output: -1
Explanation: There's no substring with 2 distinct characters.
Input: s = "aabaaab", k = 2
Output: 7
Explanation: The entire string "aabaaab" has exactly 2 unique characters 'a' and 'b', making it the longest valid substring.
Constraints:
1 ≤ s.size() ≤ 105
1 ≤ k ≤ 26



'''

from collections import defaultdict
class Solution:
      def longestKSubstr(self, s:str, k:str):
          max_len=-1
          n=len(s)
          for i in range(n):
              hash_map=defaultdict(int)
              for j in range(i,n):
                  hash_map[s[j]]+=1
                  if len(hash_map)==k:
                      max_len=max(max_len,j-i+1)
          return max_len
class Solution:
      def longestKSubstr(self, s:str, k:str):
          left=right=0 
          n,max_len=len(s),-1
          hash_map=defaultdict(int)
          while right<n:
              while len(hash_map)>k:
                    hash_map[s[left]]-=1
                    if hash_map[s[left]]==0:
                        del hash_map[s[left]]
                    left+=1
              hash_map[s[right]]+=1
              if len(hash_map)==k:
                  print(hash_map)
                  max_len=max(max_len,right-left+1)
              right+=1
          return max_len
   
class Solution:
      def longestKSubstr(self, s:str, k:str):
          max_len,n=-1,len(s)
          left=right=0 
          hash_map=defaultdict(int)
          while right<n:
                if len(hash_map)>k:
                    hash_map[s[left]]-=1
                    if hash_map[s[left]]==0:
                        del hash_map[s[left]]
                    left+=1
            
                hash_map[s[right]]+=1
                if len(hash_map)==k:
                    max_len=max(max_len,right-left+1)
                right+=1
          return max_len
           
class TestApp:
      def testing_case_one(self):
          assert Solution().longestKSubstr("aabacbebebe",3)==7 
      def testing_case_two(self):
          assert Solution().longestKSubstr("aaaaa",2)==-1
      def testing_case_three(self):
          assert Solution().longestKSubstr("aabaaab",2)==7