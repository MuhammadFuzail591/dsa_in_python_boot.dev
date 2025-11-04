# ref.py

from insert_nodes_l5 import BSTNode

def ref_implementation(bst_node: BSTNode, user):
   """Insert a user into the BST (reference correct solution)."""
   # If the current node has no value yet, assign the user.
   if bst_node.val is None:
      bst_node.val = user
      return

   # Compare and insert recursively.
   if user < bst_node.val:
      if bst_node.left is None:
         bst_node.left = BSTNode(user)
      else:
         ref_implementation(bst_node.left, user)
   elif user > bst_node.val:
      if bst_node.right is None:
         bst_node.right = BSTNode(user)
      else:
         ref_implementation(bst_node.right, user)
   # If equal (same id), we do nothing — duplicates not allowed.


def ref_inorder(bst_node: BSTNode, result: list):
   """Return an inorder traversal list of users (for comparison)."""
   if bst_node is None:
      return result
   ref_inorder(bst_node.left, result)
   if bst_node.val is not None:
      result.append(bst_node.val)
   ref_inorder(bst_node.right, result)
   return result
