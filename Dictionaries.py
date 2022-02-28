# DICTIONARIES
Groceries = {'banana': 4, 'apple': 5}
print(Groceries['banana'])

contacts = {
    'jane': ['123-456-7890', 'jane@mail.com'],
    'jack': ['098-765-4321', 'jack.@web.ng']
}

print(contacts['jack'][1])


# word counts using Dictionary
sentence = 'I like the name Aaron, because the name Aaron is the best'

word_counts = {
    'name': 2,
    'like': 1,
    'Aaron': 2
}

print(word_counts['Aaron'])

# add to word_counts
word_count = word_counts['the'] = 3
print(word_counts)


# METHODS IN DICTIONARY
# DICT.ITEMS()
print(word_counts.items())

# DICT.KEYS()
print(word_counts.keys())

# DICT.VALUES()
print(word_counts.values())

# DICT.POPITEM()
print(word_counts.popitem())

# DICT.POP()
print(word_counts.pop('Aaron'))

# DICT.CLEAR()
print(word_counts.clear())

# DICT.KEY = KEY --> VALUE

contacts = {
    'jane': ['123-456-7890', 'jane@mail.com'],
    'joe': ['098-765-4321', 'joe@web.ng'],
    'jack': ['219-383-4853', 'jack@web.com']
}


# Iterating over a dictionary to get the items()
for contact in contacts.items():
    print(contact)


# Iterating over a dictionary to get the keys
for contact in contacts.keys():
    print(contact)


# Iterating over a dictionary to get the values
for contact in contacts.values():
    print(contact)


# you can also index into dictionaries to print out a specific value
print(contacts['jane'][1]) 
