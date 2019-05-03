"""
원하는 부분의 문자열을 뽑아내는 것을 슬라이싱 이라고 합니다.

a [ 시작번호 : 끝번호 ]와 같이 표현됩니다.
"""

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 문자열 인덱싱,슬라이싱
"""
슬라이싱시에 a[4:6] 일경우
0번 부터 인덱스로 시작해서 4번째의 경우의 값 ~ 6번째를 포함하지 않은 값까지 !
"""
a="123456"

print(a[4:6])


a = "hello"
print(a[0]);
print(a[1]);
print(a[2]);
print(a[3]);
print(a[4]);

a = "I loveCoffee"
print(a[0:6])

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 문자열 인덱싱,슬라이싱 
a = "hello"
print(a[0]);
print(a[1]);
print(a[2]);
print(a[3]);
print(a[4]);

a = "I love Coffee"
print(a[0:6])

a = "python is fun"
print(a[2])
print(a[5:11])