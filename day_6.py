# st = set()
# num = {1,2,3,4,5,6,7,8}
# st.add('udit')
# print(st)
# num.update(st)
# print(num)
# num.remove(3)
# print(num)
# num.pop()
# print(num)
# num.clear()
# print(num)
# del num
# it_companies = {'apple','microsoft','ibm'}
# print(len(it_companies))
# it_companies.add('Twitter')
# print(it_companies)
# new_companies = {'facebook','instagram','youtube'}
# it_companies.update(new_companies)
# print(it_companies)

# a = {1,2,3}
# b = {2,3,4}
# c = a.union(b)
# print(c)
# print(a.difference(b))
# print(a.intersection(b))
# print(a.issubset(b))
# print(a.issuperset(b))
# print(a.isdisjoint(b))
# del a
# del b
# del c

# # Dictionary
# empty_dict = {}
# dct = {
#     'name':'udit katre',
#     'age':21,
#     'country':'India',
#     'skills':['Java','Javascript','Python','React'],
#     'address':{
#         'state':'Madhya Pradesh',
#         'city':'Bhopal',
#     }
# }
# print(dct['name'])
# print(dct['age'])
# print(dct['country'])
# print(dct['skills'])
# print(dct['address']['city'])
# print(dct['address']['state'])
#
# dog = dict()
# dog['name'] = 'bruno'
# dog['color'] = 'brown'
# dog['breed'] = 'labra'
# dog['legs'] = 4
# dog['age'] = 10
#
# student = {
#     'first_name':'udit',
#     'last_name':'katre',
#     'age':21,
#     'gender':'male',
#     'marital_status':'married',
#     'skills':['Java','Javascript','Python','React'],
#     'address':{
#         'state':'Madhya Pradesh',
#         'city':'Bhopal',
#     }
# }
# print(len(student))
# print(type(student['skills']))
# student['skills'].append('Github')
# print(student['skills'])
#
# keys = student.keys()
# values = student.values()
# print(keys)
# print(values)
# print(student.items())
# student.pop('age')
# student.popitem()
# del student['first_name']
# print(student)

# Conditionals

# age = int(input('Enter your age: '))
#
# if age >= 18:
#     print('You are old enough to drive')
# else:
#     print(f'you need {18-age} more year to learn to drive')


# my_age = 22
# your_age = int(input('Enter your age: '))
#
# if my_age > your_age:
#     diff = my_age - your_age
#     if diff == 1:
#         print(f'I am {diff} years older than you')
#     else:
#         print(f'I am {diff} years older than you')
# elif my_age < your_age:
#     diff = your_age - my_age
#     if diff == 1:
#         print(f'You are {diff} years older than me')
#     else:
#         print(f'you are {your_age-my_age} years older than me')
# else:
#     print('We both are of same age')

# a = int(input('Enter number one: '))
# b = int(input('Enter number two: '))
#
# if a>b:
#     print(a,"is greater than b")
# elif a<b:
#     print(a,"is less than b")
# else:
#     print(a,"is equal to b")

score = int(input('Enter your score: '))

if score <= 100 and score >= 90:
    print('You get A grade')
elif score >=80 and score <=89:
    print('you get B grade')
elif score >=70 and score <=79:
    print('you get C grade')
elif score >=60 and score <=69:
    print('you get D grade')
else:
    print('you get F grade')