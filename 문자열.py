# # # 문자열 관련 주요 함수
# # # count : 대상 문자열에 지정한 문자가 몇개가 있는 출력하는 함수
# # a = "python"
# # print(a.count('o'))

# # # find : 대상 문자열에서 지정한 문자가 index에 있는 찾는 함수
# # # index : find와 같은 기능
# # print(a.find('o'))
# # # 없는 문자를 찾을 떄는 -1 return
# # print(a.find('x'))

# # whatyouwant = input("아무런 문자나 입력해주세요")
# # search = input("찾고자 하는 문자 1개면 입력해주세요")
# # result = whatyouwant.find(search)
# # print("요청하는 문자는 %s 번쨰에 있습니다"% result)

# # 대소문자 변경 : upper() / lovwer()
# a = "hello"
# print(a.upper())
# b = "HELLO"
# print(b.lower())

# # 문자열 양쪽 공백을 없는 함수 : strip()
# a = "   Hello word  "
# print(a.strip())

# # myID = (input("id를 입력해주세요")strip()
# # mypw = input("비멀본호를 입력해주세요")

# #print("ID는 "+ myID" 이고 + "비밀번호는 "myPw)

# # 문자열 대체 : replace()
# a = 'I studied python'
# a = a.replace('python', 'jave')
# print(a)

# # 공백을 기준으로 문자를 자르는 함수 : split()
# a = "I studied python"
# b = a.split()
# print(b)

# a = "I  studied  python"
# b =a.split(" ")
# print(b)

# x = int (input("x값을 입력해주세요"))
# y = 2.5 * pow(x, 2) + 3.3*x +6
# print(y)

a = input("첫번쨰 문자를 입력해주세요")
b = input("첫번쨰 문자를 입력해주세요")
c = input("첫번쨰 문자를 입력해주세요")
abc = a[0]+ b[0]+c[0]
print(abc)