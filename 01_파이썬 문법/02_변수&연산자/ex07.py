# 멤버쉽 연산자
# - 어떤 값이 지정한 컬렉션에 포한되어 있는지 여부를 반환하는 연산자
# a in C        : 컬렉션 C 의 a 가 포함되면 True, 아니면 False
# a not in C    : 컬렉션 C 의 a 가 포함되지 않으면 True, 아니면 False

a = [1,2,3]
b = [4,5,6]

x = 3 in a
y = 10 in a
z = 100 not in b
print('x : {}'.format(x))
print('y : {}'.format(y))
print('z : {}'.format(z))