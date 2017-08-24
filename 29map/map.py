#zip 迭代器
a = [1,2,3]
b = [4,5,6]
zip(a,b)
print(list(zip(a,a,b)))

for i,j in zip(a,b):
    print(i/2,j*2)

#lambda
def fun1(x,y):
    return (x+y)
fun2 =lambda x,y:x+y
print(fun2(4,5))
print(fun1(2,3))

#map
map(fun1,[1],[2])
print(list(map(fun1,[1,3],[2,6])))
