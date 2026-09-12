/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

// if 
// if left not null, go left
// if right not null, go right
// return and reverse children

// if left smaller than root go left
// if left null && right not null go right
// reverse children



// if root null, return null
// if left smaller than right, revert node children
// return smaller node 

// class Solution {
//     public TreeNode invertTree(TreeNode root) {
//         if (root == null) {
//             return;
//         }
//         if (root.left.val < root.val){ // reverse children
//             int oldLeft = root.left.val;
//             root.left.val = root.right.val;
//             root.right.val = oldLeft;
//             return invertTree(root.left);
//         }
//         if (root.right.val )
//         return root;
//     }
// }

class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) {
            return null;
        }
        TreeNode left = invertTree(root.left);
        TreeNode right = invertTree(root.right);

        root.left = right;
        root.right = left;

        return root;
    }
}