#coding:utf-8

#class
class Calculator:
    name = 'Good Calculator'
    price =18
    def add(self,x,y):
        result =x+y
        print(result)
    def minus(self,x,y):
        result =x-y
        print(result)
    def times(self,x,y):
        print(x*y)
    def divide(self,x,y):
        print(x/y)
calcul=Calculator()
print(calcul.name)
calcul.add(10,11)

