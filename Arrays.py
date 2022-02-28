
# # Arrays must be imported before it can be used, and also it can be used to store only a single data type 
# # ARRAYS IN PYTHON 
# from array import *
# a = array('i', [1, 2, 3, 4, 5])
# print(a)
# # ACCESSING ELEMENTS i.e INDEXING
# # positive indexing
# print(a[2])
# print()

# print(a[4])
# print()

# # Negavive indaxing
# print(a[-3])
# print()

# print(a[-1])
# print()


# # FIND THE LENGTH OF AN ARRAY WITH THE  USE OF LEN() FUNCTION

# # from array import *
# a = array('i', [1, 2, 3, 4, 5, 6])

# length = len(a)
# print('The length is', length)


# # ADD AN ELEMENT TO THE END OF AN ARRAY WITH THE USE OF APPEND() METHOD
# a = array('i', [1, 2, 3, 4, 5, 6])
# a.append(8)
# print(a)

# # ADD BUNCH OF ELEMENTS AT THE END OF AN ARRAY WITH THE USE OF EXTENS METHOR()

# a = array('i', [1, 2, 3, 4, 5, 6])
# a.extend([7, 8, 9])
# print(a)

# # INSERT AN ELEMENT TO A SPECIFIC INDEX OF AN ARRAY
# a = array('i', [1, 2, 3, 4, 5, 6])
# a.insert(3, 9)
# print(a)

# # REMOVING ELEMENT OF AN ARRAY USING THE POP METHOD() AND STILL RETURN THE REMOVED ELENMENT
# a = array('i', [1, 2, 3, 4, 5, 6])
# # the pop method removes the last element of the list if its not specified and still returns the element removed
# print(a.pop())

# # the pop method removes the specified index from an array and still returns the element removed
# a = array('i', [1, 2, 3, 4, 5, 6])
# print(a.pop(2))

# # REMOVING ELEMENT OF AN ARRAY USING THE REMOVE METHOD()
# # The remove method is used to remove the specified indexed element and does not returns it
# a = array('i', [1, 2, 3, 4, 5, 6])
# a.remove(5)
# print(a)

# # ARRAY CONCATENATION
# a = array('i', [1, 2, 3, 4, 2])
# b = array('i', [5, 4, 3, 2, 1])
# c = a + b
# print(c)


# # use ('d') float of an array
# from array import *
# a = array('d', [1, 2, 3, 4, 5, 6])
# print(a)

# import array
# a = array.array('i', [1, 2, 3, 4, 5, 6])
# b = 2

# while b < a[3] :
#     print(a[b])
#     b = b + 1



    
# # FUNCTION TO SUM ARRAYS SIMULTANEOUSLY

# def add_arrays(x, y):
#     z = []
#     for x_elem, y_elem in zip(x, y):
#         z.append(x_elem + y_elem)
#     return z 

# x = [1,2,3,4]
# y = [5,6,7,8]

# z = add_arrays(x,y)
# print(z)


def 