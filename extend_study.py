class people(object):
    __sex = "male" #私有属性
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("my name:",name)
        print("age is:",age)

    def run(self):
        print("{} can run".format(self.name))

    def not_run(self):
        print("{} can not run".format(self.name))

    def __findsex(self):
        print("小朋友是{}".format(self.__sex))

    def seceret(self):
        self.__findsex()

class child(people):
    def eat(self):
        print("{} can eat rice".format(self.age))
#子类可以重构父类的方法
    def run(self):
        print("{}长大了，她可以决定跑步还是不跑步".format(self.name))
#子类继承父类时，如果父类有构造函数，那么我们也需要调用这个构造函数并进行传参。
alice = child("alice",3)
alice.run()
alice.eat()
#我们可以在类中调用__age和__run，但是我们创建一个类对象时，我们不可以调用私有属性和方法。
alice.seceret()
