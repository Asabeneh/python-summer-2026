for i in range(6): # 0 to 5
    print(i)

print('==== While loop section ====')

n = 0

while n < 6:
    print(n)
    n = n  + 1 # 6


n = 5

while n > -1:
    print(n)
    n = n - 1


# crops = []

# while True:
#     name = input('Enter crop name: ')
#     if name == 'e' or name == 'exit':
#         break
#     crops.append(name)
# print(crops)


nums = [3, 0, -1, 4, 8, 5]
count = 0
while count < len(nums):
    print(nums[count], count)
    count = count + 1

'''
Number guessing game
'''