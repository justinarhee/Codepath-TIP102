from collections import deque 
# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)
def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root
'''
Problem 1: Monstera Madness
Given the root of a binary tree where each node represents the number of splits in a leaf of a Monstera plant,
return the number of Monstera leaves that have an odd number of splits.

Evaluate the time complexity of your function

Understand
- given: root node of binary tree
- return: int val of the number of monstera leaves that have odd values
Match: binary tree recursion

Plan:
- if the root is none, return 0
- total_count = count_odd_splits(left and right)
- if root.val is odd: total_count+=1
- return total_count

'''
         
# def count_odd_splits(root):
#     if not root:
#         return 0
#     total = count_odd_splits(root.right)+count_odd_splits(root.left)
#     if root.val%2 == 1:
#         total+=1
#     return total

# values = [2, 3, 5, 6, 7, None, 12]
# monstera = build_tree(values)

# print(count_odd_splits(monstera))
# print(count_odd_splits(None))
# # Evaluate:
# # Time complexity: O(n)
# # Space complexity: O(n)
'''
Problem 2: Flower Finding
You are looking to buy a new flower plant for your garden. 
The nursery you visit stores its inventory in a binary search tree (BST) where each node represents a plant in the store. 
The plants are organized according to their names (vals) in alphabetical order in the BST.

Given the root of the binary search tree inventory and a target flower name, 
write a function find_flower() that returns True if the flower is present in the garden and False otherwise.

Evaluate the time complexity of your function. 
Define your variables and provide a rationale for why you believe your solution has the stated time complexity. 
Assume the input tree is balanced when calculating time complexity.

- Understand: 
    input: BST of flower names, flower name
    output: boolean

    goal: write a function that will find a flower based on the name

- Plan:
    - if root is None, return False
    - if name == root.val, return True
    - if name if greater than root.val, return  find_flower(root.right, flower)
    - if name is less than root.val, return find_flower(root.left, flower)

'''

# def find_flower(inventory, name):
#     if inventory is None :
#         return False
#     if name == inventory.val:
#         return True
#     elif name > inventory.val:
#         return find_flower(inventory.right, name)
#     else:
#         return find_flower(inventory.left,name)

# """
#           Rose
#          /    \
#       Lilac  Tulip
#       /  \       \
#    Daisy Lily   Violet
# """

# # using build_tree() function at top of page
# values = ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"]
# garden = build_tree(values)
# print(find_flower(garden, "Lilac"))  
# print(find_flower(garden, "Sunflower"))

# #Review
# #Time Complexity: O(logn)
# #Space Complexity: O(logn)

'''
Problem 3: Flower Finding II
Consider the following function non_bst_find_flower() which accepts the root of a binary tree inventory and a flower name, 
and returns True if a flower (node) with name exists in the binary tree. Unlike the previous problem, this tree is not a binary search tree.

Compare your solution to find_flower() in Problem 2 to the following solution. Discuss with your group: How is the code different? Why?
What is the time complexity of non_bst_find_flower()? How does it compare to the time complexity of find_flower() in Problem 2?
How would the time complexity of find_flower() from Problem 2 change if the tree inventory was not balanced?
'''

# def non_bst_find_flower(root, name):
#     if root is None:
#         return False
    
#     if root.val == name:
#         return True

#     return non_bst_find_flower(root.left, name) or non_bst_find_flower(root.right, name)

# """
#          Daisy
#         /    \
#       Lily   Tulip
#      /  \       \
#   Rose  Violet  Lilac
# """

# # using build_tree() function at top of page
# values = ["Rose", "Lily", "Tulip", "Daisy", "Lilac", None, "Violet"]
# garden = build_tree(values)
# print(non_bst_find_flower(garden, "Lilac"))  
# print(non_bst_find_flower(garden, "Sunflower"))  

# #Time Complexity: O(n)

'''
Problem 4: Adding a New Plant to the Collection
You have just purchased a new houseplant and are excited to add it to your collection! 
Your collection is meticulously organized using a Binary Search Tree (BST) where each node in the tree represents a houseplant in your collection,
and houseplants are organized alphabetically by name (val).

Given the root of your BST collection and a new houseplant name, insert a new node with value name into your collection. 
Return the root of your updated collection. If another plant with name already exists in the tree, 
add the new node in the existing node's right subtree.

Evaluate the time complexity of your function. 
Define your variables and provide a rationale for why you believe your solution has the stated time complexity. 
Assume the input tree is balanced when calculating time complexity.

Understand
- given: root of binary search tree, string name of node value we want to add
- return: root of the new bst

edge cases: if root is None: new Node must be root

Plan
- if root is None, return new node with name as value
- if name < root.val:
    if root.left:
        add_plant(left tree)
    root.left = add_plant(left tree)
-if name > root.val:
    if root.right:
        add_plant(right tree)
    root.right = add_plant(right tree)
- return root
'''

def add_plant(collection, name):
    pass

"""
            Money Tree
        /              \
Fiddle Leaf Fig    Snake Plant
"""

# Using build_tree() function at the top of page
values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant"]
collection = build_tree(values)
# Using print_tree() function at the top of page
print_tree(add_plant(collection, "Aloe"))
