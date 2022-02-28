
# BOOLEAN ALGEBRA
# True / False

johnny_salary = 40

# this will automaticall print True because johnny_salary is greater than 39
print(johnny_salary > 39)

# USING CONDITIONAL STATEMENTS IN BOOLEAN
Johnny_homework = True
Johnny_throwout_gabbage = True
Johnny_play_game = False

if Johnny_homework:
    print('Johnny does his homework')


# USING THE BOOLEAN LOGICAL OPERATORS( AND, OR, NOT)
Johnny_homework = True
Johnny_throwout_gabbage = True
Johnny_play_game = False
Johnny_jumped_up = False
# AND
if Johnny_homework and Johnny_throwout_gabbage:
    print('Johnny is a good boy')

if Johnny_homework and Johnny_play_game:
    print('Excellent')

if Johnny_play_game and Johnny_jumped_up:
    print('OK')

# logical operator OR
Johnny_homework = True
Johnny_throwout_gabbage = True
Johnny_play_game = False
Johnny_jumped_up = False

if Johnny_homework or Johnny_play_game:
    print('YEAH!')

if Johnny_throwout_gabbage or Johnny_homework:
    print('yooooo!')

if Johnny_play_game or Johnny_jumped_up:
    print('waooooow')

# logical operator NOT
Johnny_homework = True
Johnny_throwout_gabbage = True
Johnny_play_game = False
Johnny_jumped_up = False

if not(Johnny_throwout_gabbage) or not(Johnny_homework):
    print('Dadadaddadadado')

print(not(Johnny_homework))
print(not(Johnny_throwout_gabbage))
print(True or False)
