# Functions
import math
from itertools import count


def print_name(name):
    print(name)
print_name('udit')

def add_two_numbers(a,b):
    return a+b
add_two_numbers(4,6)

def area_of_circle(radius):
    return math.pi*radius**2
area_circle = area_of_circle(5)
print(area_circle)

def add_all_nums(*args):
    if not all(isinstance(x, (int, float)) for x in args):
        return "All numbers should be integers."

    return sum(args)
print(add_all_nums(1,2,3,4,5,6,'t',8,9))

def convert_celsius_to_fahrenheit(temp):
    return temp*(9/5)+32
print(convert_celsius_to_fahrenheit(10))


def check_season(month):
    month = month.capitalize()
    seasons = {
        'Winter': ['December', 'January', 'February'],
        'Spring': ['March', 'April', 'May'],
        'Summer': ['June', 'July', 'August'],
        'Autumn': ['September', 'October', 'November']
    }

    for season, months in seasons.items():
        if month in months:
            return season

    return "Invalid Month"

print(check_season("march"))

def calculate_slope(x1, y1, x2, y2):
    if x2 -x1 == 0:
        return "Undefined"
    return (y2-y1)/(x2-x1)
print(calculate_slope(2,3,2,5))

def print_list(list):
    return list[0:len(list)-1]
lst = [1,2,3,4,5]
print(print_list(lst))

def reverse_list(lst):
    return lst[::-1]
print(reverse_list(lst))

def capitalize_list_items(list):
    return [item.capitalize() for item in list]

fruits = ['apple', 'banana', 'orange']
print(capitalize_list_items(fruits))

def add_item(list, item):
    if item in list:
        return 'item already exists'
    list.append(item)
    return list
print(add_item(fruits, 'Mango'))
print(add_item(fruits, 'banana'))

def remove_item(list, item):
    if item not in list:
        return 'item does not exist'
    list.remove(item)
    return list

print(remove_item(fruits, 'pineapple'))

def sum_of_numbers(num):
    if num < 1:
        return num
    return sum_of_numbers(num-1) + num
print(sum_of_numbers(100))

def is_prime(num):
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True
print(is_prime(7))
count = 0
for i in range(2,100):
    if is_prime(i):
        count= count+1
        print(i)
print(count)

def check_item_is_unique(list1):
   return len(list1) == len(set(list1))

print(check_item_is_unique(fruits))