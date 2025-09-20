# 다중 조건문
# - 위의 나온 조건이 만족하지 않을 때, (if)
#   아래의 조건을 확인하고 (elif)
#   모두 만족하지 않으면 else 문을 실행한다.

score = input("성적 : ")
score = int(score)

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")