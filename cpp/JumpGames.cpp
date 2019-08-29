/*
  We care about the farlest distance we can reach,
  and the goal distance is the size-1,
  We keep checking if we reach the goal in every iteration,
  we can stop looping if 1. we reach the goal, or 2. we can't move.
  we keep updating the farthest position in every iteration.
*/

class Solution {

public:
  bool canJump (vector<int>& nums){
    int n = nums.size(), reach = 0; // the goal and our progress
    for (int i=0; i < n; i++){
      if (i > reach || reach >= n-1) break;
      else{
        reach = max(reach, i+nums[i]);
      }
    }
    return reach >= n-1;
  }
}
