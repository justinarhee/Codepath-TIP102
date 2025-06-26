# Problem 1: Planning Your Daily Work Schedule
# Your day consists of various tasks, each requiring a certain amount of time. To optimize your workday, you want to find a pair of tasks that fits exactly into a specific time slot you have available. You need to identify if there is a pair of tasks whose combined time matches the available slot.

# Given a list of integers representing the time required for each task and an integer representing the available time slot, write a function that returns True if there exists a pair of tasks that exactly matches the available time slot, and False otherwise.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.


def find_task_pair(task_times, available_time):
    for i in task_times:
        if available_time - i in task_times and available_time - i != i:
            return True
    return False

# Example Usage:

# task_times = [30, 45, 60, 90, 120]
# available_time = 105
# print(find_task_pair(task_times, available_time))

# task_times_2 = [15, 25, 35, 45, 55]
# available_time = 100
# print(find_task_pair(task_times_2, available_time))

# task_times_3 = [20, 30, 50, 70]
# available_time = 60
# print(find_task_pair(task_times_3, available_time))
# Example Output:

# Complexity : O(n) where n is the size of the task_times
# True
# True
# False

# Problem 2: Minimizing Workload Gaps
# You work with clients across different time zones and often have gaps between your work sessions. You want to minimize these gaps to make your workday more efficient. You have a list of work sessions, each with a start time and an end time. Your task is to find the smallest gap between any two consecutive work sessions.

# Given a list of tuples where each tuple represents a work session with a start and end time (both in 24-hour format as integers, e.g., 1300 for 1:00 PM), write a function to find the smallest gap between any two consecutive work sessions. The gap is measured in minutes.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def find_smallest_gap(work_sessions):
    diff = []
    for i in range(len(work_sessions) - 1):
        hour = work_sessions[i+1][0]//100 - work_sessions[i][1]//100
        minutes = work_sessions[i+1][0] % 100 - work_sessions[i][1] % 100
        if minutes < 0:
            hour -= 1
        minutes = abs(minutes)
        diff.append(hour * 60 + minutes)
    return min(diff) if diff else 0
# Example Usage:

# work_sessions = [(900, 1100), (1300, 1500), (1600, 1800)]
# print(find_smallest_gap(work_sessions))

# work_sessions_2 = [(1000, 1130), (1200, 1300), (1400, 1500)]
# print(find_smallest_gap(work_sessions_2))

# work_sessions_3 = [(900, 1100), (1115, 1300), (1315, 1500)]
# print(find_smallest_gap(work_sessions_3))
# Example Output:

# 60
# 30
# 15

# Problem 3: Expense Tacking and Categorization
# You travel frequently and need to keep track of your expenses. You categorize your expenses into different categories such as "Food," "Transport," "Accommodation," etc. At the end of each month, you want to calculate the total expenses for each category to better understand where your money is going.

# Given a list of tuples where each tuple contains an expense category (string) and an expense amount (float), write a function that returns the expense categories and the total expenses for each category. Additionally, the function should return the category with the highest total expense.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def calculate_expenses(expenses):
    category = {}
    for expense in expenses:
        if expense[0] in category:
            category[expense[0]]+=expense[1]
        else:
            category[expense[0]] = expense[1]
    return (category, max(category, key=category.get))
# Example Usage:

# expenses = [("Food", 12.5), ("Transport", 15.0), ("Accommodation", 50.0),
#             ("Food", 7.5), ("Transport", 10.0), ("Food", 10.0)]
# print(calculate_expenses(expenses))

# expenses_2 = [("Entertainment", 20.0), ("Food", 15.0), ("Transport", 10.0),
#               ("Entertainment", 5.0), ("Food", 25.0), ("Accommodation", 40.0)]
# print(calculate_expenses(expenses_2))

# expenses_3 = [("Utilities", 100.0), ("Food", 50.0), ("Transport", 75.0),
#               ("Utilities", 50.0), ("Food", 25.0)]
# print(calculate_expenses(expenses_3))
# Example Output:

# ({'Food': 30.0, 'Transport': 25.0, 'Accommodation': 50.0}, 'Accommodation')
# ({'Entertainment': 25.0, 'Food': 40.0, 'Transport': 10.0, 'Accommodation': 40.0}, 'Food')
# ({'Utilities': 150.0, 'Food': 75.0, 'Transport': 75.0}, 'Utilities')

# Problem 4: Analyzing Word Frequency
# As a digital nomad who writes blogs, articles, and reports regularly, it's important to analyze the text you produce to ensure clarity and avoid overusing certain words. You want to create a tool that analyzes the frequency of each word in a given text and identifies the most frequent word(s).

# Given a string of text, write a function that returns the unique words and the number of times each word appears in the text. Additionally, return a list of the word(s) that appear most frequently.

# Assumptions:

# The text is case-insensitive, so "Word" and "word" should be treated as the same word.

# Punctuation should be ignored.

# In case of a tie, return all words that have the highest frequency.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

import re
from collections import Counter

def word_frequency_analysis(text):
    lower = text.lower()
    words = re.findall(r'\b\w+\b', lower)
    dic = Counter(words)
    return (dic, max(dic,key = dic.get))
#  max(category, key=category.get)

text = "The quick brown fox jumps over the lazy dog. The dog was not amused."
print(word_frequency_analysis(text))

text_2 = "Digital nomads love to travel. Travel is their passion."
print(word_frequency_analysis(text_2))

text_3 = "Stay connected. Stay productive. Stay happy."
print(word_frequency_analysis(text_3))
# Example Output:

# ({'the': 3, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 2, 'was': 1, 'not': 1, 'amused': 1}, ['the'])
# ({'digital': 1, 'nomads': 1, 'love': 1, 'to': 1, 'travel': 2, 'is': 1, 'their': 1, 'passion': 1}, ['travel'])
# ({'stay': 3, 'connected': 1, 'productive': 1, 'happy': 1}, ['stay'])

