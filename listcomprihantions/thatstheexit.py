for i in range(1, 11):
    print("Value of i:", i)
    if i == 5:
        print("i has become 5, exiting the program...")
        exit()

print("This line will not be executed because of exit().")