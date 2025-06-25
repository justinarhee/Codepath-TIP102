def engagement_boost(engagements):
    squared_engagements = []
    
    for i in range(len(engagements)):
        squared_engagement = engagements[i] * engagements[i]
        squared_engagements.append((squared_engagement, i))
    
    squared_engagements.sort(reverse=True)
    
    result = [0] * len(engagements)
    position = len(engagements) - 1
    
    for square, original_index in squared_engagements:
        result[position] = square
        position -= 1
    
    return squared_engagements

print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))

# [0, 1, 9, 16, 100]
# [4, 9, 9, 49, 121]

def mystery_function(nums):
    left = len(nums) - 1
    right = len(nums) - 1

    while right >= 0:
        if nums[right] != 0:
            temp = nums[right]
            nums[right] = nums[left]
            nums[left] = temp
            left -= 1
        right -= 1
    return nums

nums = [0, 0, 1, 2, 0, 3]
print(mystery_function(nums))


