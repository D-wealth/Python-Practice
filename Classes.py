# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def speak(self):
#         print('Hello, my name is ' + self.name + ' and i am ' + str(self.age) + ' years old')
        
# john = Person('john', 34)
# jack = Person('jack', 35)

# print(jack.name, jack.age)
# jack.speak()

# print('--------------------------')

# print(john.name, john.age)
# john.speak()

# print('-------------------------------------------------------------------------------')


# class Dog:
#     def __init__(self, name, colour):
#         self.name = name
#         self.colour = colour

# bruno = Dog('bruno', 'brown')


# print('The name of my dog is ' + bruno.name + ' and its colour is ' + bruno.colour)



# class Employee:
#     company_name = 'Google'
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         # self.email = first_name + last_name + '@email.com'

#     def EmployeeDetails(self):
#         print(f'{self.first_name}.{self.last_name}@{Employee.company_name}.com')

#     @classmethod
#     def change_name(cls, new_name):
#         cls.company_name = new_name

# Employee.change_name('Youtube')
# emp_1 = Employee('john', 'dave')
# emp_1.EmployeeDetails()



def dist_conversion(distance):
    d_input = int(input('Enter a distance in km :'))
    miles = d_input *  0.6214
    return miles

dist_conversion(10)