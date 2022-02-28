# TUPLES
credit_card_1 = ('12365235673864439', 'Jane smith', '12/09', 647)
credit_card_2 = ('45786287582524531', 'Joe brian', '11/04', 204)

print(credit_card_1)

# unpacking tuples
person_1 = ('jane moore', 12, 'pasta')
person_2 = ('Joe', 15, 'noodles')

people = person_1, person_2
for (name, age, favfood) in people:
    print(name)
    print(age)
    print(favfood)