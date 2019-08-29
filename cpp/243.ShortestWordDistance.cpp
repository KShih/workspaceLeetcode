/*
  We can optimize our solution with only one for-loop,
  To do so, we can't memorize the index of each matching words,
  instead we should calculate the min distance when we walk through the array.

  We need two value to calculate the min distance, but we can use "i" as one value.
  therefore, we just need to allocate one other variable idx.
*/

class Solution {
public:
    int shortestDistance(vector<string>& words, string word1, string word2) {
        int idx = -1, res = INT_MAX;
        for (int i=0; i < words.size(); i++){
          if (words[i] == word1 || words[i] == word2){
            if (idx != -1 && words[i] != words[idx]){
              res = min(res, i - idx );
            }
            idx = i; // update the idx fowardly
          }
        }
        return res;
    }
};
