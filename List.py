# LIST
# LIst can be used to store many data types
l = [1, 'hello', ['hi'], ('hey'), 2.5,{'banana': 4}, {'apple'}, True]
print(l)

# INDEXING LIST
fruits = ['banana', 'apple', 'pineapple', 'papaya']
print(fruits[0])

# METHODS IN LIST

# APPEND()
fruits = ['banana', 'apple', 'pineapple', 'papaya']
fruits.append('paw-paw')
print(fruits)

# SUM()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum(numbers))


# LEN()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(numbers))


# REPLACE()
a = 'Hello World'
print(a.replace('H', 'J'))



# SORT()
numbers = [34, 67, 23, 13, 9, 56]
numbers.sort()
print(numbers)

# POP()
fruits = ['banana', 'apple', 'pineapple', 'papaya']
fruits.pop()
print(fruits)

# REVERSE()
numbers = [34, 67, 23, 13, 9, 56]
numbers.reverse()
print(numbers)

# DEL()
numbers = [34, 67, 23, 13, 9, 56]
del(numbers)

# EXTEND()
fruits = ['banana', 'apple', 'pineapple', 'papaya']
vegetables = ['okro', 'bitterleaf']
fruits.extend(vegetables)
print(fruits)

# CLEAR()
fruits = ['banana', 'apple', 'pineapple', 'papaya']
fruits.clear()

# INSERTING()
fruits = ['banana', 'apple', 'pineapple', 'papaya']
fruits.insert(1, 'orange')
print(fruits)


# SQUARE NUMBERS IN A LIST USING THE APPEND METHOD
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

squared_numbers = []

for number in numbers:
    squared_numbers.append(number ** 2)

print(squared_numbers)

















