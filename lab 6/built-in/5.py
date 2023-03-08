my_tuple = (True, True, True, True, 1, 'aa')

print(all(my_tuple))
#or
if all(my_tuple):
    print("All elements of the tuple are True.")
else:
    print("Not all elements of the tuple are True.")
