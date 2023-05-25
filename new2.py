# # # # 문자열 관련 주요 함수
# # # # count : 대상 문자열에 지정한 문자가 몇개가 있는 출력하는 함수
# # # a = "python"
# # # print(a.count('o'))

# # # # find : 대상 문자열에서 지정한 문자가 index에 있는 찾는 함수
# # # # index : find와 같은 기능
# # # print(a.find('o'))
# # # # 없는 문자를 찾을 떄는 -1 return
# # # print(a.find('x'))

# # # whatyouwant = input("아무런 문자나 입력해주세요")
# # # search = input("찾고자 하는 문자 1개면 입력해주세요")
# # # result = whatyouwant.find(search)
# # # print("요청하는 문자는 %s 번쨰에 있습니다"% result)

# # # 대소문자 변경 : upper() / lovwer()
# # a = "hello"
# # print(a.upper())
# # b = "HELLO"
# # print(b.lower())

# # # 문자열 양쪽 공백을 없는 함수 : strip()
# # a = "   Hello word  "
# # print(a.strip())

# # # myID = (input("id를 입력해주세요")strip()
# # # mypw = input("비멀본호를 입력해주세요")

# # #print("ID는 "+ myID" 이고 + "비밀번호는 "myPw)

# # # 문자열 대체 : replace()
# # a = 'I studied python'
# # a = a.replace('python', 'jave')
# # print(a)

# # # 공백을 기준으로 문자를 자르는 함수 : split()
# # a = "I studied python"
# # b = a.split()
# # print(b)

# # a = "I  studied  python"
# # b =a.split(" ")
# # print(b)

# # x = int (input("x값을 입력해주세요"))
# # y = 2.5 * pow(x, 2) + 3.3*x +6
# # print(y)

# a = input("첫번쨰 문자를 입력해주세요")
# b = input("첫번쨰 문자를 입력해주세요")
# c = input("첫번쨰 문자를 입력해주세요")
# abc = a[0]+ b[0]+c[0]
# print(abc)

# list안에 list의 값을 조화하는 방법
lis_ex1 = ['a', 'b', 'c', [1, 2, 3]]
number = lis_ex1[3]
result = number[0] + number[2]  
print(result)

# 리스트 더하기
# list를 2개를 선언하고 만들어서, 2개를 더해서 하나의 리스트로 만들어보자 그리고 출력

lista=[1,2,3]
listb=['a','b','c']
listc=lista+listb

#리스트 길이 구하기 : len

lista = [1,3,5,6,7,9]
lista[1]=4
print(lista)
lista[2]=[5,5,5]
print(lista)
# 리스트 요소 개수 세기
lista = ["1","2","3","4","1","1","3"]
counta=lista.count("1")
print(counta)

# 리스트 지정 숫자 갯수 삭제 하기
lista = [1,3,5,7,9,10]
del lista[4]
print(lista)

# 리스트요소 삭제 하기 : remove
listb = [1,3,5,7,9,10]
listb.remove(3)
print(listb)

# del, for range
listc(1,9,4,9,5,7,8,9)
del listc[1,3,7]
print(listc)

#list는 변수마다 값을 할당해서 사용하기에,
#관리의 어려움이 있으므로 한 변수에 값을
#집합시켜놓은 것.

# a="김돌쇠"
# b="김갑돌"
# c="김갑순"
# print(a)
# print(b)
# print(c)

#하나의 변수로 여러개의 데이터를 관리
#list의 경우에 []대괄호를 사용하여 데이터를 집합
# lista=["a","b","c","d","e","f"]

#list안의 각각의 값에 접근할때에는 index를 사용
# print(lista[0])
# print(lista[1])
# print(lista[2])
# print(lista[3])
# print(lista[4])

#여러개의 데이터를 범위를 지정해서 가져오고 싶을때는 slicing사용
#슬라이싱의 결과값은 같은 list로 출력
#0~5번째까지 출력
# print(lista[0:5])

#0~5번째까지 출력한 결과물의 type출력
# print(type(lista[0:5]))

#문자열은 메모리 내부적으로 list와 유사한 자료구조
#문자열은 값을 추가하거나 수정할 수가 없다.
#그러나 list는 값의 추가,삭제,수정이 가능한 구조를 가지고 있다.

#연습문제2
#list_ex1=['a','b','c',[1,2,3]]이라는 리스트가 있다.
#1)변수 number에 [1,2,3]을 담아 출력하라
#2)number에 담은 값중 1과 3을 더해 4를 출력하라
list_ex1=['a','b','c',[1,2,3]]
number=list_ex1[3]
print(number[0]+number[2])
print(list_ex1[3][0]+list_ex1[3][2]) #2가지 방법으로 해결할 수 있다.

#리스트 더하기 또는 곱하기
#list 2개 선언하고 만들어서, 2개를 더해서 하나의 리스트로 만들어보자, 그리고 출력

lista=[1,2,3]
listb=[4,5,6]
listc=lista+listb
print(listc*10)

#리스트 길이 구하기: len
print(len(lista))

#리스트 값 수정하기
# ->1개의 값만 바꿀땐 1개의 값으로 대체
# ->여러값을 바꿀땐 다른 리스트로 대체

lista=[1,3,5,6,7,9]
lista[1]=4
print(lista)
lista[2]=[5,5,5]
print(lista)

#연습문제3 요소 개수 세기
#lista["1","2","3","4","1","1","3"]
#리스트 중 "1"이 몇 개 있는지 세보시오
# lista=["1","2","3","4","1","1","3"]
# counta=lista.count("1")
# print(counta)

#리스트 요소 삭제하기 : del
#del 리스트명[인덱스] or del 리스트명[시작:끝]
# lista=["1","2","3","4","1","1","3"]
# del lista[0:4]
# print(lista)

#리스트 요소 삭제하기: remove
#위 리스트에서 원하는 값을 삭제하라
a=[1,3,5,7,9,10]
a.remove(3)
print(a) #remove는 하나의 값만 지운다. 또한 3이 2개있다고 해서 2개다 지워지지 않는다

#모든 특정한 숫자 9값을 삭제하려면?
#del, for range 이용해보자
lista=[1,3,5,7,9,10,9]

#방법1
count=0
for a in range(0,len(lista)):
    if lista[a-count]==9:
        del lista[a-count]
        count=count+1
print(lista)


#방법2
for a in range(0,len(lista)):
    if 9 in lista:
        lista.remove(9)
    else:
        break
print(lista)