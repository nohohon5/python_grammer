class people():
    """
    定义一个人g
    """
    def __init__(self,name):
        self.name = name

    def my_name(self):
        print("my name is:"+self.name)

bobby = people("bobby") #创建一个对象
bobby.my_name()

"""
1.第一种initf方法称为类的初始化方法和构造方法，当创建了这个类的实例就会调用这个方法
2.self表示的是实例本身，在定义类的方法中是必有的，虽然在实例调用的函数的时候不需要传

我们创建了一个People类，People类有一个构造函数，当我们创建一个People类的对象时需要传入一个参数，创建的对象可以调用People类中的方法
"""
