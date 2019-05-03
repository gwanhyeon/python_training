# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# 딕셔너리 Key/Value
phones = {'fruit' : 'apple', 'bird' : 'peacock'}
print(phones['fruit'])

# 딕셔너리 삽입
phones['class'] = 'math'
print(phones)
"""
사전 자료형 a 에 'class': 'math' 쌍이 추가된 것을 볼 수 있습니다.

또한 del a[key] 와 같이 입력하면 해당하는 key : value 쌍을 삭제할 수 있습니다.

사전 자료형은 리스트처럼 인덱스를 참조하는 것이 아닌 key 를 이용하여 상응하는 값을 참조하기 때문에 순서에 상관없이 데이터를 다룰 수 있습니다.
"""
# 딕셔너리 삭제
del phones['fruit']
print(phones)

phones1 = {'model' : '모델명','manufacturer':'제조사','year':'출시연도'}
del phones1['year']
print(phones1)

