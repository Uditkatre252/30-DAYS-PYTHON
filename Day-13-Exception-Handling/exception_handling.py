
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

try:
    name = input('Enter your name: ')
    year_born = int(input('Enter your year born: '))
    age = 2026 - year_born
    print(f'You are {name} and your age is {age} years old.')
except Exception as e:
    print(e)
