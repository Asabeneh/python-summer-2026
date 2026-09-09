'''
Tuple: is not modifiable
- ordered and index

'''

nums = (1, 2, 3, 4)
print(nums)
print(type(nums))
print(len(nums))
print(nums[0])
for num in nums:
    print(num)

print(nums.count(2))
print(nums.index(4))

print(tuple(['a','b','c']))
print(4 in nums)

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits_and_vegetables = list(fruits + vegetables)
fruits_and_vegetables.sort()
print(fruits_and_vegetables)

