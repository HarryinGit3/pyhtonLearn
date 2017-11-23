import pickle
a_dict ={'da':111,2:[23,1,45],'23':{1:2,'d':'sad'}}

file =open('pickle_example.pickle','wb')
pickle.dump(a_dict,file)
file.close()