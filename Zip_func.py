# ZIP FUNCTION
# zip list
list_1 = [1, 2, 3, 4, 5]
list_2 = ['one', 'two', 'three', 'four', 'five']
zip_list = list ( zip (list_1, list_2))
print(zip_list)

# unzip list
unzip = list ( zip (*zip_list))
print(unzip)

for i in zip (list_1, list_2):
    print(i)

# ZIP SENTENCE
items = ['orange', 'banana', 'cherry']
counts = [4, 3, 4]
prices = [50, 40, 55]

sentences = []

for (item, count, price) in zip (items, counts, prices):
    sentence = 'i bought ' + str(count) + ' ' + str(item) + 's at ' + str(price) + ' each.'

    sentences.append(sentence)

print(sentences)
    
# SUM_LIST SIMULTENEOUSLY USING THE ZIP FUNCTION
 # zip 2
a = [1,2,3,4]
b = [5,6,7,8]

c = []

for a_elem,b_elem in zip(a,b):
    c.append(a_elem - b_elem)

print(c)


