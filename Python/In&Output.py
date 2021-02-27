# 표준입출력
# 출력포멧
# 파일입출력
# -----------------------------------------------------------

# 표준입출력
answer = input("아무 값이나 입력하세요 : ")  # str타입
print(type(answer))  # str타입
print("입력하신 값은 " + answer + "입니다.")

print("Python", "Java", sep=" vs ")  # sep="" : ""으로 구분된 문장 사이에 들어갈 내용

print("Python", "Java", sep=", ", end="?")
# end="?" : 문장의 끝부분에 들어갈 내용
# end=" " : 밑의 문장을 이어서 출력
print("무엇이 더 재밌을까요?")

###
import sys

print("Python", "Java", file=sys.stdout)  # 표준 출력
print("Python", "Java", file=sys.stderr)  # 표준 에러 - 따로 로딩해서 error처리 할 수 있음

###
scores = {"수학": 0, "영어": 50, "코딩": 100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")
    # .lust(8) : Text에 사용 / 8칸의 공간을 확보해서 왼쪽 정렬
    # .rjust(4) : Text에 사용 / 4칸의 공간을 확보해서 오른쪽정렬

for num in range(1, 21):
    print(
        "대기번호: " + str(num).zfill(3)
    )  # .zfill(3):  3개만큼의 크기를 확보하고 값을 집어넣음 / 값이 없는 빈 공간은 0으로 채움

# -----------------------------------------------------------

# 출력포멧

print("{0: >10}".format(500))  # 빈 자리는 빈 공간으로 채움 / 오른쪽 정렬 / 10자리 공간 확보
print("{0: >+10}".format(-500))  # 양수일 땐 +로 표시, 음수일 땐 -로 표시 #### 부호 없으면 양수일땐 +가 없다는 차이점
print("{0:_<+10}".format(+500))  # 빈칸을 _로 채움 / 왼쪽 정렬 / +-부호 표시 / 10칸 채움
print("{0:+,}".format(123123123))  # +-부호 표시 / 3자리 마다 콤마(,) 찍어줌
print("{0:^<+30,}".format(1234567890))  # 빈자리 ^로 채움 / 왼쪽정렬 / +- 부호 표시 / 30자리 차지
print("{0:.2f}".format(5 / 3))  # 소수점 출력 / 3째 자리에서 반올림 / 2째 자리까지 표시

# -----------------------------------------------------------

# 파일입출력

### 쓰기
#### 파일을 열어서 점수정보를 씀 #출력 : 파일 생성됨
#### open("파일이름", "목적(Writing 쓰기)(Append 이어쓰기)", encoding="utf8")
#### utf8이 아니면 한글이 이상하게 표시됨
score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()  # 파일 닫기 / 반드시 필요 / 소스코드 내 다른 곳에서 똑같은 파일에 접근하는 경우, 이미 파일이 열려있으면 lock상태가 되기 때문에 사용 불가한 상황이 됨

score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학 : 80")  # 파일에 쓰기
score_file.write("\n코딩 : 100")  # 줄바꿈이 자동으로 안 됨
score_file.close()

### 읽기
#### open("파일이름", "목적(Read 읽기)", encoding="utf8")
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline())  # 줄별로 읽기 / 한 줄 읽어오고 커서를 다음 줄로 이동
print(score_file.readline(), end="")  # 줄바꿈 없애줌
print(score_file.readline())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
while True:  # 무한루프
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()  # line을 list형태로 저장
for line in lines:
    print(line, end="")
score_file.close()

# 파일입출력 - pikcle
### 사용하는 데이터를 file형태로 저장
### 출력 : profile.pickle 파일이 생김
### rb : read binary / 바이너리 형태의 파일 / 이미지 등
### rt, r : read text / 텍스트 파일
import pickle  # 모듈 import

profile_file = open("profile.pickle", "wb")  # wb : Write Binary / 인코딩 설정할 필요X
profile = {"이름": "박명수", "나이": 30, "취미": ["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file)  # pickle.dump(파일에 저장할 내용, 파일명)
profile_file.close()

###
with open("study.txt", "w", encoding="utf8") as study_file:  # close필요없음
    study_file.write("파이썬을 열심히 공부하고 있어요")


### file에 있는 데이터를 출력
profile_file = open("profile.pickle", "rb")  # rb : Read Binary
profile = pickle.load(profile_file)  # file에 있는 정보를 변수(profile)에 불러옴
print(profile)
profile_file.close()

###
with open("study.txt", "r", encoding="utf8") as study_file:  # close필요없음
    print(study_file.read())

### file에 있는 데이터를 출력
### close 필요 없음
import pickle

with open("profile.pickle", "rb") as profile_file:  # profile_file이라는 변수에 저장
    print(pickle.load(profile_file))