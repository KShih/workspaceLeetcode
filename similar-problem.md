# Similar Problem

## Binary Tree Path Sum
### Questions
- LC112, LC113, LC437, LC124

1. LC112 Path Sum I
    1. 題目:
        - Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
    2. 分析:
        - 相對嚴格的條件從 root to leaf, 因此我們只需要維護一個 curSum 到 leaf 在判斷是否為 target 即可
    3. 解法:
        - 前序遍歷
2. LC113 Path Sum II
    1. 題目:
        - Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
    2. 分析:
        - 與上題一樣的條件，只是這題必須要求出所有路徑，因此只需要在上題的基礎上多維護一個 path arrays 去更新即可
    3. 解法:
        - 前序遍歷
3. LC437 Path Sum III
    1. 題目:
        - You are given a binary tree in which each node contains an integer value. Find the number of paths that sum to a given value. The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
    2. 分析:
        - 因為不需要從 root 開始 Naive 的作法是維護 path, 並且走到新的節點就把舊的節點一個一個扣掉，看是否有等於 target 的點，但這種作法需要一直重複加減太不高笑。可以使用 prefix sum dictionary，去紀錄該 accumulated sum 出現的次數，到了新的節點只需要求出加上此節點後跟 target 的差距，再去這個 dict 找出此 sum 的出現次數再加上去即可
    3. 解法:
        - 前序遍歷 + prefix sum
4. LC124 Binary Tree Maximum Path Sum
    1. 題目:
        - Given a non-empty binary tree, find the maximum path sum. For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.
    2. 分析:
        - 此題要求的就不是是否等於某個 target，而是此 tree 所能產生的最大值
        - 因此前序已經不適用於此了，因為左右邊的值會影響我們的選擇
    3. 解法:
        - 後序遍歷 + global max update
