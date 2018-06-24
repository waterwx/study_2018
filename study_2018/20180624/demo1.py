#coding = utf-8
class animal:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def say(self):
        print("你的名字是 %s" % self.name)
        print("你的年龄是 %d" % self.age)

dog = animal("小花", 2)
dog.say()
