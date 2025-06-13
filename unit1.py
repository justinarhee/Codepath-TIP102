# session 1 standard problem set ver 1

# problem 1
def welcome():
	print("Welcome to The Hundred Acre Wood!")
	
# welcome()

# problem 2
def greeting(name):
    print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")

# greeting("Justina")

# problem 3
def print_catchphrase(character):
    dict = {"Pooh": "Oh, bother!","Tigger": "TTFN: Ta-ta for now!", 
            "Eeyore": "Thanks for noticing me.", "Christopher Robin": "Silly old bear."}
    if character in dict:
        print(dict[character])
    else:
        print(f"Sorry! I don't know {character}'s catchphrase!")

# character = "Pooh"
# print_catchphrase(character)
# character = "Piglet"
# print_catchphrase(character)

# problem 4
def get_item(items, x):
     if x > 0 and x < len(items):
         return items[x]
     return None

# items = ["piglet", "pooh", "roo", "rabbit"]
# x = 2
# print(get_item(items, x))
# items = ["piglet", "pooh", "roo", "rabbit"]
# x = 5
# print(get_item(items, x))

# problem 8
def print_todo_list(task):
    print("Pooh's To Dos:")
    
    for i, item in enumerate(task, start=1):
         print(f"{i}. {item}")

# task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
# print_todo_list(task)
# task = []
# print_todo_list(task)

# problem 10
def split_haycorns(quantity):
    factors = []
    for i in range(1, quantity+1):
        if quantity % i == 0:
            factors.append(i)
    return factors

# quantity = 6
# print(split_haycorns(quantity))
# quantity = 1
# print(split_haycorns(quantity))

# problem 11
def tiggerfy(s):
    s = s.lower()
    letters_to_remove = {'t', 'i', 'g', 'e', 'r'}
    result = [c for c in s if c not in letters_to_remove]
    return ''.join(result)

# s = "suspicerous"
# print(tiggerfy(s))
# s = "Trigger"
# print(tiggerfy(s))
# s = "Hunny"
# print(tiggerfy(s))

# session 1 standard problem set ver 2
# problem 5
def concatenate(words):
    return ''.join(words)

# words = ["vengeance", "darkness", "batman"]
# print(concatenate(words))
# words = []
# print(concatenate(words))

# session 1 advanced problem set ver 1

# problem 1
def linear_search(lst, target):
    for i in lst:
          if i == target:
              return lst.index(i)
    return -1

# items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
# target = 'hunny'
# print(linear_search(items, target))
# items = ['bed', 'blue jacket', 'red shirt', 'hunny']
# target = 'red balloon'
# print(linear_search(items, target))

# problem 4
def non_decreasing(nums):
    count = 0
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            count += 1
        if count > 1:
            return False
    return True

# nums = [4, 2, 3]
# print(non_decreasing(nums))
# nums = [4, 2, 1]
# print(non_decreasing(nums))

# problem 5
'''
Understand
- given an int list clues, integer values lower and upper
- all elements in clues are unique, within the range [lower, upper]
- not all integers in the range [lower, upper] are in clues
- return a list of integer lists that identify the missing integers in the range [lower, upper]
  from clues
- should have the least number of elements as possible

Plan
1. create a list missed to store the list of missing integers
2. create a for loop iterating through the elements in clues
3. check the element at index i in clues and the element at index i+1
    3a. if clues[i+1] - clues[i] > 1
        3a1. append to missed a list [clues[i] + 1, clues[i+1] - 1]
    3b. else, continue
4. return missed
'''
def find_missing_clues(clues, lower, upper):
    missed = []
    for i in range(len(clues) - 1):
        if clues[i + 1] - clues[i] > 1:
            missed.append([clues[i]+1, clues[i+1]-1])
    if clues[0] > lower:
        missed.insert(0, [lower, clues[0] - 1])
    if clues[-1] < upper:
        missed.append([clues[-1] + 1, upper])
    missed.sort()
    return missed

# clues = [0, 1, 3, 50, 75]
# lower = 0
# upper = 99
# print(find_missing_clues(clues, lower, upper))
# clues = [-1]
# lower = -1
# upper = -1
# print(find_missing_clues(clues, lower, upper))

# problem 6
def harvest(vegetable_patch):
    count = 0
    for row in vegetable_patch:
        for col in row:
            if col == "c":
                count += 1
    return count

