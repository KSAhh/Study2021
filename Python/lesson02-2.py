# 문자열 - 내장함수
str = "멋쟁이 사자처럼"
str2 = "은 좋은 동아리입니다."
print(str + str2)  # 덧셈 / 이어서 출력
print(str * 4)  # 곱셈 / 4번 출력
print(str[0])  # 인덱싱
print(str[1:5])  # 슬라이싱

print(len(str))  # 문자열의 길이
print(str.count("사"))  # '사'라는 글자가 나온 횟수
print(str.split(" "))  # 공백을 기준으로 나눔
print(str.split("처"))  # '처'를 기준으로 나눔
print(str.find("머"))  # '머'의 index를 찾음 / -1반환
print(str.index("멋"))  # '멋'의 index를 찾음

# 문자형 - 리스트(내장함수)
li = [3, 1, 4, 5, 2]

print(len(li))  # 길이

li.sort()  # 오름차순 정렬
print(li)

# 문자형 - 딕셔너리(내장함수)
pairs = {"잔나비": "뜨거운 여름밤은 가고 남은 건 볼품없지만", "소히": "산책", "ㅇㅇㅇ": "홍연"}

print(pairs)  # 그대로 출력

pairs["스탠딩 에그"] = "휴식"  # 키와 값 추가
print(pairs)

del pairs["잔나비"]  # del함수 특정 키.value 삭제
print(pairs)

v = pairs.get("스탠딩 에그")  # key로 value얻기 / 변수.get(키)
print(v)