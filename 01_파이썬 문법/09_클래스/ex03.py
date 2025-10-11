# 인스턴스 변수, 메소드
# 클래스 변수, 메소드

class Student:
    # 인스턴스 변수 : 객체마다 고유한 값으로 사용하는 변수
    # name = ''
    # age = 0
    # tel = ''

    # 클래스 변수 : 객체 간의 공유할 값으로 사용하는 변수
    count = 0       # 학생수
    student_list = []

    # 인스턴스 변수 접근    : self.변수
    # 클래스 변수 접근      : 클래스명.변수

    def __init__(self, no, name, major):
        self.no = no
        self.name = name
        self.major = major
        Student.count += 1
        Student.student_list.append(self)

    def __str__(self):
        return '{} / {} / {}'.format(self.no, self.name, self.major)

    # @이름     : 데코레이터
    #           - 해당 클래스나 메소드의 기능/용도를 명시하는 역할

    # 클래스 메소드
    # @classmethod : 해당 메소드를 클래스 메소드로 명시
    # * 클래스 메소드는 첫번째 매개변수로 클래스(cls) 를 받아온다
    # * 인스턴스 메소드는 첫번째 매개변수로 인스턴스(self) 를 받아온다
    @classmethod
    def show_info(cls):
        for student in cls.student_list:
            print( str(student) )

# -----------------------------------------------------------------
s1 = Student('김조은', 20, '010-1111-2222')
s2 = Student('박조은', 30, '010-2222-2222')
s3 = Student('황조은', 40, '010-3333-4444')


# 클래스 변수
print('{} 명의 학생이 참여하였습니다.'.format(Student.count) )
print( s1.count )   # 인스턴스 변수 (클래스 변수가 공유됨)
print( s2.count )   #   - 각 다른 객체로 접근해도 클래스 변수 값에 접근
print( s3.count )

# 클래스 메소드
Student.show_info()
