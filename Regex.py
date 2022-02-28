# #  REGULAR EXPRESSION IN PYTHON (regex)
# import re
# texts = 'De-wealthofficial1@gmail.com, Nvestor001@web.ng, frghfredvsxbjheg'
# pattern = re.compile('[A-Za-z-]+[a-z0-9]+@+\w+\.(com|ng)')
# result = pattern.search(texts)
# print(result)

# #[A-Za-z-]+[a-z0-9]+@+\w+\.(com|ng)

import sys

s1 = sys.argv[1]
s2 = sys.argv[2]

import random
from random import randint

user = int(input(random.randint(s1, s2)))
print(user)