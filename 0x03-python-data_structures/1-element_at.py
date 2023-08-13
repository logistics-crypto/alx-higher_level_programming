#!/usr/bin/python3
def element_at(my_list, idx):
    """Retrive an element from a list."""
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    return (my_list[idx])

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
