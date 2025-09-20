# continue
# - 뒤의 남은 실행문을 건너뛰고,
#   다음 반복문으로 넘어가는 키워드

# 짝수의 합계
a = 0
sum = 0
while a <= 20:
    a = a + 1
    # 홀수의 경우
    if a % 2 == 1:
        continue
    sum = sum + a

print("1~20 사이의 짝수의 합계 : {}".format(sum))