#coding:utf-8

#class
class Calculator:
    def __init__(self,name,price,height):
        self.name=name
        self.p=price
        self.h=height;
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
calcul=Calculator('Good',15,100)
print(calcul.p)
calcul.add(10,11)