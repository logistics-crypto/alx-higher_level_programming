#!/usr/bin/python3
def no_c(my_string):
 copy = [x for x in my_string if x != 'c' and x != 'C']
 return ("".join(copy))

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
