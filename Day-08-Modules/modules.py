import random


def generate_full_name(first_name,last_name):
    return first_name+' '+last_name

def sum_two_nums(a,b):
    return a+b


# import random
# import string
#
#
# def random_user_id():
#     k = int(input('Enter number of Character'))
#     n = int(input('How much user Ids you want '))
#
#     char_pool = string.ascii_letters + string.digits
#
#     user_ids = []
#
#     for i in range(n):
#         uid = ''.join(random.choice(char_pool) for i in range(k))
#         user_ids.append(uid)
#     return user_ids

# ids = random_user_id()
#
# for uid in ids:
#     print(uid)

def rgb_color_gen():
    r_color = str(random.randint(0,255))
    g_color = str(random.randint(0,255))
    b_color = str(random.randint(0,255))

    return(f'#rgb({r_color},{g_color},{b_color})')

print(rgb_color_gen())



