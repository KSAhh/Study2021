# 문자형
# 문자열
# 탈출문자
# 문자열 - 처리함수
# 문자열- 슬라이싱
# 문자열 - 포멧
# -----------------------------------------------------------

# 문자형
print("풍선")
print("풍선")

print("ㅋ" * 9)

# -----------------------------------------------------------

# 문자열
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)  # 공백포함 4줄 차지

# -----------------------------------------------------------

# 탈출문자
print("백문이 불여일견\n백견이 불여일타")  # 줄바꿈 \n

print("저는 '나도코딩'입니다.")
print('저는 "나도코딩"입니다.')
print('저는 "나도코딩"입니다.')  # \" 또는 \' : 문자 내에서 텍스트로 인식
print("저는 '나도코딩'입니다.")

print("c:\\Users\\user\\Desktop\\2021-1\\practice.py")  # \\ : 하나의 \로 인식
# \ : 오류

print("Red Apple\rPine")  # \r : 커서를 맨 앞으로 이동 / Red가 없어지고 Pine이 들어감

print("Redd\b Apple")  # \b : 백스페이스 / 한 글자 삭제

print("Red\tApple")  # \t : tap


# -----------------------------------------------------------

# 문자열 - 처리함수
python = "Python is Amazing"
print(python.lower())  # 소문자로 변환
print(python.upper())  # 대문자로 변환
print(python[0].isupper())  # 대문자인지 확인
print(len(python))  # 길이
print(python.replace("Python", "Java"))  # 문자변환 / replace("찾고싶은 문자", "바꿀문자")

index = python.index("n")  # 문자의 위치 찾기 / 0부터
print(index)
index = python.index("n", index + 1)  # n다음 위치부터 찾기
print(index)
# print(python.index("Java"))  # 변수에 없는 문자는 오류 출력

print(python.find("n"))  # 문자의 위치 찾기
print(python.find("Java"))  # 변수에 없는 문자는 -1 출력

print(python.count("n"))  # 문자의 사용 횟수

# -----------------------------------------------------------

# 문자열- 슬라이싱
jumin = "970101-1234567"
print("성별 : " + jumin[7])  # 0부터 시작
print("연 : " + jumin[0:2])  # 0부터 2번째 직전까지
print("뒤 7자리(뒤에서부터) : " + jumin[-7:])  # 뒤에서부터 7번째자리~끝까지

# -----------------------------------------------------------

# 문자열 - 포멧
print("나는 %d살입니다." % 20)  # d 정수
print("나는 %s살입니다." % 20)  # s(string) 문자열
print("나는 %s을 좋아해요." % "파이썬")
print("Apple은 %c로 시작해요." % "A")  # c(Charictor) 한 문자
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

print("나는 {}살 입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))  # 0부터 / 순서 바뀜
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))

# python version 3.6이상에서 사용가능
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# -----------------------------------------------------------
