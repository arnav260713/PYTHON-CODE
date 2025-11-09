from abc import ABC, abstractmethod
class animal(ABC):
    @abstractmethod
    def move(self):
        pass
class human(animal):
    def move(self):
        print("Humans can walk and run")
    class dog(animal):
        def move(self):
            print("dogs can walk and run on their four legs")
human = human()
dog = dog()
human.move()
dog.move
