# tpl = list()
# tpl[0] = 'udit'
# print(tpl)

sisters = ('Sister1','Sister2')
brothers = ('Brother1','Brother2')
sibling = sisters + brothers
print(sibling)
print(f"There are {len(sibling)} siblings")

parents = ('Father','Mother')
family_members = parents + sibling
print(family_members)

fruits = ('apple','banana','orange')
vegetable = ('potato','tomato','cabbage','lady Finger')
animal_product = ('milk','cheese','curd','eggs')

food_stuff_tp = fruits + vegetable + animal_product
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)


length = len(food_stuff_lt)
mid = length // 2

if length % 2 == 0:
    middle_items = food_stuff_lt[mid - 1 : mid + 1]
else:
    middle_items = food_stuff_lt[mid : mid + 1]

print(middle_items)

print(food_stuff_lt[0:3])
print(food_stuff_lt[length-4:length-1])
del food_stuff_lt

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonis' in nordic_countries)
print('Iceland' in nordic_countries)