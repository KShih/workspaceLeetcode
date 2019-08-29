/*
  We should use the Greedy's opinion to solve this question.
  Predict the farthest destination this step can be (if not reach the goal).
  Then calculate if there is opportunity to goal in next step between the last farthest step to this farthest step.
  If there is, then the solution is don't go that far in this step, shorten it then move with the goal process.
  If there is not, we still can find the farthest position we can reach.
*/

class Solution {

public:
  int jump (vector<int>& nums){
    int n = nums.size(), i = 0, res = 0, cur = 0;
    while (i < n-1){
      res ++;
      int pre = cur;
      for (;i <= pre; i++){
        cur = max(cur, i+nums[i]);
        if (cur >= n-1){
          return res;
        }
      }
    }
    return res;
  }
}
