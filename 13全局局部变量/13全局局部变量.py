APPLE = 100 #全局变量一般是全都大写
def fun():
    global a
    a = 20 #a就是局部变量
    print(a)
    return a+100
print(fun())
print(APPLE)
print(a)