
nums = [1, 2, 3, 4, 5]
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
values = [10, 20, 30, 40, 50, '60', 'N/A']

# List Comprehension
# Snippet 1
squared_nums = [num ** 2 for num in nums]
print(squared_nums)  # Output: [1, 4, 9, 16, 25]

# Snippet 2
share_names = [stock['name'] for stock in portfolio]
print(share_names)  # Output: ['IBM', 'AAPL', 'FB', 'HPQ', 'YHOO', 'ACME']
print(type(share_names))  # Output: <class 'list'>

# Set Comprehension
# Snippet 3
share_name = {stock['name'] for stock in portfolio}
print(share_name)  # Output: {'IBM', 'AAPL', 'FB', 'HPQ', 'YHOO', 'ACME'}
print(type(share_name))  # Output: <class 'set'>

# Dictionary Comprehension
#snippet 4
share_names = {stock['name']: stock['shares'] for stock in portfolio}
print(share_names) # Output: {'IBM': 100, 'AAPL': 50, 'FB': 200, 'HPQ': 35, 'YHOO': 45, 'ACME': 75}
print(type(share_names))  # Output: <class 'dict'>

# Nested List Comprehension
# Snippet 5
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Error Handling in List Comprehension
# Snippet 6
def to_int(val):
    try:
        return int(val)
    except ValueError:
        return None

data_1 = [to_int(val) for val in values]
print(data_1)  # Output: [10, 20, 30, 40, 50, 60]

data_2 = [to_int(val) for val in values if to_int(val) is not None]
print(data_2)  # Output: [10, 20, 30, 40, 50, 60]

data_3 = [val for x in values if (val := to_int(x) is not None)]
print(data_3)  # Output: [10, 20, 30, 40, 50, 60]