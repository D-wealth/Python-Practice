filename = 'calc.txt'
import os

if os.path.isfile(filename):
    with open(filename, 'r') as file:
        print(file.read())
