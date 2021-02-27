# ★★★★★★★★★★★실행하면 안됨
# 주석, 줄바꿈
# Boolean (참과 거짓)
# 변수, 지역/전역 변수
# 예외처리
# 모듈
# 패키지
# 내장함수
# 외장함수

# 연습문제 - 치킨주문
# -----------------------------------------------------------

# 주석
""" 주석처리하고 싶은 내용 """

# 줄바꿈
## \ + Enter
# print("이름 : {0}\t 나이 : {1}\t주 사용 언어: {2}".format(name, age, main_lang))

# -----------------------------------------------------------

# Boolean (참과 거짓)
print(5 > 10)
print(1 == 1)
print(1 != 1)

print(not 5 > 10)
print(not True)

# -----------------------------------------------------------

# 변수
# 값을 저장하는 공간
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3
print("우리집 " + animal + "의 이름은 " + name + "이에요")
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")  # str() : 숫자형 → 문자형
print(animal, "는 어른일까요? ", is_adult)  # "," 로 연결될 때는 str()을 사용안 해도 되지만, 자동으로 띄어쓰기가 들어감

# 지역변수와 전역변수
# 가급적 지역변수 사용
### 이해 됩기위한 예시(잘못 사용한 예시)
def checkpoint(soliders):
    gun = 20
    gun = gun - soliders
    print("[함수 내] 남은 총 : {0}".format(gun))


gun = 10
print("전체 총 : {0}".format(gun))
checkpoint(2)
print("남은 총 : {0}".format(gun))

### 제대로 사용 한 예시
def checkpoint(soliders):
    global gun  # 전역 공간에 있는 gun 사용
    gun = gun - soliders
    print("[함수 내] 남은 총 : {0}".format(gun))


gun = 10
print("전체 총 : {0}".format(gun))
checkpoint(2)
print("남은 총 : {0}".format(gun))

### 제대로 사용한 예시


def checkpoint_ret(gun, soliders):  # 지역변수라 밖의 값이 바뀌지 않음 but return으로 외부로 가져갈 수 있음
    gun = gun - soliders
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun


gun = 10
print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))

# -----------------------------------------------------------

# 예외처리
### 에러가 발생했을 때, 처리해주는 것
### error : 아파트가 10층까지인데 택배주소는 10층인 경우 / 버스카드 잔액 없는 경우 / 계신기에 숫자 입력 받아야 하는데 문자 입력 받음 / 홈페이지 주소 잘못 / 사용자 많아 접속 잘 되지 않는 현상
try:
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    print("{0} / {1} = {2} ".format(num1, num2, int(num1 / num2)))
except ValueError:  # "삼"이라 적은 경우 /// ValueError: invalid literal for int() with base 10: '삼'
    print("에러! 잘못된 값을 입력하였습니다.")  # 에러발생하면 출력
except ZeroDivisionError as err:  # 나누는 수가 "0"인 경우 /// ZeroDivisionError: division by zero
    print(err)  # 출력 : division by zero

try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    # nums.append(int(nums[0] / nums[1])) #없는 경우,
    print(
        "{0} / {1} = {2} ".format(nums[0], nums[2], nums[3])
    )  # num[3]가 없음 /// IndexError: list index out of range
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except:  # 위에서 정의된 에러 외에 모든 에러
    print("알 수 없는 에러가 발생하였습니다.")
### 설명 추가
# except Exception as err:
#     print("알 수 없는 에러가 발생하였습니다.")
#     print(err)

# -----------------------------------------------------------

### 예외 처리 - 사용자 지정 에러
try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise ValueError  # 에러 발생
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")

# -----------------------------------------------------------

### 예외처리 - python에서 제공하는 에러 이외에 사용자 지정 에러
class BigNumBerError(Exception):
    pass


try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumBerError  # 에러 발생
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumBerError:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")

