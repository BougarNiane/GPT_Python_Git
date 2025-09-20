# 조건 연산자
# x if 조건식 else y
# - 조건식의 결과가 참이면 x
#   거짓이면 y 를 반환하는 연산자

m = 100
n = 200
result = m if (m - n) > 0 else n
print('result : {}'.format(result))