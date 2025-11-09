class myclass:
    _privatevar = 100
    def _privmeth(self):
        print("this is a private method,accessible only in class")

    def hello(self)
        print("accessing private variable inside the class:",self ._privatevar)
        self ._privmath()
obj= myclass()
obj.hello()