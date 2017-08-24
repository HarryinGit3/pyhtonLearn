a_list=[1,2,4,5,76]

#d={key1:value1,key2:value2}
d={'apple':1,'pear':2,'orange':3}
print(d['apple'])
del d['pear']
print(d)
d['b']=20
print(d) #字典是没有顺序的容器
d={'apple':[1,2,3],'pear':{1:3,2:'ss'},'orange':3}
print(d)
print(d['pear'][2])