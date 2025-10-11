'''
    클래스 선언
    
    class 클래스명:
        
        # 생성자
        def __init__(self, 매개변수):
            생성자 내용
            
        # 소멸자
        def __def__(self):
            소멸자 내용
            
        # 메소드
        def 메소드명(self, 매개변수):
            메소드 내용
'''

class Person:
    # 생성자
    # None : 값이 없음을 의미하는 키워드
    def __init__(self, name=None, age=None, tel=None):
        # pass                # 에러방지용: 아무 동작도 하지 않는 키워드. 일단 가다만 잡고 내용은 나중에 작성할 때 사용
        self.name = name
        self.age = age
        self.tel = tel
        print('Person 객체 생성!')
        

    # 소멸자
    def __del__(self):
        print('Person 객체 소멸!')

    # 메소드
    def show_info(self):
        print('이름 : {}, 나이 : {}, 전화번호 : {}'.format(
            self.name, self.age, self.tel
            )
        )

# 객체 생성
# 변수명 = 클래스명()
# * 인스턴스 : 클래스를 통하여 생성된 객체
person = Person()       # 기본 생성

# 객체의 변수 접근
person.name = '김조은'  # 값을 넣어줌
person.age = 20
person.tel = '010-1234-1234'

print('이름 : {}'.format(person.name))
print('나이 : {}'.format(person.age))
print('전화번호 : {}'.format(person.tel))

# 매개변수를 전달하여 객체 생성
person2 = Person('박조은')
person3 = Person('박조은', 20)
person4 = Person('박조은', 20, '010-1234-1234')

print('이름 : {}'.format(person2.name))
print('나이 : {}'.format(person2.age))
print('전화번호 : {}'.format(person.tel))