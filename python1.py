# 표시는 프로그램밍에서 주석이라 말한다
# 주석은 파이썬의 인터프리터가 인식하지 못하도록 기호
# 단축키는 Ctrl 슬래시

# 아래 a=1의 의미는 B와1이 같다는 의미가 아니라, 
# a라는 이름의 변수에 1을 담겠다는 뜻.
a = 1
b = '1'

# print는 실행후 결과값을 가시적으로 보여주기 위해 터미널창에 출력하는 것
# print(a)
# print(b)

# 변수명명 규칙
# 변수명을 지울때는 숫자가 먼저 나와서는 안된다.
# 변수명 중간에 띄어쓰기, 특수기호등을 일반적으로 쓰지 않는다.
# 특수부호는 일반적으로 사용하지는 않지만, _언더바는 천천히 사용 한다
# 변수자료형 출력해보기

# print(type(a))
# print(type(b))

# c = 2.1
# print(type(c))

# # 자료의 형변환
# # 숫자 > 문자 , 실수 > 정수
# a = 10
# b = 20
# # 결과값이 1020이 나오도록 덧셈을 하여라.
# print(str(a)+str(b))
# c = 2333.33333
# print(int(c))
# 'a'라는 문자를 변수에 저장하게 되면, 메모리상에 어떤 숫자값으로 저장될까?
# 문자는 ""따음표 또는 ''를 따음표로 표현을 한다.
# 'a'라는 문자를 
# 아스키코드라는 문자와 매핑되는 테이블을 사용하여 약속을 숫자값으로 지정
#현대에는 아스키코드의 표현범위와 한계로 인해, utf-8를 표준으로 사용

x = 'a'
print(ord(x))