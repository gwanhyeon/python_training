# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


"""
formatting 을 지정 할때는 %s, %d 등을 사용하고, 그 뒤에 %(변수, 값)을 입력해준다.
값이 여러개 일 경우는 ","로 여러 개를 넣어 줄 수 있다.
"""

# a와 b에 값을 저장
a = "apple"
b = 10

# 밑줄친 부분을 알맞게 수정해 봅시다.
c = "%s가 %d개 있습니다" %(a,b)

print(c)