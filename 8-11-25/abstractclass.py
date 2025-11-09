from abc import ABC, abstractmethod
class base(ABC):

    def display(self):
        print("This is the display method of base class")

    @abstractmethod
    def show(self):
        pass

class derived(base):

    def show(self):
        print("This is the show method of the dervied class")

obj = derived()
obj.display()
obj.show