# vegetable_patch = [
# 	['x', 'c', 'x'],
# 	['x', 'x', 'x'],
# 	['x', 'c', 'c'],
# 	['c', 'c', 'c']
# ]
# print(harvest(vegetable_patch))

# problem 7
'''
Understand
- given two integer lists pile1 and pile2, positive int k
- finds good pairs (i, j) s.t. i and j are indices of pile1 and pile2, pile1[i] % pile2[j] * k == 0
- returns number of good pairs

Plan
1. multiply each element in pile2 by k
2. create an int count = 0
3. for each element in pile1, check if its divisible by any elements in pile2
    3a. if true, increment count
    3b. else, continue
4. return count
'''

def good_pairs(pile1, pile2, k):
    count = 0
    pile2 = [x * k for x in pile2]
    for i in pile1:
        for j in pile2:
            if i % j == 0:
                count += 1
    return count

# pile1 = [1, 3, 4]
# pile2 = [1, 3, 4]
# k = 1
# print(good_pairs(pile1, pile2, k))
# pile1 = [1, 2, 4, 12]
# pile2 = [2, 4]
# k = 3
# print(good_pairs(pile1, pile2, k))

# problem 8
'''
Understand
- given a n x n grid of integerse
- return a n-2 x n-2 grid of integers called maxGrid
- element at (i,j) in maxGrid is maximum of 3x3 subgrid in grid centered at (i+1, j+1)

Plan
1. create an empty list maxGrid to store the maximums
    1a. size = n-2
    1b. maxGrid = [[0 for _ in range(size)] for _ in range(size)]
2. create a for loop that iterates through n-2 x n-2
    2a. for element at (i,j), find maximum of 3x3 grid centered at (i+1, j+1)
        2a1. maximum = max(grid[i][j], grid[i][j+1], grid[i][j+2],
                        grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2],
                        grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2])
    2b. maxGrid[i][j] = maximum
'''
def local_maximums(grid):
    n = len(grid)
    size = n - 2
    maxGrid = [[0 for _ in range(size)] for _ in range(size)]
    
    for i in range(size):
        for j in range(size):
            maximum = max(
                grid[i][j], grid[i][j+1], grid[i][j+2],
                grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2],
                grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]
            )
            maxGrid[i][j] = maximum
            
    return maxGrid

# grid = [
# 	[9, 9, 8, 1],
# 	[5, 6, 2, 6],
# 	[8, 2, 6, 4],
# 	[6, 2, 2, 2]
# ]
# print(local_maximums(grid))
# grid = [
# 	[1, 1, 1, 1, 1],
# 	[1, 1, 1, 1, 1],
# 	[1, 1, 2, 1, 1],
# 	[1, 1, 1, 1, 1],
# 	[1, 1, 1, 1, 1]
# ]
# print(local_maximums(grid))

# session 1 advanced problem set ver 2

# problem 2
def hulk_smash(n):
    hulk = []
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            hulk.append("HULK SMASH")
        elif i % 3 == 0:
            hulk.append("HULK")
        elif i % 5 == 0:
            hulk.append("SMASH")
        else:
            hulk.append(i)
    return hulk

# n = 3
# print(hulk_smash(n))
# n = 5
# print(hulk_smash(n))
# n = 15
# print(hulk_smash(n))

# problem 4
'''
Understand
- given a int list meals, int list capacity
- meals include the number of meals to contain in boxes
- capacity includes different boxes and how many meals they can contain
- return the minimum number of boxes needed to contain all meals

Plan
1. find the sum of meals
    1a. total = sum(meals)
2. sort capacity in descending order
    2a. capacity.sort(reverse=True)
3. create a int var count = 0 to store the number of boxes used
4. create a for loop to iterate through capacity
    4a. for each box in capacity, check if total is greater than 0
        4a1. if true, subtract the box capacity from total
        4a2. increment count by 1
    4b. else, break the loop
5. return count
'''
def minimum_boxes(meals, capacity):
    total = sum(meals)
    capacity.sort(reverse=True)
    count = 0
    
    for box in capacity:
        if total > 0:
            total -= box
            count += 1
        else:
            break
            
    return count

# meals = [1, 3, 2]
# capacity = [4, 3, 1, 5, 2]
# print(minimum_boxes(meals, capacity))
# meals = [5, 5, 5]
# capacity = [2, 4, 2, 7]
# print(minimum_boxes(meals, capacity))

# session 2 advanced problem set ver 1

# session 2 advanced problem set ver 2


# def main():
#     print(split_haycorns(8))

# if __name__ == "__main__":
#     main()