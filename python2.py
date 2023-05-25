# set은 (수학)집합이라고 부르기도 한다.
# set의 특성은 딕셔너리와 마찬가지로, 
# index가 없고, 중복이 없다.
s1 = {'이름', '나이', '성별'}
# list의 중복을 제거하기 위해서
# list을 가지고 set으로 형변환 시키는 방식도
# 많이 사용
# print(len(s1))
# 집합의 개수 구하는 함수 : len
# s1 = set(['이름', '나이', '성별'])
# print(s1)
# print(s2) 


# 이 반 학생들의 혈액형 종류는총 몇 개 인가?
# A, B, AB -> 3개
lista = ['A','A','A','B','A','B','AB','O']
setA = set(lista)
print(setA)
print (len(setA))

# setA의 값을 하나씩 출력하려면? setA[0],setA[1]
for a in setA:
    print(a)

# 합집합
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8])
# 프로그래밍에서 | 이 기호는 or(또는)를 의미
# 프로그맹에서 &은 일반적으로 and(그리고)를 의미
# 엠퍼샌드 라고 부른다.
s3 = s1 | s2
print(s3)
s3 = s1 & s2
s3 = s1.intersection(s2)
print(s3)

# s2에서 s1을 차집합을 구해보자
# -, difference
print(s2.difference(s1))

# 집합에서 값 추가 : add
s1 = {1,2,3,4,5,6}
# 7을 추가한다음에 s1출력
s1.add(7)
print(s1)

# 값 여러개 추가시 update함수(딕셔너리와 동일)
# s1
# s2
# s1를 s2를 update
# s1출력

s1={1,2,3,4,5}
s2={4,5,6,7}
s1.update(s2)

# set값 삭제 시 removem, discard 함수 사용
s1 = {1,2,3,4,5,6}
s1.remove(6)
s1.discard(5)
print(s1)
# discard : remove와의 차이점은, 삭제할 값이
# 존재하지 않아도 에러가 발생하지 않는다는 점.

#boolean(불형)타입
# : in(또는 not in) 뒤에 iterable한 자료형 나온다.
# a in lista, a not in lista, a in dicta.keys()

# 비어있는 값들은 거짓, 값이 들어있으면 참
while 조건:
    실행문
for a in 리스트:
    실행문
listA = [1,2,3]
while listA:
    print('참입니다.')
    listA.pop

git add .  
git commit -m "커밋메시지"
git push origin main