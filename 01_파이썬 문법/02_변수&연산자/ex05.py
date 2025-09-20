# 논리 연산자
# and   : A and B 와 같은 조건에서,
#         A 와 B 모두 True(참)일 때, 결과가 True(참)이다.
# 쇼트서킷
# A and B : A가 False 이면 B를 검사하지 않는다.

# or     : A or B 와 같은 조건에서
#          A 와 B 둘 중 하나의 조건이라도 True(참)이면, 결과 True(참)이다.
# 쇼트서킷
# A or B  : A가 True 이면 B를 검사하지 않는다.

#not     : True 이면, False 로, False 이면, True 로 변경한다.

a = 10
b = 5

result1 = a > 7 # True
result2 = b > 7 # False
result3 = a < 7 # False
result4 = b < 7 # True

print('{} > 7 and {} > 7 : {}'.format(a,b, result1 and result2)) # 1
print('{} > 7 or {} > 7 : {}'.format(a,b, result1 or result2))   # 2 쇼트서킷
print('{} < 7 and {} < 7 : {}'.format(a,b, result3 and result4)) # 3 쇼트서킷
print('{} < 7 or {} < 7 : {}'.format(a,b, result3 or result4))   # 4

print('not : {} : {}'.format(a, not a))
print('not : {} : {}'.format(0, not 0))