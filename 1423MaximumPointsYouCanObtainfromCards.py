'''

There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

 

Example 1:

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
Example 2:

Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.
Example 3:

Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.
 

Constraints:

1 <= cardPoints.length <= 105
1 <= cardPoints[i] <= 104
1 <= k <= cardPoints.length

'''

class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n=len(cardPoints)
        left,right=k-1,n-1 
        max_sum=current_sum=0
        for i in range(k):
            max_sum+=cardPoints[i]
            current_sum+=cardPoints[i]
        while left>=0:
              current_sum-=cardPoints[left]
              left-=1
              current_sum+=cardPoints[right]
              right-=1
              max_sum=max(max_sum,current_sum)
        return max_sum 
class TestApp:
    def testing_case_one(self):
        assert Solution().maxScore([1,2,3,4,5,6,1],3)==12 
    def testing_case_two(self):
        assert Solution().maxScore([2,2,2],2)==4 
    def testing_case_three(self):
        assert Solution().maxScore([9,7,7,9,7,7,9],7)==55   
        