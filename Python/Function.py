# 분기
# 반복문
# 분기, 반복문 응용
# 함수 - 전달값과 반환값, 기본값, 키워드값, 가변인자
# 함수2

# 연습문제
# -----------------------------------------------------------

# 분기
# 어떤 상황에서는 1번 코드를, 다른 상황에서는 2번 코드를 실행
# 형식
#   if 조건문:
#       실행 명령문
#   elif 조건문:
#       실행 명령문
#   else:
#       실행 명령문
weather = input("오늘 날씨는 어때요?")
if weather == "비" or weather == "눈":  # or, and,
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비를 필요 없어요.")

# -----------------------------------------------------------

# 반복문
# 형식
# for 변수 in 반복:
#   반복할 명령
for waiting_no in [1, 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(5):
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))

# 형식 - 조건이 만족하는 동안만 실행
#   while (조건):
#       반복할 명령문
customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1}번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분 되었습니다.")

customer = "토르"
# index = 1
# while True: #무한루프 / 종료는 Ctrl+C
#    print("{0}, 커피가 준비되었습니다. 호출 {1} 회" .format(customer, index))
#    index += 1

customer = "토르"
person = "Unknown"
while person != customer:
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")

# -----------------------------------------------------------

# 분기, 반복문 응용
absent = [2, 5]
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue  # 밑의 문장을 실행하지 않고 다음 반복문 실행
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break  # 다음 반복문도 안하고 종료
    print("{0}, 책을 읽어봐".format(student))

students = [1, 2, 3, 4, 5]
print(students)  # 1,2,3,4,5
students = [i + 100 for i in students]  # i+100값을 넣을건데 i는 students에서 가져온다.
print(students)  # 101,102,103,104,105

students = ["Iron man", "Thor", "I amd groot"]  # 문자열
students = [len(i) for i in students]  # 길이로 바꿈
print(students)  # [8,4,11]

students = ["Iron man", "Thor", "I amd groot"]
students = [i.upper() for i in students]  # 길이로 바꿈
print(students)  # ['IRON MAN', 'THOR', 'I AMD GROOT']

# -----------------------------------------------------------

# 함수
def open_account():  # 함수정의 / 실행X
    print("새로운 계좌가 생성되었습니다.")


open_account()  # 함수 실행

# -----------------------------------------------------------

# 함수 - 전달값과 반환값
### 입금
def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0} 원 입니다.".format(balance + money))
    return balance + money  # 반환 / balance에 저장됨


balance = 0  # 잔액
balance = deposit(balance, 1000)
print(balance)

### 출금
def withdraw(balance, money):
    if balance >= money:  # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance


balance = withdraw(balance, 1100)
balance = withdraw(balance, 500)

### 저녁에 출금
def withdraw_night(balance, money):
    commission = 100  # 수수료
    return commission, balance - money - commission  # 튜플형식


balance = deposit(balance, 1000)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))

# -----------------------------------------------------------

# 함수 - 기본값
def profile(name, age=17, main_lang="Python"):  # 전달받지 않았을 때, 기본값을 넣어줌
    print("이름 : {0}\t 나이 : {1}\t주 사용 언어: {2}".format(name, age, main_lang))


profile("유재석", 55)
profile("양세찬")

# 함수 - 키워드값
def profile(name, age, main_lang):
    print(name, age, main_lang)


profile(name="유재석", main_lang="Python", age=55)

# -----------------------------------------------------------
# 함수 - 가변인자

### 가변인자 미적용
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    print(lang1, lang2, lang3, lang4, lang5)


profile("유재석", 56, "Python", "Java", "C", "C++", "C#")
profile("양세찬", 37, "Kotlin", "Swift", "", "", "")

### 가변인자 적용
def profile(name, age, *language):  # *language : 가변인자 / 개수 달라도 상관 없음
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()  # enter역할


profile("유재석", 56, "Python", "Java", "C", "C++", "C#")
profile("양세찬", 37, "Kotlin", "Swift")

# -----------------------------------------------------------
# 함수2
from random import shuffle, sample

lst = [1, 2, 3, 4, 5]
shuffle(lst)  # 무작위로 값 순서를 바꿈
new = sample(lst, 2)  # 2개 무작위로 뽑음

# -----------------------------------------------------------
# -----------------------------------------------------------
# -----------------------------------------------------------
# -----------------------------------------------------------
# -----------------------------------------------------------

### 연습문제 - 표준체중 구하기
def std_weight(height, gender):
    if gender == "man":
        weight = round((height / 100) ** 2 * 22, 2)
        print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height, weight))
    elif gender == "woman":
        weight = (height / 100) ** 2 * 21
        print("키 {0}cm 여자의 표준 체중은 %.2fkg 입니다.".format(height) % weight)
    return weight


result = std_weight(175, "man")
print(result)

### 또는
def std_weight_video(height, gender):  # 키 m단위 (실수), 성별 "남자"/"여자"
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21


height = 175  # cm단위
gender = "남자"
weight = round(std_weight_video(height / 100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))