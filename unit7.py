#standard set 1

#P1
#understand - want to count number of suits in array, iterativly and recursivly.
#match - for-loop, recursion, queue
#edge cases - empty array,
#plan -
# parameters = array, current position 
#1. if array is empty return 0
#2. return 1 + funct(suits - first element)
#time & space - O(n), O(1)


def count_suits_iterative(suits):
    count = 0
    for i in suits:
        count += 1
    return count

def count_suits_recursive(suits):
    if not suits:
        return 0
    return 1 + count_suits_recursive(suits[1:])

#print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
#print(count_suits_recursive(["Mark I", "Mark I", "Mark III", "Mark IV"]))

'''
P2

Understand: return the total sum of elements in list
Edge Cases: empty array
Match: recrusion
Plan:
1. if arry empty return 0
2. return value of stone + sum_stones(array - first element)
time & space - O(n), O(1)
'''

def sum_stones(stones):
    if not stones:
        return 0
    return stones[0] + sum_stones(stones[1:])

#print(sum_stones([5, 10, 15, 20, 25, 30]))
#print(sum_stones([12, 8, 22, 16, 10]))


#P3
#understand - want to count num of unique suits
#match - rescursion, set, itertivly, stack
#edge cases - empty array
#plan -
#1. if the arry is empty return 0
#2. if 0 va of index is in values from 1 to end move to next val
#   else return + 1 and moev to next index.
#time & space - O(n), O(1)


def count_suits_iterative2(suits):
    lst = set(suits)
    count = 0

    for s in lst:
        count += 1
    return count

def count_suits_recursive2(suits):
    if not suits:
        return 0
    if suits[0] in suits[1:]:
        return count_suits_recursive2(suits[1:])
    return 1 + count_suits_recursive2(suits[1:])


# print(count_suits_iterative2(["Mark I", "Mark II", "Mark III"]))
# print(count_suits_recursive2(["Mark I", "Mark I", "Mark III"]))

#P4
#understand - want to cal fib seq n times
#match - recursion
#edgecases - if n = 1 or 0
#plan -
#1. if 1 or 0 return n
#2. return fib(n - 1) + fib(n - 2)
#time & space -

def fibonacci_growth(n):
    if n == 0 or n == 1:
        return n
    return fibonacci_growth(n - 1) + fibonacci_growth(n - 2)

#print(fibonacci_growth(5))
#print(fibonacci_growth(8))

#P5
#understand - want to caluc power of 4 to nth value
#match - recursion
#edge cases - n = 0(return 1), n = 1(return 4)
#plan -
#1. if n == 0 return 1 if n == 1 return 4
#2. return 4 * funct(abs(n - 1))
#time & space - O(n), O(1)

def power_of_four(n):
    if n == 0:
        return 1
    if n == 1:
        return 4
    if n < 0:
        return 1 / (4 * power_of_four(abs(n)-1))
    return 4 * power_of_four(abs(n)-1)

# print(power_of_four(2))
# print(power_of_four(-2))

'''
P1
It's vacation time! Given an integer vacation_length and a list of integers cruise_lengths sorted in ascending order, 
use binary search to return True if there is a cruise length that matches vacation_length and False otherwise.

Example Output:
True
False

Understand
- given: a list of integers in ascending order, int value vacation_length
- return: boolean value, True if the int vacation_length is in the given list, False otherwise

Match: binary search

Plan:


'''

def find_cruise_length(cruise_lengths, vacation_length):
    left = 0
    right = len(cruise_lengths) - 1

    while left <= right:
        mid = (right + left) // 2
        if cruise_lengths[mid] == vacation_length:
            return True
        elif cruise_lengths[mid] < vacation_length:
            left = mid + 1
        else:
            right = mid - 1
    return False

# print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))
# print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))



def find_cabin_index(cabins, preferred_deck):
    pass

print(find_cabin_index([1, 3, 5, 6], 5))
print(find_cabin_index([1, 3, 5, 6], 2))
print(find_cabin_index([1, 3, 5, 6], 7))
