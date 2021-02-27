# ----------------------------------------------------------

# 모듈
### 필요한 것들끼리 부품처럼 만들어진 파일
### 특정 부품만 수정 가능

# 일반 가격 - 모듈
def price(people):
    print("{0}명 가격은 {1}원 입니다.".format(people, people * 1000))


# 조조할인 가격 - 모듈
def price_morning(people):
    print("{0}명 조조 할인 가격은 {1}원 입니다.".format(people, people * 6000))


# 군인 할인 가격 - 모듈
def price_solider(people):
    print("{0}명 군인 할인 가격은 {1}원 입니다.".format(people, people * 4000))
