# 가위바위보 게임

# choices = ['가위', '바위', '보']
# choice() : 리스트 요소 중 하나를 랜덤으로 선택
# r = random.choice(choices)
# print(r)

# 컴퓨터    : 가위 바위 보를 랜덤으로 선택
# 나        : 가위 바위 보를 입력
# 내가 질 때까지 게임을 계속 진행

# 가위바위보 게임 만들어보기

'''
import random
choices = ['가위', '바위', '보']

while True:
    com = random.choice(choices)  # 컴퓨터가 가위 바위 보 중 하나를 랜덤으로 선택
    me = input("가위 바위 보 중 하나를 선택하세요 : ")

    if me not in choices:   # 잘못된 입력 처리
        print("잘못된 입력입니다. 다시 선택하세요.")
        continue    # 반복문의 처음으로 돌아감
    
    elif com == me:  # 비길 때
        print("컴퓨터 : {}, 나 : {}".format(com, me))
        print("비겼습니다.")

    elif (com == '가위' and me == '바위') or (com == '바위' and me == '보') or (com == '보' and me == '가위'):
        print("컴퓨터 : {}, 나 : {}".format(com, me))
        print("이겼습니다.")
    
    else:  # 내가 졌을 때
        print("컴퓨터 : {}, 나 : {}".format(com, me))
        print("졌습니다. 게임을 종료합니다.")
        break   # 반복문 종료
'''

'''
import random

choices = ['가위', '바위', '보']
user = ''

while user != '그만':
    computer = random.choice(choices)
    user = input("가위바위보 입력 : ")
    print()

    print("컴퓨터 : {}".format(computer))
    print("나     : {}".format(user))

    if user not in choices:
        print("잘못 입력하셨습니다. 다시!")
        print()
        continue
    
    elif computer == user:
        print("비겼습니다.")
        print()

    elif (computer == "가위" and user == '바위') or (computer == '바위' and user == '보') or (computer == '보' and user == '가위'):
        print("이겼습니다.")
        print()
    
    else:
        print("졌습니다.\n")
        # print()
        print("----- GAME OVER -----\n")
        break
'''

import random
choices = ['가위', '바위', '보']
user = ''
win = True # 내가 이겼는지 여부

while win:
    computer = random.choice(choices)
    user = input("가위바위보 입력 : ")
    
    print("컴퓨터 : {}".format(computer))
    print("나     : {}".format(user))

    # 이겼을 때
    win1 = (user == '가위' and computer == '보')
    win2 = (user == '바위' and computer == '가위')
    win3 = (user == '보' and computer == '바위')

    if user == computer:
        print("비겼습니다!")
    elif win1 or win2 or win3:
        print("이겼습니다!")    
    else:
        win = False
        print("졌습니다!")