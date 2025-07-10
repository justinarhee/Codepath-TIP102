'''
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
If the two linked lists have no intersection at all, return null.
For example, the following two linked lists begin to intersect at node c1:

Understand
- given: two singly linked lists
- return: node (a node that is being pointed to by both of the lists, if else return None)

Happy case
Linked List A: 4 - 3- 2- 1
Linked List B: 6 - 5 - 3 - 2 - 1
Intersecting Node: 3

Edge case
Linked List A: 1 - 2 - 3
Linked List B: 4 - 5 - 6
Intersecting Node: None

1 - 2 - 3
3 - 4 - 5

1 - 2 - 3
1 - 2 - 3

1 - 2 - 3
6 - 7 - 8 - 9 - 4 - 5 - 2 - 3

Plan:
- create Node class, defining node.data and node.next
- create a function to find the intersection, intersection(headA, headB)
- check if either headA or headB, headA.next or headB.next is None, if so return None
- create two pointers, pointerA and pointerB, pointerA = headA, pointerB = headB
- while pointerA is not None or pointerB is not None:
    - if pointerA is equal to pointerB, return pointerA
    - else, set pointerA = pointerA.next, pointerB = pointerB.next
- return None

e time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

U: we want to see if the head and tail are connected
M: use two pointers to detect the cycle
   use a set to see if we detect the cycles
P:
    1. check if the list is empty or contain only one node
    2. initialize two pointers call one and two to detect the cycle
    3. if two pointers are not equals return False 
        else :
    4. once cycle is found, iterate through list and create a set
        4a. if the set already includes the iterated node, return False
        4b. else, add node to set
        4c. keep iterating until you reach the head
    5. return True
I
'''