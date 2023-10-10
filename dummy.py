from functools import reduce 

nums = [1, 2, 3, 4]
ans = tuple(num*5 for num in nums)
print(ans) 

# fruits = ['mango', 'apple', 'orange', 'cherry', 'grapes']
# print(list(filter(lambda fruit: 'g' in fruit, fruits)))