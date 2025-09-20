# 반복문
#   : 조건을 만족할 때까지, 실행문을 반복하는 문장
# while 문

# while 조건식 :
#     반복 실행 문장
#     반복 실행 문장

# 1 ~ 10까지 반복하여 출력
i = 1
while i <= 10:
    print(i, end=' ')
    i = i + 1
print()

# 1 ~ 10까지 합계
a = 1
sum = 0
while a <= 10:
    sum = sum + a
    print(a, end='')

    if a != 10:
        print("+", end='')
    a = a + 1
print("={}".format(sum))
print("sum = {}".format(sum))