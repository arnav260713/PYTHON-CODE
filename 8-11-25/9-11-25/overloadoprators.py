class comparenumbers:
    def_init_(self, value):
    self.value = value
    def__it__(self, others):
    return self.value < other.value
    def __eq__(self, other):
        return self.value == other.value
ob1 = comparenumber(3)
ob2 = comparenumber(4)
ob3 = comparenumbers(3)
print("ob1 < ob2:", ob1 < ob2)
print("ob2 < ob1:", ob2 < ob1)
print("ob1 == ob2:", ob1 == ob2)
print("ob1 == ob3:", ob1 == ob3)