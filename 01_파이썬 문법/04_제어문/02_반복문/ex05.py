# range() 함수
# : 범위를 생성하는 함수
# * 구조 : range(초기값, 종료값+1, 증감값)

# range(5)        : 0 1 2 3 4
# range(1, 11)    : 1 2 3 4 5 6 7 8 9 10
# range(1, 10, 2) : 1 3 5 7 9

# 1 ~ 10까지 출력하기
for i in range(1, 11):  # 1 ~ 10
    print(i, end=' ')
print()

# -20 ~ 20까지 출력하기
for i in range(-20, 21, 1):
    print(i, end=' ')
print()

# 10 ~ 1까지 출력하기
for i in range(10, 0, -1):
    print(i, end=' ')
print()