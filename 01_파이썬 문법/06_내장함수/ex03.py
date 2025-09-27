# C언어, Python, Java
# 0, 1, 2
# enumerate(  )
'''
    (0, 'C언어'),
    (1, 'Python'),
    (2, 'Java'),
'''
prog = ['C언어', 'Python', 'Java']
for item in enumerate(prog):
    print(item)
print()
for item in enumerate(prog):
    print('{}. {}'.format( item[0]+1, item[1] ))
print()
    
    
# range(10)     : 0 1 2 3 4 5 6 7 8 9
for i in range(10):
    print(i, end=' ')
print()
# range(1,11)     : 1 2 3 4 5 6 7 8 9 10
for i in range(1, 11):
    print(i, end=' ')
print()
# range( ?, ?, ? )
# 1 3 5 7 9 11 13 15 17 19
for i in range(1, 20, 2):
    print(i, end=' ')
print()
# 2 4 6 8 10 12 14 16 18 20
for i in range(2, 21, 2):
    print(i, end=' ')
print()

# len
li = ['월','화','수','목','금','토','일']
print(li)
print('li 의 요소의 개수 : {}'.format( len(li) ))
# sorted
# * 원본은 바뀌지 않는다!
# - 해당 리스트를 정렬한 새 리스트를 반환하는 함수
# sorted( 리스트, reverse=False )   : 오름차순
# sorted( 리스트, reverse=True )    : 내림차순
scores = [100, 90, 65, 80, 70]
print(scores)
print( sorted(scores) )
print( sorted(scores, reverse=True) )
print( sorted(scores, reverse=False) )
print(scores)
# sort
# * 원본을 정렬 해준다!
# - 해당 리스트를 정렬하여 갱신하는 함수
# 리스트.sort(reverse=False)       : 오름차순
# 리스트.sort(reverse=True)        : 내림차순
scores.sort(reverse=True)
print(scores)
scores.sort(reverse=False)
print(scores)
# zip
names = ['s1','s2','s3','s4','s5']
scores = [100, 90, 65, 80, 70]
for student in zip(names, scores):
    print(student)