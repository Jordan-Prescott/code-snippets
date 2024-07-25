
nums = [1,2,3,4,5]

# Generator Expression
# Snippet 1
squared_nums = (num ** 2 for num in nums)
print(squared_nums)  # Output: <generator object <genexpr> at 0x7f8b1c7b3d60>

# Generators can only be iterated once and then that value is lost from memory
squared_nums.__next__()  # Output: 1

for num in squared_nums:
    print(num) # Output: 4, 9, 16, 25
    
# Snippet 2
# Here we are using a generator expression to calculate the sum of squares of the numbers in the list
sum_of_squares = sum(num ** 2 for num in nums)
print(sum_of_squares)  # Output: 55