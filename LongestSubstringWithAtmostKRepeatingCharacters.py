from collections import defaultdict
class Solution:
      def longestSubString(self,s:str,k:int)->int: 
          max_len,n=0,len(s)
          for i in range(n):
              hash_map=defaultdict(int)
              for j in range(i,n):
                  hash_map[s[j]]+=1
                  if len(hash_map)<=k:
                      max_len=max(max_len,j-i+1)
                  else:
                      break 
          return max_len 
class Solution:
      def longestSubString(self,s:str,k:int)->int: 
          max_len,n=0,len(s)
          hash_map=defaultdict(int)
          left=right=0
          while right<n:
                hash_map[s[right]]+=1
                while len(hash_map)>k:
                      hash_map[s[left]]-=1
                      if hash_map[s[left]]==0:
                          del hash_map[s[left]]
                      left+=1
                max_len=max(max_len,right-left+1)
                right+=1
          return max_len
class Solution:
      def longestSubString(self,s:str,k:int)->int: 
          max_len,n=0,len(s)
          hash_map=defaultdict(int)
          left=right=0
          while right<n:
                hash_map[s[right]]+=1
                if len(hash_map)>k:
                      hash_map[s[left]]-=1
                      if hash_map[s[left]]==0:
                          del hash_map[s[left]]
                      left+=1
                max_len=max(max_len,right-left+1)
                right+=1
          return max_len
class TestApp:
      def testing_case_one(self):
          assert Solution().longestSubString("aabacbebebe",2)==6 
      def testing_case_two(self):
          assert Solution().longestSubString("aabghhgyiioo",3)==5