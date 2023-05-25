# # # tuple은 변경불가능한 자료형으로서, ()통해 표현
# # t1 = (1,2,'a','b')
# # print(t1)
# # # 인덱싱, 슬라이싱 둘다 리스트와 동일하게 허용
# # print(t1[0])

# # # 삭제,변경 불가
# # del t1[0]
# # print(t1)

# # # 튜플을 사용하는 이유는 개발자가 해당 자료를 수정하지 못하도록
# # # 강제적으로 지정한것.
# # # 리스트에 비해 메모리 효율적

# # # 파이썬에서의 dictionary는 다른 language의 map 또는 hashmap과 유사한 자료형
# # # json이라는 자료형태와도 유사하다.

# # # 딕셔너리 자료형은 key와 avlue로 이루어져있다.
# # # 영어사전에서 단어와 뜻으로 이루어져있것에서 유래.

# # dic1 = {'이름':'홍길동','나이':25, '성별':남, '성별':'여'}

# # print(dic1)
# # result = {'1':80, '2':90, '3':100, '4':10}
# # print(result)
# # print(dic1)

# # # 딕셔너리의 기본호출 방식은 변수명[key], 변수명.get(key)
# # print(dic1['나이'])
# # print(dic1.get['나이'])
# # # 리스트는 a = [value, ...] 딕셔너리는 a = {key:value, ...} 
# # # 튜플은 a = (value, ...) 딕셔너리와는 튜플은 a[index], 딕셔너리는 a[key]

# # #딕셔너리의 특징2
# # #key와 value로 이루어져 있다보니, 순서가 의미 없다. index로 접근 불가
# # #키는 중복이 허용되지 않고 값은 중복이 허용 된다.
# # #리스트/튜플처럼 인덱스(순서)를 통해 값을 가져 오지 않고,
# # #key를 가지고 value검색할떄 해시함술르 통해
# # #index를 찾다보니, 매우 빠른 속도를 보장.

# # dic1 = {'이름':'홍길동','나이':25, '성별':남, '성별':'여'}
# # # key:value 추가
# # dic1['신분']='학생'
# # print(dic1)

# # 딕셔너리에서 키를 이용한 key:value 삭제
# del dic1['성별']
# print(dic1)

# # 딕셔너리에서 key목록만을 뽑아낼때
# # iterable한 형태로 data가 뽑아져 나오므로 for문 사용가능
# keyList = dic.keys()
# print(keyList)
# # 위의 keyList에서 각각의 값을 출력해보자.
# for a in keyLiist:
#     print([k])
# # key를 출력해주는 for문안에서 value도 같이 출력해도록 해보자.
# for b in keyList:
#     print(b)
# # 위의 for문을 활용해서, key가 담긴 list를 만들고, value가 담긴 list를 만들어
# # 각각 출력 해보자.
# for c in keylist:
#     print(c)
# # value목록을 뽑아낼때는 .values()를 사용
# for k in dic1.values():
#     print(k)
#     #key을 출력해주는 for문안에서 value도 같이 출력하도록 해보자.
# for k in keyList:    
#     tempList1.append(a)
#     # key을 출력해주는 for문안에서 value도 같이 출력하도록 해보자.
#     tempList2.append(dic1[k])
# print(tempList1)    
# print(tempList2)

# #딕셔너리의 확장 : update함수
# dic1 = {"a":1, "b":2, "c":3}
# dic2 = {"a":1, "d":4, "f":3}
# dic1.update(dic2)
# print(dic1)

# 딕셔너리 생성
# dic11 = {"이름":"홍길동", "나이:30," "성별":"남성"}

# dic1 = {'이름':'홍길동','나이':25, '성별':남, '성별':'여'}
# # key:value 추가
# dic1['신분']='학생'
# print(dic1)

# lista = ['A','A','B','O','AB', 'ab']
# dicta = {'A':2, "B":1, "O":2, }

# 딕셔너리로 변환해서 출력 해보자.
# 예를들어 'A':2, 'B':1, 'O':2 이렇게 출력되도록 코딩 해보자
# hint : a not in dicta.keys()
# 검사 

dicta = {}
for a in lista:
    if no in dicta.keys():
        dicta['A']= 1
    else:
      dicta[a] = dicta[a] +1
print(dicta) # {'A': 2, 'B': 1, 'O':2, 'AB' : 2}
# 방법2
if a not in dicta.keys():
   dicta[a]= lista.count(a)
print(dict) # {'A': 2, 'B': 1, 'O'2, 'AB':2}

def solution(participant, completion):
    answer = ""
    dictc = {}
    for c in completion:
        if c not in dictc.keys():
            dictc[c] = 1
        else:
            dictc[c] = dictc[c] + 1    
    for p in participant:
        if p in dictc and dictc[p] > 0:
            dictc[p] = dictc[p] -1
        else:
            answer = p
    return answer

