def cube(number):
    return number*number*number
def divisiblebythree(number):
    if number%3==0:
        return cube(number)
    else:
        return False
print(divisiblebythree(6))