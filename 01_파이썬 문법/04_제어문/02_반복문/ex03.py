# 컬렉션 반복

# [] : 리스트
menu = ["샌드위치", "김밥", "컵라면", "파인애플", "햄버거"]

for food in menu:
    print("오늘 점심 메뉴 : {}".format(food))
print()

# () : 튜플
stars = ("마동석", "김태리", "박보검", "김하늘", "이정재")
for star in stars:
    print(star)
print()

# {} : 세트
burger_king_set = {"와퍼", "프렌치프라이", "콜라"}
for item in burger_king_set:
    print(item)
print()

# {"key": "value"} : 딕셔너리
users = {
    "joeun": "123456",
    "user": "user1004",
    "admin": "1q2w3e"
}
for id, pw in users.items():    ## items() : 내장함수. key, value
    print("아이디 : {}, 비밀번호 : {}".format(id, pw))