### 예외처리 - python에서 제공하는 에러 이외에 사용자 지정 에러
### 예외처리 - finally / 마지막에 무조건 실행
class BigNumBerError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumBerError("입력값 : {0}, {1}".format(num1, num2))  # 에러 발생
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumBerError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)
finally:
    print("계산기를 이용해 주셔서 감사합니다.")

# -----------------------------------------------------------

### 연습문제 - 치킨주문
class SoldOutError(Exception):
    pass


chicken = 10
waiting = 1
while True:
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))

        if order > chicken:  # 남은 치킨보다 주문량이 많을 때
            print("재료가 부족합니다.")
        elif order < 1:
            raise ValueError
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting, order))
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break

# -----------------------------------------------------------

# 모듈
### 필요한 것들끼리 부품처럼 만들어진 파일
### 특정 부품만 수정 가능

### import 구문
import theater_module  # import 파일명

theater_module.price(3)
theater_module.price_morning(4)
theater_module.price_solider(2)

### import 구문
import theater_module as mv

mv.price(3)
mv.price_morning(4)
mv.price_solider(2)

### from import 구문
from theater_module import *

price(3)
price_morning(4)
price_solider(2)

### from import 구문
from theater_module import price, price_morning

price(3)
price_morning(4)


# -----------------------------------------------------------

# 패키지
### 모듈을 모아놓은 것
### travel/tailand.py, travel/vietnam.py,  travel/__init__.py

#############################
# import travel.thailand  # import 뒷부분은 모듈 or 패키지만 가능 / 클래스 or 함수는 불가

# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

#############################
# from travel.thailand import ThailandPackage  # import 뒷부분은 클래스 or 함수 가능

# trip_to = ThailandPackage()
# trip_to.detail()

#############################
# from travel import vietnam

# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

############################ 오류
# from travel import *  # * 사용할 때, 범위 설정을 해주어야 함 / __init__.py 수정

# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# -----------------------------------------------------------

# 패키지, 모듈 위치
import inspect
import random

from travel import *

trip_to = thailand.ThailandPackage()
trip_to.detail()

print(inspect.getfile(random))  # random 모듈이 어디위치에 있는지 파일 정보 알려줌 / 이 내용에 폴더 복사 붙여넣기 ->
print(inspect.getfile(thailand))  # lib에 넣은 위치로 나옴

# -----------------------------------------------------------

# pip install (패키지 설치)
### 구글에 "pypi" 검색 -> "browse project" 클릭 -> 패키지 리스트 출력

# ----------------------------------------------------------

# 내장함수
### ★★★★★★★★★★★★★"list of python builtins" 구글 검색
### input(), print()
### dir() # 어떤 객체를 넣어줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
import random

print(dir())  # random 추가됨

print(dir(random))  # random 모듈이 가지는 변수와 함수 / random.을 찍을때 나오는 것들

lst = [1, 2, 3]
print(dir(lst))  # list변수에 쓸 수 있는 것들
name = "Jim"
print(dir(name))  # 사용할 수 있는 변수들

# ----------------------------------------------------------

# 외장함수
### ★★★★★★★★★★★★★"list of python modules" 구글 검색
### random 등

# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
import glob

print(glob.glob("*.py"))  # 확장자가 py인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
import os

print(os.listdir())  # glob과 비슷한 기능

###
print(os.getcwd())  # 현재 디렉토리

###
folder = "sample_dir"
if os.path.exists(folder):  # 폴더 확인
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)  # 폴더 삭제
    print(folder, "폴더를 삭제하였습니다.")
else:
    os.makedirs(folder)  # 폴더 생성
    print(folder, "폴더를 생성하였습니다.")

# time : 시간 관련 함수
import time

print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime

print("오늘 날짜는 ", datetime.date.today())
print("오늘 날짜는 ", datetime.date.today().__format__("%Y.%m.%d"))

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today()  # 오늘 날짜 저장
td = datetime.timedelta(days=100)  # 100일 저장
print("우리가 만난지 100일은", today + td)

# -----------------------------------------------------------
