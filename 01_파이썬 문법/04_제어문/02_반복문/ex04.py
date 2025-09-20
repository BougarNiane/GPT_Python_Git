# 중첩 반복문(이중 반복문)
# : 반복문 안에 또 하나의 반복문을 작성
# i : 2 ~ 9
# j : 1 ~ 9
# 구구단 출력하기
for i in range(2, 10):      # 2 ~ 9
    for j in range(1, 10):  # 1 ~ 9
        print("{} x {} = {}".format(i, j, i * j))
    print()     # 단이 바뀔 때마다 줄바꿈