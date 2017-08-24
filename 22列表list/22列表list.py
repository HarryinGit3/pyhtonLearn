a= [5,6,2,32,1]
a.append(100)
a.insert(1,100)
a.remove(100) #移除第一个出现的值
print(a)
print(a[0])
print(a[-1]) #-1代表最后一位
print(a[0:3])
print(a[:3])
print(a[3:5])
print(a[-3:])
print(a.index(2))
print(a.count(100))
a.sort()
print(a)
a.sort(reverse=True)
print(a)