# Given dictionary
data = {'Codingal':2,
'is': 2,
'best': 2,
'for': 2,
'Coding': 1
}
value_to_check = int(input("Enter the value to find its frequency: "))
frequency = list(data.values()).count(value_to_check)
print(f"The frequency of value {value_to_check} is: {frequency}")