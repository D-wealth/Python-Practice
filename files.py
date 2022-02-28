# file = open('datas.csv', 'r')
# file.write('This is a csv file\n')
# file.write('This is just a practice')
# file.write('\nThis is a appending file')

# print(file.read())

# file.close()

# Checking if a file exists
filename = 'datas.csv'
import os

if os.path.isfile(filename):
    with open (filename, 'r+') as file:
        # print(file.write('\n Another csv file'))
        # file.write('\n New csv file')
        print(file.read())


# def sample(l):
#     new_l = []
#     for x in l:
#         new_l.append(x**2)
#     return new_l

# print(sample([1,2,3,4,5]))
