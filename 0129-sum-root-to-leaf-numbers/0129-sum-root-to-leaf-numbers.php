/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     public $val = 0;
 *     public $left = null;
 *     public $right = null;
 *     function __construct($val = 0, $left = null, $right = null) {
 *         $this->val = $val;
 *         $this->left = $left;
 *         $this->right = $right;
 *     }
 * }
 */

class Solution {

    function sumNumbers($root) {
        return $this->dfs($root, 0);
    }

    function dfs($node, $current) {
        if ($node == null) {
            return 0;
        }

        $current = $current * 10 + $node->val;

        // Leaf node
        if ($node->left == null && $node->right == null) {
            return $current;
        }

        return $this->dfs($node->left, $current) +
               $this->dfs($node->right, $current);
    }
}