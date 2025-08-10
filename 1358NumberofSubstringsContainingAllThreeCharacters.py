'''
Given a string s consisting only of characters a, b and c.
Return the number of substrings containing at least one occurrence of all 
these characters a, b and c.

 

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
    def numberOfSubstrings(self, s: str) -> int:
        n,count=len(s),0
        for i in range(n):
            hash_map=defaultdict(int)
            for j in range(i,n):
                hash_map[s[j]]+=1
                if len(hash_map)==3:
                    count+=1
        return count 

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n,count=len(s),0
        hash_map={'a':-1,'b':-1,'c':-1}
        for i in range(n):
            hash_map[s[i]]=i 
            if hash_map['a']!=-1 and hash_map['b']!=-1 and hash_map['c']!=-1:
                count+=min(hash_map['a'],hash_map['b'],hash_map['c'])+1
        return count

         
class TestApp:
      def testing_case_one(self):
          assert Solution().numberOfSubstrings("abcabc")==10 
      def testing_case_two(self):
          assert Solution().numberOfSubstrings("aaacb")==3 
      def testing_case_three(self):
          assert Solution().numberOfSubstrings("abc")==1