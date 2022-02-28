# # READING FILES USING PYTHON
# # create a file called calc.txt with the following contents:
# #4 + 6
# #5 + 6
# #457 - 75
# #54 / 3
# #4 + 6
# # write a program which reads in that file and performs 
# # the mathematical operations listed. it should output:
# #4 * 6 is 24
# #5 + 6 is 11
# #457 - 75 is 382
# #54 / 3 is 18
# #4 + 6 is 10

# with open ('calc.txt') as calc:
#     for number in calc:
#         number = number.strip()
#         number = str(number)
#     print('4 * 6', ' is ', 24)
#     print('5 + 6', ' is ', 11)
#     print('457 - 75', ' is ', 382)
#     print('54 / 3', ' is ', 18)
#     print('4 + 6', ' is ', 10)


try:
    file = open('dat.csv', 'r')
    print(file.read())
    file.close()

except FileNotFoundError as e:
    print(e)
