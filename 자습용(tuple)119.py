list_statements.py
# # list는 변수마다 값을 할당해서 사용하기에, 관리의 어려움이 있으므로
# # 한 변수에 값을 집합시켜놓은 것.
# a = "김돌쇠"
# b = "김갑돌"
# c = "김갑순"
# print(a)
# print(b)
# print(c)

# # 하나의 변수로 여러개의 데이를 관리
# # list의 경우에 [] 대괄호를 사용하여 데이를 집합
# lista = ["a", "b", "c", "d", "e", "f", "g"]

# # list안의 각각의 값에 접근할때에는 index를 사용
# print(lista[0])
# print(lista[1])
# print(lista[2])

# # 여러개의 데이터를 범위를 지정해서 가져오고 싶을때는 slicing사용
# # 슬라이싱의 결과값은 같은 list로 출력
# # 0~5번째까지 출력
# print(lista[:5])
# # 0~5번째까지 출력한 결과물의 type출력
# print(type(lista[:5]))

# # 문자열은 메모리 내부적으로 list와 유사한 자료구조
# # 문자열은 값을 추가하거나 수정할수가 없다.
# # list는 값의 추가,삭제,수정이 가능한 구조를 가지고 있다.

# # list안에 list의 값을 조회하는 방법
# list_ex1 = ['a', 'b', 'c', [1, 2, 3]]
# number = list_ex1[3]
# print(number[0]+number[2])
# print(list_ex1[3][0]+list_ex1[3][2])

# # 리스트 더하기 또는 곱하기
# # list를 2개 만들어서, 
# # 2개를 더해서 하나의 리스트로 만들어보자 그리고 출력
# lista = [1,2,3]
# listb = ['a', 'b', 'c']
# listc = lista + listb
# print(listc*10)

# # 리스트 길이 구하기 : len
# print(len(lista))

# # 리스트 값 수정하기 
# # -> 1개의 값만 바꿀땐 1개의 값으로 대체
# # -> 여러값을 바꿀땐 다른 리스트로 대체
# lista = [1,3,5,6,7,9]
# lista[1] = 4
# print(lista)
# lista[2] = [5,5,5]
# print(lista)

# # 리스트 요소 개수 세기
# lista = ["1", "1", "2", "4"]
# counta = lista.count("1")
# print(counta)

# # 리스트 요소 삭제하기 : del 변수[index]
# lista = [1,4,5,7,8,9]
# del lista[3]
# print(lista)

# # 리스트 요소 삭제하기 : remove
# lista = [1,9,4,9,5,7,8,9]
# lista.remove(9)
# print(lista)

# # 특정한 9라는 값을 모두 제거하려면 어떻게 해야 할까
# # del, for range
# lista = [1,3,9,3,5,6,9,9]
# # 방법3
# for a in range(0, len(lista)):
#     if 9 in lista:
#         lista.remove(9)
#     else:
#         break
# print(lista)

# # # 또는 append 사용
# # listb.append(lista[a])

# # # 방법1
# # count = 0
# # for a in range(0, len(lista)):
# #     if lista[a-count] == 9:
# #         del lista[a-count]
# #         count = count + 1
# # print(lista)

# # 방법2
# listb = []
# for a in range(0, len(lista)):
#     if lista[a] !=9:
#         # listb = listb + [lista[a]]
#         listb.append(lista[a])
# print(listb)

# list append : 리스트 맨 뒤로 추가
lista = [1,3,5,7]
# 9,10을 append이용해서 추가해서 출력
lista.append(9)
lista.append(10)
print(lista)

# list insert : index를 지정하여 추가 가능
# lista.index(2,"abc") 추가 후 출력
lista.insert(2,"abc")
print(lista)

# list extend : iterable객체를 list에 추가할때 사용
# extend는 각 요소를 꺼내어 맨 뒤에 추가
listb = [10,20,30]
# lista.append(listb)
lista.extend(listb)
print(lista)

# list의 정렬은 sort()함수 사용
# sort()는 오름차순 정렬
# reserse=True 옵션을 주면 내림차순 정렬
numa = [5,3,18,4,2,1]
numa.sort(reverse=True)
print(numa)

chlist = ['brad', 'john', 'abc']
chlist.sort()
print(chlist)

# list뒤집기 : reverse()
chlist.reverse()
print(chlist)

# list위치 반환 : index()
lista =  ['김돌쇠', '김갑돌', '김갑순', '김철수']
print(lista.index('김철수'))

# 마지막요소 끄집어 내기 : pop()
# remove and return last value
lista =  ['김돌쇠', '김갑돌', '김갑순', '김철수']
lista.pop()
print(lista)

a = 10
b = 20
result = 0
# 만약에 ~하면 result = 1 그렇지 않으면 result = -1

# 문자 리스트를 문자열로 만들기
lista = ["hello", "world", "python"]
st2 = "".join(lista)
print(st2)
# 문자열을 문자 리스트로 만들기
sta = "hello world python"
mySta1 = list(sta)
mySta2 = sta.split()
print(mySta2)