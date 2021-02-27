# 숫자형
# 숫자처리함수
# 함수
# -----------------------------------------------------------

# 숫자형
print("index) 숫자형")
print(2 ** 3)  # 8 # 제곱 2^3
print(10 % 3)  # 1 # 나머지
print(10 // 3)  # 3 # 몫

number = 0
number += 2  # 2
number *= 2  # 4
number /= 2  # 2
number %= 3  # 2 # 나머지

# -----------------------------------------------------------

# 숫자처리함수
print("index) 숫자처리함수")
print(abs(-5))  # 5 # 절댓값
print(pow(4, 2))  # 16 # 제곱

print(max(5, 12))  # 12
print(min(5, 12))  # 5

print(round(3.14))  # 3 #반올림
print(round(4.99))  # 5
### 형식 round(변수, 소수점 자릿수) # 둘째자리까지 나타내고 싶으면 2

from math import *  # python 제공 math라이브러리 내의 모든것을 이용할 것이다

print(floor(4.99))  # 4 # 내림
print(ceil(3.14))  # 4 # 올림
print(sqrt(16))  # 4.0 # 제곱근

from random import *  # python제공 random 라이브러리

print(random())  # 난수 생성 / 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10)  # 난수 생성 / 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10))  # 난수 생성 / 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1)  # 난수 생성 / 1 ~ 11 미만의 임의의 값 생성
print(int(random() * 45) + 1)  # 난수 생성 / 1 ~ 46 미만의 임의의 값 생성
print(randrange(1, 46))  # 난수 생성 / 1 ~ 46 미만의 임의의 값 생성
print(randint(1, 45))  # 난수 생성 / 1 ~ 45 이하의 임의의 값 생성

# -----------------------------------------------------------

# 함수
range(5)  # 0부터 5미만까지
users = range(1, 21)  # 1부터 20까지 숫자 생성
print(type(users))  # range 형식 / list형식 아님

temp = int(input("기온은 어때요?"))  # 정수형으로 변환

print(type(6))  # int
print(type(6 / 3))  # float
print(type(6 // 3))  # int
print(type(int(6 / 3)))  # int
