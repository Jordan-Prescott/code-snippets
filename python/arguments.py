# Forcing positional arguments to be passed by keyword
# This is a Python 3.8 feature

def func(x, y, /):
    pass

func(1, 2)  # Valid
func(1, y=2)  # Invalid

#Force keyword arguments
def read_data(filename, *, debug=False):
    pass

read_data('data.txt', debug=True)  # Valid
read_data('data.txt', True)  # Invalid

#This can improvce code readability
