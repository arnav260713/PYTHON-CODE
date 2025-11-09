class Employes:
    def _init_(self, name, salary):
        self.name = name
        self.salary = salary
        print(f"Employee {self.name} is created with salary {self.salary}.
    def_del_(self):
    print(f"Emplee {self.name} is deleted from memory.")
def employee_details():
    emp1= Employee("somya",50000)
    print(f"Employee Name: {emp1.name}")
    print(f"Employee Name: {emp1.salary}")
    del emp1
    print("Employee object is deleted manually inside the function.")
employee_details()
print("End of program")
