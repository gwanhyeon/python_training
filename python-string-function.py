# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

a = "Contrary to popular belief, Lorem Ipsum is not simply random text."

# 't' 의 개수 출력
print(a.count('t'))
# 가장 먼저 나오는 'i' 의 인덱스 출력
print(a.index('i'))

# 모두 대문자로 바꾼 뒤 출력
print(a.upper())
# 모두 소문자로 바꾼 뒤 출력
print(a.lower())

# 'a' 를 'b'로 바꾼 뒤 출력
print(a.replace('a','b'))

# 문자열을 공백(" ")으로 나눈 것을 출력
print(a.split(' '))    # split 자료형은 반환 값이 list 값이다! 주의 할것!

# 문자열 삽입

print(" ".join(a));	# => 'a b c'
print(",".join(a));  # => 'a,b,c'
"""
5
23
CONTRARY TO POPULAR BELIEF, LOREM IPSUM IS NOT SIMPLY RANDOM TEXT.
contrary to popular belief, lorem ipsum is not simply random text.
Contrbry to populbr belief, Lorem Ipsum is not simply rbndom text.
['Contrary', 'to', 'popular', 'belief,', 'Lorem', 'Ipsum', 'is', 'not', 'simply', 'random', 'text.']
C o n t r a r y   t o   p o p u l a r   b e l i e f ,   L o r e m   I p s u m   i s   n o t   s i m p l y   r a n d o m   t e x t .
C,o,n,t,r,a,r,y, ,t,o, ,p,o,p,u,l,a,r, ,b,e,l,i,e,f,,, ,L,o,r,e,m, ,I,p,s,u,m, ,i,s, ,n,o,t, ,s,i,m,p,l,y, ,r,a,n,d,o,m, ,t,e,x,t,.

"""