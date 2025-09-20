'''
    커피 1잔을 300원
    자판기에 금액을 입력하고
    커피의 잔 수에 따라서 남은 금액을 출력하세요.

    (입력 예시)
    입력 금액 : 1400원
    (출력 예시)
    커피 1잔, 1100원    
    커피 2잔, 800원    
    커피 3잔, 500원    
    커피 4잔, 200원    
'''

'''
money = input("입력 금액 : ")
money = int(money)

coffee = 300
i = 1

while money >= coffee:
    money -= coffee
    print("커피 {}잔, {}원".format(i, money))
    i += 1
'''

money = int(input("입력 금액 : "))

i = 0
while money >= 300:     # 남은 금액(잔돈)
    money = money - 300        # 커피 잔수
    i = i + 1
    print("커피 {}잔, {}원".format(i, money))