# Shallow copy
a = [1, 2, [3, 4]]
b = list(a)
print(b is a)  # False
b.append(100)
print(b)  # [1, 2, [3, 4], 100]
print(a)  # [1, 2, [3, 4]]
b[2][0] = -100
print(b)  # [1, 2, [-100, 4], 100]
print(a)  # [1, 2, [-100, 4]]

# Deep copy
import copy
a = [1, 2, [3, 4]]
b = copy.deepcopy(a)
b[2][0] = -100
print(b)  # [1, 2, [-100, 4]]
print(a)  # [1, 2, [3, 4]]