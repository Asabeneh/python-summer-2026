'''
List is an indexed, ordered collection of items
- index
- order
- modifiable
'''

empty_list = []
print(empty_list)
print(len(empty_list))

nums = [1, 2, 3, 4]
print(nums)
print(len(nums))
print(nums[0])
print(nums[1])
print(nums[2])
print(nums[3])
print(nums[-1])
print(nums[0:2])
print(nums[1:])
print(nums[1:3])
nums[0] = 100
print(nums)

nums[-1] = 500

print(nums)

shopping_list = ['apple','orange','tomato']
shopping_list.append('brocolli')
print(shopping_list)
shopping_list.append('milk')
shopping_list.append('meat')
print(shopping_list)
shopping_list.extend(['coffee','tea','sugar','honey', 'drinks'])
print(shopping_list)

# shopping_list.pop(0)

print(shopping_list)
shopping_list.insert(3,'Onion')
print(shopping_list)
shopping_list.remove('brocolli')
print(shopping_list)
# del shopping_list[0]
print(shopping_list)
# shopping_list.clear()
print(shopping_list)
shopping_list_copy = shopping_list.copy()
print(shopping_list)
shopping_list_copy.extend(['Wine', 'Chicken', 'Pizza'])
print(shopping_list_copy)

positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers)

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

num1 = [0, 1, 2, 3]
num2= [4, 5, 6]
num2.extend(num1)
print(num2)

fruits = ['banana', 'orange', 'mango', 'lemon', 'orange', 'orange','lemon']
print(fruits.count('lemon'))   # 2
print(fruits.index('mango'))

fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits.reverse()
fruits.sort()
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)