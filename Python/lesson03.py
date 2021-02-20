# 제어문 - 분가문

### 85점 이상 PASS, 아니면 FAIL
score = int(input("점수를 입력해 주세요 : "))
if score >= 85:
    print("PASS")
else:
    print("FAIL")

### 동아리
activity = input("너 동아리 뭐해? : ")
if activity == "멋쟁이사자처럼":
    print("어, 너도 멋사야?")
else:
    print("그래..")

### 5000원 이상: 아웃백 / 3000원 이상 : 학식 / 1000원 이상 : 컵라면 / ㅠㅠ : 공기밥
money = int(input("돈 얼마 있어? "))
if money >= 5000:
    print("아웃백 가자")
elif money >= 3000:
    print("학식 먹자")
elif money >= 1000:
    print("컵라면 먹자")
else:
    print("알바하자")
