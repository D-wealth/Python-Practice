# STRING
a = 'hello'
print(a)

# strings concatenation
age = 20
first_name = 'Abdulroheem'
last_name = 'Qowam'
output = 'My name is '+ first_name + ' ' + last_name + ' and i am '  + str(age)+ 'years old.'
print(output)

# STRING FORMATTING USING THE DEF FUNCTION
our_dog = {'name': 'bruno', 'colour': 'brown'}

def describe(dog):
    return f"{dog['name']} is {dog['colour']}"

our_dog = describe(our_dog)
print(our_dog)
