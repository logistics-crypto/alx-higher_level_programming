#!/usr/bin/python3
# 11-delete_at.py


def delete_at(my_list=[], idx=0):
    """Delete an item at a specific position in a list."""
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return (my_list)

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)
