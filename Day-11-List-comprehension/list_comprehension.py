
language = 'Python'
lst = list(language)
print(type(lst))
print(lst)


lst = [i for i in language]
print(type(lst)) # list
print(lst)

# Generating numbers
number = [i for i in range(11)]
print(number)
squares = [i*i for i in range(11)]
print(number)
number_tuple = [(i , i*i) for i in range(11)]
print(number_tuple)

even_numbers = (i for i in range(21) if i % 2 == 0)
print(even_numbers)

# Exercises

# Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
non_zero = [num for num in numbers if num>0]
print(non_zero)

# Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
falttened_list = [num for row in list_of_lists for num in row]
print(falttened_list)

num = [(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]

num_to_tup = [(i ,i) for i in num]
print(num_to_tup)

add = lambda x , y : x+y
print(add(10,20))

cube = lambda x : x**3
print(cube(10))

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
falttened_countries = [country for list in countries for country in list]
print(falttened_countries)