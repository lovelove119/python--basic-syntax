# # a = 3
# # b = 4
# # # 덧셈 : +, 빼기 - , 곱하기 *, 나누기 : / 몫 : // 나머지 : %
# # print (a+b)
# # print(a-b)
# # print(a*b)
# # print(a/b)
# # print(a//b)
# # print(a%b)

# # # 제곱, 제곱근
# # # 2의10 제곱을 출력해라
# # print(2**10)
# # print(pow(2,10))
# # import math
# # pow(match,sqrt(1024))
# # # 자료의 형변환
# # # 숫자 > 문자 , 실수 > 정수
# # # 1024의 제곱근을 구해라
# # # 제곱근은 nath라는 라이브러리를 import를 해야한다
# # a = 10
# # b = 20
# # # 결과값이 1020이 나오도록 덧셈을 하여라.
# # print(str(a)+str(b))
# # c = 2333.33333
# # print(int(c))

# # # multi line으로 문자열을 표현하고 싶으면, 
# # # 쌍따음표를 3개 사용하거나 호홈따음표를 3개 사용 하면 된다

# # a= """hello
# # word"""
# # print(a)

# # 문자열 포맷팅이란 문자열 중간에 특정 문자(또는 숫자 등)을 삽입하는 방식
# # %s : 문자열, %d : 정수

# # # 그렇다면 python's easy라는 문구를 출력해보자

# # d ="python's easy"
# # print(d)
# # # 이스케이프문을 활용한 줄바꿈
# # # 이스케이프문이란 \n : 줄바꿈, \t:tap키
# # # 역슬래시의 또다른 활용
# # # "쌍따음표("")는 파이썬에서 문자를 의미한다." 문구를 출력해보세요
# # e = "hello\word"
# # print(e)
# # f = "쌍따음표(\")는 파이썬에서 문자를 의미한다"
# # print(f)

# # 문자열 더하기, 곱하기
# # a라는 변수에 python이라는 문자열을 담고,
# # b라는 변수에는 is fun라는 문자열을 담는다.
# # 그리고 c라는 변수에 두 문자열을 더한 값을 c를 출력

# a = "python"
# b = " is fun"
# c = a + b
# print(c)
# # 문자열 곱하기
# # python python is fun이라는 문자열을 c에 담아 출력
# c = a*2 +b
# print(c)

# # 파이썬에서 인덱스란, 기본적으로 특정위치를 가리키는 용도로 사용
# # 인덱스의 사용방법은 원하는 대상[숫자값]
# # 프로그래밍에서는 대부분의 순서는 0부터 시작된다.
# # 0,1,2,3,4,5....의 체계
# # 문자 h를 출력하라
# a = "python's fun"
# print(a[3])

# a = "python's funpython's funpython's fun"
# print(a.strip()[-1])
# # 문자열의 길이를 구하는 구하는 함수는 len()
# print(len(a))
# print(a[35])
# print(a[len(a)-1])

# # 문자열의 슬라이싱
# # 슬라이싱이란 문자열을 잘라내는 것을 의미
# # 대상변수[X:y]:x이상 y미만의
# # index를 가진 문자열을 잘라낸다
# a = "python is fun"
# # python만 잘라내서 b에 담아 출력해주세요
# b = a[0:6]
# print(b)
# # x,y 자리에 값이 없으면 처음부터 또는 끝까지를 의미
# # 6번쨰 문자부터 끝까지 잘라내서 변수 b에 담아 출력
# print(a[6:])
# # a[x:y:z] 여기에서 z는 2-1 개씩 건너뛰고,
# # 2번쨰 이상 7번쨰 미만 문자열 중에 1개씩 건너뛰고 b에 담아 출력
# print(b[::3])

# a = "20220505children's_day"
# # date라는 변수에 날짜 day라는 변수에 children's'_day을 담아서 각각 출력하시오.
# date = a[:8]
# day = a[8:]
# print(date)
# print(day)

# # 문자열 포맷팅이란 문자열 중간에 특정 문자(또는 숫자 등)을 삽입하는 방식
# # %s : 문자열, %d : 정수, %f는 살수
# # 포맷팅을 왜 쓰는가
# # 1)문자열을 직접 삽입하면 1회성으로 coding을할수 밖에 없지만, 포맷팅은 변수값을 삽입 수 있음
# # 2)따음표를 여러번 안담아도된다.
# times = 2
# a = "I studied %s %d times" %("python")
# language = input("좋아하는 언어를 입력하세요")
# times = input("그 언어를 몇번이나 공부하셨나요")
# a = "I studied %s very hard %d times"(language, int(thmes))
# print(a)

# age = int(input("나이가 몇 살 인가요?"))
# weight = float(input("몸무게가 몇 킬로그램인가요?"))
# b = "my age is %d, and weight is %f kg" %(age,weight)
# print(b)