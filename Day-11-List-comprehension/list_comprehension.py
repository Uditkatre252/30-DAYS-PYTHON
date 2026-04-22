
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