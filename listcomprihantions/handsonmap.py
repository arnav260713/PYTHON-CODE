def add_numbers(x,y):
    return x + y
def square_number(n):
    return n ** 2
list1= [1,2,3,4]
list2= [5,6,7,8]
addition = list(map(add_numbers, list1, list2))
print("Addition of two list:",addition)
numbers = [2,3,4,5]
squares = list(map(square_numbers , numbers))
print("Square of numbers:",squares)