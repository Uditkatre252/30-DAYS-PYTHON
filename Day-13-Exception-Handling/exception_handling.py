
#
# try:
#     print(10+'8')
# except TypeError:
#     print('Oops! Something went wrong.')
#
# try:
#     name = input('Enter your name: ')
#     year_born = input('Enter your year born: ')
#     age = 2026 - year_born
#     print(f'You are {name} ad your age is {age} years old.')
# except ValueError:
#     print('Value Error Occured.')
# except TypeError:
#     print('Type error occured.')
# except ZeroDivisionError:
#     print('zero division error occured.')

# try:
#     name = input('Enter your name: ')
#     year_born = int(input('Enter your year born: '))
#     age = 2026 - year_born
#     print(f'You are {name} and your age is {age} years old.')
# except Exception as e:
#     print(e)

#Unpacking
def sum_of_five_numbers(a,b,c,d,e):
    return a+b+c+d+e
lst = [1,2,3,4,5]
print(sum_of_five_numbers(*lst))

numbers = range(2, 7)
print(list(numbers))
args = [2, 7]
numbers = range(*args)
print(numbers)


countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)

table = [2,4,6,8,10]
one , *middle,last = table
print(one, middle, last)

def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} years old'
dct = {'name': 'udit katre', 'country':'India','city':'Bhopal','age':22}
print(unpacking_person_info(**dct))

for index, item in enumerate([20, 30, 40]):
    print(index, item)
