#加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。可变参数

def add(*numbers):
    sum = 0
    for n in numbers:
        if type(n) == int or type(n) == float:
            sum = sum + n
        else:
            n = 0
            sum = sum + n
    return sum

print(add(2,3,'as'))


def person(name,age=35):
    print("名字:",name)
    print("年龄:",age)

person("hh",50)
person("lll") #不传参会使用默认参数


