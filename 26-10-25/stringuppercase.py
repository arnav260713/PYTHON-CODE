class IOString:
    def _init_(self):
        self.str1=""
    def get_String(self):
        self.str1=input("Enter a string")
    def print_str(self):
        print("Result is",self.str1.upper())
str1=IOString
str1.get_String()
str1.print_str()