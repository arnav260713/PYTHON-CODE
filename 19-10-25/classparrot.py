class parrot:
    species = "bird"
    def_init_(self,name, age):
       self.name = name
       self.age = age
parrot1 = parrot("blue", 10)
parrot2 = parrot("kiwi", 15)
print(f"\nall parrot are of species: {parrot.species}")
print(f"{parrot1.name} is {parrot1.age} years old.")
print(f"{parrot2.name} is {parrot2.age} years old.")