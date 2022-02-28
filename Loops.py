# # WHILE LOOPS
# count = 100
# while count > 0:
#     print(count)
#     count = count - 1

# # while loops 2

# jack = 'happy'
# while jack == 'happy':
#     print('I am deeply sorry')

# import random
# n = 20
# number_to_be_guessed = random.randint(1, 20) + 1
# guess = 0

# while guess != number_to_be_guessed :
#     guess = int(input('Guess : '))

#     if guess > 0 :
#         if guess < number_to_be_guessed:
#             print('number is too small')

#         elif guess > number_to_be_guessed :
#             print('number is too large')

#     else:
#         print('You\'re giving up already')
#         break
# else:
#     print('Congratulations, you made it')
    

i = 0
while i < 10:
    print(i)
    i += 1
        



def map_l(l):
    return l - 2

print(list(map(map_l, [2,3,4,5]))) 

numbers = [1,2,3,4,5]

for num in numbers:
    res =  num * num
    print(res)