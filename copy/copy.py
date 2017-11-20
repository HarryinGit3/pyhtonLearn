import copy

a = [1,2,3]
b = a
c=copy.copy(a)
d=copy.deepcopy(a) #完完全全copy过来
print(id(a))
#print(a)
print(id(b))
#print(b)
