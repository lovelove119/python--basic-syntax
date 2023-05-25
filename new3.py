# # 특정한 값을 모두 제거하려면 어떻게 해야 할까
# # del, for range
# # 방법1
# # count = 0
# # for a in rangea(0, len(lista)):
# #     if lista[a] == 9:
# #         del lista[a]
# #         count = count + 1
# # print(lista)
# # # 방법3
# # for a in range(0, len(lista)):
# #     if 9 in lista:
# #         lista.remove(9)
# #     else:
# #         break
# # print(lista)

# b = 119
# for k in range(2, 1, 2):
#   print(k)

# lista=[1,2,3]
# listb=['a','b','c']
# listc=lista+listb
# print(listc)

# # list append
# lista = [11,3,5,7]
# lista.append(9.10)
# print(lista)

# # list extend : iterable객체를 list에 추가할떄 사용
# # list.index(2,"abc")
# lista.insert(2,"a,b,c")
# print(lista)

# # list extend : iterable객체를 list에 추가할떄 사용
# # extend는 각 요소를 꺼내에 맨 뒤에 추가
# listb = [10,20,30]
# # lista.append(listb)
# lista.extend(listb)
# print(lista)

# # 리스트 값 정렬하기
# # list의 정렬은 sort()함수 사용
# # sort()는 오름차순 정렬
# # resense=True 옵션을 주면 내림차순 정렬

# numa = [5,3,18,4,2,1]
# numa.sort()
# print(numa)

# chlist = ['brad', 'john','abc']
# chlist.sort()
# print(chlist)

# # list : reverse()
# chlist.reverse()
# print(chlist)

# list=['김될쇠', '김갑룡', '김갑순', '김철수']
# print(list.index('김철수'))

# # 마지막 요소 끄집어 내기 : pop()
# lista.pop()
# lastvalue = lista.pop()
# print(listvalue)

# # 7, 1, 15명 일 떄 case
# n = 8
# answer = 8

# answer = n//7

# print(answer)

# numbers	num1	num2
# numbers = [1,2,3,4,5]
# num1 = 1
# num2 = 3
# answer = numbers()

# 문자 리스트를 문자열로 만들기
# 문자열을 먼저 리스트로 만들기

# lista = ["hello", 'world', "python"]
# st1 = ""
# st2 = st1.join(lista)
# print(st2)
# for a in lista:
#     st1 = st1 + a
# sta = "hello world python"
# mySta = list(sta)
# print(mySta)
# mySta2 = sta.split()
# print(mySta2)

# my_string="jaron"

# sta = "jaron"
# my_string=list(sta)
# print(sta)



for i in strlist:
        answer.append(len(i))
def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))
    return answer


#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// num_list_len은 배열 num_list의 길이입니다.
int* solution(int num_list[], size_t num_list_len) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc(1);
    return answer;
}