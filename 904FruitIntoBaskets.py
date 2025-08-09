'''

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

 

Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
 

Constraints:

1 <= fruits.length <= 105
0 <= fruits[i] < fruits.length

'''

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        max_len=0
        n=len(fruits)
        for i in range(n):
            arr=set()
            for j in range(i,n):
                arr.add(fruits[j])
                if len(arr)<=2:
                    max_len=max(max_len,j-i+1)
                else:
                    break 
        return max_len 
from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        max_len,n=0,len(fruits)
        hash_map=defaultdict(int)
        left=right=0 
        while right<n:
             hash_map[fruits[right]]+=1
             while len(hash_map)>2:
                  hash_map[fruits[left]]-=1
                  if hash_map[fruits[left]]==0:
                      del hash_map[fruits[left]]
                  left+=1
             max_len=max(max_len,right-left+1)
             right+=1
        return max_len
        
class Solution:
      def totalFruit(self, fruits: list[int]) -> int:
          max_len,n=0,len(fruits)
          left=right=0
          hash_map=defaultdict(int)
          while right<n:
              hash_map[fruits[right]]+=1
              if len(hash_map)>2:
                  hash_map[fruits[left]]-=1
                  if hash_map[fruits[left]]==0:
                      del hash_map[fruits[left]]
                  left+=1
              max_len=max(max_len,right-left+1)
              right+=1
          return max_len 
 
    
class TestApp:
      def testing_case_one(self):
          assert Solution().totalFruit([1,2,1])==3
      def testing_case_two(self):
          assert Solution().totalFruit([1,2,3,2,2])==4
      def testing_case_three(self):
          assert Solution().totalFruit([0,1,2,2])==3