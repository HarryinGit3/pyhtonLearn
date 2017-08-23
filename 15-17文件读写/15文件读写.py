#coding:utf-8

text = "This is my first test.\nThis is next line.\nThis is last line"
my_file= open('my_file.txt','w')
my_file.write(text)
my_file.close()