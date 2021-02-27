# 리스트 []
# 사전 {}
# 튜플 ()
# 세트(집합, set) {} 또는 set([])
# 자료구조의 변경
# -----------------------------------------------------------

# 리스트(list)
# 순서를 가진 객체의 집합
# 0부터 / data 변경 가능
subway = [10, 20, 30]
print(subway)

subway = ["유재석", "박명수", "하하"]
print(subway)

print(subway.index("유재석"))  # 0부터 시작 / 유재석 위치

subway.append("양세형")  # 맨 뒤에 객체 추가
print(subway)

subway.insert(1, "양세찬")  # 1번째에 객체 추가
print(subway)

print(subway.pop())  # 뒤에서 삭제할 객체
print(subway)  # 삭제된 후, 나머지 객체

subway.append("유재석")
print(subway.count("유재석"))  # 같은 객체 몇개인지

num_list = [5, 3, 4, 2, 1]
num_list.sort()  # 오름차순 정렬
print(num_list)

num_list.reverse()  # 뒤집기
print(num_list)

num_list.clear()  # 삭제
print(num_list)

mix_list = ["양세찬", 20, True]  # 다른 자료형 함께 사용
print(mix_list)

num_list = [5, 3, 4, 2, 1]
num_list.extend(mix_list)  # 하나의 리스트로 합침
print(num_list)

# -----------------------------------------------------------

# 사전(Dictionary)
# 형식 {key:value}
cabinet = {3: "유재석", 100: "김예림"}
print(cabinet[3])
print(cabinet.get(3))

scores = {"수학": 0, "영어": 50, "코딩": 100}
print(
    scores.items()
)  # 출력 : dict_items([('수학', 0), ('영어', 50), ('코딩', 100)]) / # key와 value값으로 나옴

# print(cabinet[5])  # 없는 key는 오류 발생 / KeyError: 5 / 뒤의 함수 실행 안 됨
print(cabinet.get(5))  # 없는 key는 None 출력 / 뒤의 함수 실행 됨
print(cabinet.get(5, "사용 가능"))  # 5라는 key가 없으면 대체문구 출력

print(3 in cabinet)  # key in 변수 / key가 있는지 확인 (Boolean)

cabinet = {"A-3": "유재석", "B-100": "김종국"}
cabinet["A-3"] = "알간지"  # 수정
cabinet["C-4"] = "제시"  # 추가
del cabinet["B-100"]  # 삭제
print(cabinet)

print(cabinet.keys())  # key만 출력
print(cabinet.values())  # value만 출력
print(cabinet.items())  # key와 value 쌍으로 출력

cabinet.clear()  # 모두 삭제
print(cabinet)

# -----------------------------------------------------------

# 튜플
# 0부터 시작 / data 변경 불가능
menu = ("돈까스", "치즈까스")
print(menu[0])

# menu.add("생선까스") #오류

name = "김종국"
age = 23
hobby = "코딩"
print(name, age, hobby)

name, age, hobby = "김종국", 23, "코딩"  # 한 번에 선언
print(name, age, hobby)

# -----------------------------------------------------------

# 세트(집합, set)
# 중복 안 됨 / 순서 없음
my_set = {1, 2, 3, 3, 3}
print(my_set)  # {1,2,3}

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])
print(java & python)  # 교집합
print(java.intersection(python))  # 교집합

print(java | python)  # 합집합
print(java.union(python))  # 합집합

print(java - python)  # 차집합
print(java.difference(python))  # 차집합

python.add("김태호")  # 추가
print(python)

java.remove("김태호")  # 삭제
print(java)

# -----------------------------------------------------------

# 자료구조의 변경
menu = {"커피, 우유", "주스"}  # 세트형
print(menu, type(menu))

menu = list(menu)  # 리스트로 변경
print(menu, type(menu))

menu = tuple(menu)  # 튜플로 변경
print(menu, type(menu))

menu = set(menu)  # 세트로 변경
print(menu, type(menu))