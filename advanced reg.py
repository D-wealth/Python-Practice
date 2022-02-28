



import re 

texts = 'CoreyMSchafer@gmail.com, corey.schafer@university.edu, corey-321-schafer@my-work.net'

pattern = re.compile('[a-zA-Z0-9-.]+@[a-z-]+\.(com|edu|net)')

result = pattern.search(texts)
print(result)



texts = 'De_wealth_official1@gmail.com, Nvestor001@gmail.ng'
pattern = re.compile('[A-Za-z0-9_@]+[a-z_0-9]+@[a-z]+\.(com|ng)')
result = pattern.findall(texts)
print(result)

