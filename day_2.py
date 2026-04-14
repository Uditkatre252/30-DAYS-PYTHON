# age = 22
# height = 6.55
# complex_number =  35 + 2j

# # area of triangle
# base = float(input("Enter base: "))
# height = float(input("Enter height: "))
# print(f"Area of the triangle is {0.5*base*height}")
#
# # Perimeter of Triangle
# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# c = int(input("Enter a number: "))
# print(f"Perimeter of the triangle is {a+b+c}")

# # Area and perimeter of Rectangle
# length = float(input("Enter a length: "))
# width = float(input("Enter a width: "))
# print(f"Area of the Rectangle is {length*width}")
# print(f"Perimeter of the Rectangle is {2*(length*width)}")

# # Slope,x-intercept,y-intercept
# m = 2
# b = -2
# slope = m
# x_intercept = b
# y_intercept = -b/m
# print(f"slope {slope}")
# print(f"x_intercept {x_intercept}")
# print(f"y_intercept {y_intercept}")

# a = len("python")
# b = len("dragon")
# print(a!=b)
#
# result = 'on' not in 'python' and 'on' not in 'dragon'
# print(result)
#
#
# print( "jargon" in "I hope this course is not full of jargon")
# sam = len("python")
# con_float = float(sam)
# con_str = str(con_float)
# print(con_str)

# num = int(input("Enter a number: "))
# if num%2==0:
#     print("Number is even")
# else:
#     print("Number is odd")

# floor_division = 7 // 3
# int_converted = int(2.7)
# if floor_division == int_converted:
#     print('Floor division is equal to 0')
# else:
#     print('Floor division is not equal to 0')
#
# if '10' == 10:
#     print(True)
# else:
#     print(False)

# hour = int(input("Enter hours"))
# rate_per_hour = int(input("Enter rate per hour"))
# print(f"Your weekly earing is {hour*rate_per_hour}")

# years = int(input("Enter number of years you have lived"))
# seconds_in_a_year = 31536000
#
#
# total_lived_seconds = years*seconds_in_a_year
#
# print(f"you have lived for {total_lived_seconds} seconds")


# Loop through numbers 1 to 5
for i in range(1, 6):
    # Print the base number, followed by its powers: i^0, i^1, i^2, and i^3
    # This matches the pattern: n, 1, n, n^2, n^3
    print(f"{i} {i**0} {i**1} {i**2} {i**3}")
