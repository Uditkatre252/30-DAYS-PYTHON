# from shlex import split
#
# fruits = ["apple", "banana", "cherry"]
# vegetables = ["Tomato", "Potato", "onion", "carrot"]
# print(fruits)
# print(len(fruits))
# print(vegetables)
# print(len(vegetables))
#
# print(vegetables[0])
# print(vegetables[1])
# print(vegetables[3])
# mixed_data_types = ["Udit katre",22,5.55,False,"Bhopal"]
# it_companies = ["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
# print(mixed_data_types)
# print(it_companies)
# print(len(it_companies))
# it_companies.append('TCS')
# print(it_companies)
# it_companies.insert(5,"Intel")
# print(it_companies)
# it_companies.sort()
# print(it_companies)
# print(it_companies[1].upper())
#
# result = '#; '.join(it_companies)
# print(result)
#
# if "Apple" in it_companies:
#     print(True)
# else:
#     print(False)
#
# print(it_companies[:3])
# print(it_companies[3:])
# print(it_companies[::2])
# print(it_companies[1::2])
# it_companies.remove(it_companies[0])
# print(it_companies)
#
# # it_companies.clear()
# # print(it_companies)
# del it_companies[0:5]
# print(it_companies)
# del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end
redux_index = full_stack.index('Redux')
full_stack.insert(redux_index + 1, 'Python')
full_stack.insert(redux_index + 2, 'SQL')
print(full_stack)