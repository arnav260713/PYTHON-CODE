class Reverse:
    def __init__(self, s=""):
        self.s = s

    def reversed_string(self):
        return self.s[::-1]


# Take input from user
user_input = input("Enter a word: ")

# Create object of Reverse class with user input
rev = Reverse(user_input)

# Display reversed string
print("Reversed string:", rev.reversed_string())