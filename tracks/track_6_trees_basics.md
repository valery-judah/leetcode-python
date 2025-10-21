# Trees — Traversals, BST Properties, and LCA

Track: `track_6_trees_basics`

Postorder "return tuple" thinking, BFS levels, inorder/BST invariants, and LCA patterns.

See generation instructions in ../README.md.

## Problems

| Problem&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Diff | Baseline | Complex Justified | Optimal | Repeats | Min Time | Conf | Clarified | Communicated | Stated | Edge Tests | Clean Impl | Mistakes |
|:---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [Maximum Depth of Binary Tree](../problems/0104-maximum-depth-of-binary-tree/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Easy | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [Invert Binary Tree](../problems/0226-invert-binary-tree/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Easy | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [Balanced Binary Tree](../problems/0110-balanced-binary-tree/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Easy | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [Diameter of Binary Tree](../problems/0543-diameter-of-binary-tree/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Easy | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [Same Tree](../problems/0100-same-tree/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Easy | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [Symmetric Tree](../problems/0101-symmetric-tree/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Easy | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [Subtree of Another Tree](../problems/0572-subtree-of-another-tree/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Easy | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [Path Sum](../problems/0112-path-sum/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Easy | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [Binary Tree Level Order Traversal](../problems/0102-binary-tree-level-order-traversal/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [Binary Tree Right Side View](../problems/0199-binary-tree-right-side-view/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [Validate Binary Search Tree](../problems/0098-validate-binary-search-tree/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [Kth Smallest Element in a BST](../problems/0230-kth-smallest-element-in-a-bst/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [Lowest Common Ancestor of a BST](../problems/0235-lowest-common-ancestor-of-a-binary-search-tree/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Easy | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [Lowest Common Ancestor of a Binary Tree](../problems/0236-lowest-common-ancestor-of-a-binary-tree/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |


## Extensions (Optional)

| Problem&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Diff | Baseline | Complex Justified | Optimal | Repeats | Min Time | Conf | Clarified | Communicated | Stated | Edge Tests | Clean Impl | Mistakes |
|:---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [Binary Tree Inorder Traversal](../problems/0094-binary-tree-inorder-traversal/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Easy | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [Binary Tree Zigzag Level Order Traversal](../problems/0103-binary-tree-zigzag-level-order-traversal/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [Binary Tree Level Order Traversal II](../problems/0107-binary-tree-level-order-traversal-ii/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [Construct Binary Tree from Preorder and Inorder Traversal](../problems/0105-construct-binary-tree-from-preorder-and-inorder-traversal/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [Construct Binary Tree from Inorder and Postorder Traversal](../problems/0106-construct-binary-tree-from-inorder-and-postorder-traversal/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [Serialize and Deserialize Binary Tree](../problems/0297-serialize-and-deserialize-binary-tree/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Hard | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [Flatten Binary Tree to Linked List](../problems/0114-flatten-binary-tree-to-linked-list/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [Binary Tree Maximum Path Sum](../problems/0124-binary-tree-maximum-path-sum/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Hard | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [Range Sum of BST](../problems/0938-range-sum-of-bst/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Easy | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [BST Iterator](../problems/0173-binary-search-tree-iterator/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [Delete Node in a BST](../problems/0450-delete-node-in-a-bst/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
