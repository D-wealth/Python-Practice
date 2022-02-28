
# DEFINING FUNCTIONS IN PYTHON
def greet():
    print('hello')
    print('how are you doing')

greet()

# DEFINING FUNCTIONS USING ARGUMENTS
def greet(name):
    print('hello', name)

greet('mark')

# PASSING MULTIPLE ARUMENTS INTO A FUNCTION

# the sum of two numbers
def add_numbers(n1, n2):
    sum = n1 + n2
    print('the sum is', sum)

number1 = 5.4
number2 = 6.7

add_numbers(number1, number2)

# USING THE RETURN METHOD
# the return statement is used to print the defined statement outside of the function, e.g
def add_numbers(n1, n2):
    result = n1 + n2
    return result

number1 = 5.4
number2 = 6.7
# the result is printed outside the function with the use of the return statement
result = add_numbers(number1, number2)
print('The sum is', result)


marks = [55, 64, 75, 80, 34]

 # you can find the length of marks using the len function

length = len(marks)
print('Length is', length)

# you can find the sum of the list using the SUM function
sum_of_numbers = sum(marks)
print('The sum is', sum_of_numbers)


# DEFINING FUNCTIONS TO FIND  GRADE AND AVERAGE MARKS
# Suppose you just attended a university examination,
# The marks you obtained in various subjects are 
# stored in a list like this:

marks = [55, 64, 75, 80, 65]

# You want to find the average marks you obtained in
# the exam. And, based on the average marks you
# want to find your grade . The grading rule is like this:

# * You will get grade A if the baverage mark is 
# equal to or above 80

# * You will get grade B if the average marks is 
# equal to or above 60 and less than 80

# * You will get grade C if the average mark is 
# equal to or above 50 or less than 60

# * And if the average marks is less than 50,
# you will get Grade F 

# functions to find average marks 
def find_average_marks(marks):
    sum_of_marks = sum(marks)
    total_subjects = len(marks)
    average_marks = sum_of_marks / total_subjects 
    return average_marks 

# functions to find grade
def compute_grade(average_marks):
    if average_marks >= 80:
        grade = 'A'
    elif average_marks >= 60:
        grade = 'B'
    elif average_marks >= 50:
        grade = 'c'
    else:
        grade = 'F'
    return grade

marks = [55, 64, 75, 80, 65]
average_marks = find_average_marks(marks)
print('Your mark is:', average_marks)

grade = compute_grade(average_marks)
print('Your grade is:', grade)


# PROGRAMMING TASK
# Can you create a program to add and multiply
# two numbers ? For this,  create two functions
# add_numbers() and multiply_numbers().
# These functions should compute the result and 
# return them to the function call. And, the results
# should be printed from outside the function

# functions to add_numbers
def add_numbers(n1, n2):
    result = n1 + n2 
    return result 

number1 = 4.5
number2 = 5.5

result = add_numbers(number1, number2)
print('The sum is', result)

def multiply_numbers(n1, n2):
    result = n1 * n2
    return result 

number1 = 5.6
number2 = 6.4

result = multiply_numbers(number1, number2)
print(result)




# SUM TWO
def sum_two(number1, number2):
    output = number1 + number2 
    return output 

number_1 = 1
number_2 = 2

output = sum_two(number_1, number_2)
print('The sum of the numbers is', output)
