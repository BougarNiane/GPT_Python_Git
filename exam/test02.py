def getStudent(no, name, major):
    student = {
        '학번': no,
        '이름': name,
        '전공': major
    }
    return student

no = input('학번 : ')
name = input('이름 : ')
major = input('전공 : ')

student = getStudent(no, name, major)

print('학번 :', student['학번'])
print('이름 :', student['이름'])
print('전공 :', student['전공'])
