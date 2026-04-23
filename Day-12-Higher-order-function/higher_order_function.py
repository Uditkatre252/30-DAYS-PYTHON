def sum_numbers(nums):
    return sum(nums)
print(sum_numbers([1, 2, 3, 4, 5]))

def higher_order_function(f,lst):
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 8])
print(result)

numbers = [1, 2, 3, 4, 5]
def square(x):
    return x** 2
result = map(square, numbers)
print(list(result))