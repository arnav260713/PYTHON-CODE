# 1. Create a tuple with different datatypes

mixed_tuple = ("Sowmya", 21, 4.11, True)

print("1. Mixed Tuple:", mixed_tuple)

# 2. Create another tuple of integers

int_tuple = (1, 2, 3, 4, 5)

print("\n2. Integer Tuple:", int_tuple)

# 3. Create a new tuple by adding 9 to the previous tuple

# Since tuples are immutable, we cannot directly add elements.

# Instead, we create a new tuple and concatenate.

new_tuple = int_tuple + (9,)

print("\n3. Integer Tuple after adding 9:", new_tuple)

# 4. Count the occurrences of an element in the tuple

count_of_3 = new_tuple.count(3)

print("\n4. Count of 3 in new_tuple:", count_of_3)

count_of_9 = new_tuple.count(9)

print(" Count of 9 in new_tuple:", count_of_9)

# 5. Perform slicing on the tuple

print("\n5. Slicing Examples:")

print(" First 3 elements:", new_tuple[:3]) # from index 0 to 2

print(" Last 3 elements:", new_tuple[-3:]) # last 3 elements

print(" Middle elements (index 2 to 4):", new_tuple[2:5]