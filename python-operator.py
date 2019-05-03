# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

a = 10
b = 4
c = 4.0

# a 를 b 로 나누기
result1 = a / b
print(result1)

# a 를 c 로 나누기
result2 = a / c
print(result2)

# a 를 b 로 나누었을때 나머지
remainder = a % b
print(remainder)


a = 1 + 2j
a.real	# 실수
print(a.real)
a.imag # 허수
print(a.imag)
a.conjugate() # 켤레복소수
print(a.conjugate)
abs(a) # 복소수 절대값 2.23606 .....
print(abs(a))