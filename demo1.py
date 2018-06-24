class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def say(self):
        print("yourname is %s "%self.name)
        print("yourage is %d"%self.age)


xiaoming = Person('xiaoming',12)
xiaoming.say()
