# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

a=[1,2]
b=['a','b','c']
print(a+b)
print(a*4)
# 원소 인덱싱
mylist =[1,2,3,4,5]
print(mylist[0] + mylist[1])

# 원소 슬라이딩 
a=[1,2,3,4,5]
print(a[1:4]) # a[1]부터 a[4]까지
print(a[:3])	 # 처음 : a[3]까지
print(a[2:])	# a[2]부터 마지막

# 원소 변경시
my_list = ['a', 1, 2, 3, 'b', ['apple', 'banana'], 4]
print(my_list)
print(my_list[4])
my_list[3] = 'hello'
print(my_list)
print(my_list[:6])
print(my_list[5][1])