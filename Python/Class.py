# ★★★★★★★★★★★실행하면 안됨
# 클래스
# 클래스 - 멤버변수
# 클래스 - 메소드
# 클래스 - 상속
# 클래스 - 다중상속
# 클래스 - 메소드 오버라이딩
# 클래스 - pass

### 연습문제 - 게임
### 연습문제 - 매매
# ---------------------------------------------------------------------------------------------------

# 클래스
### 틀 / 서로 연관이 있는 변수와 함수의 집합
### 객체 : 클래스로부터 만들어지는 것
### Unit클래스의 instance : marine1, marine2, tank
class Unit:
    def __init__(self, name, hp, damage):  ## __init__ : 생성자 / 객체 만들 때 자동으로 호출되는 부분
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))


marine1 = Unit("마린", 40, 5)  # self를 제외한 인자 적음
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

### 클래스 - 멤버변수 : self.name, self.hp, self.damage / 클래스 내에서 정의돈 변수
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))  # 인스턴스.변수 형식

wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True  # clocking : 사용자가 임의로 외부에 변수 지정 / 확장한 객체에만 적용됨
if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

# ---------------------------------------------------------------------------------------------------

### 클래스 - 메소드
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print(
            "{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.name)
        )  # self가 없으면 함수에서 받은 인자를 바로 사용

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)

# ---------------------------------------------------------------------------------------------------

### 클래스 - 상속
### 부모 클래스 Unit, 자식클래스 AttackUnit
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp


class AttackUnit(Unit):  # Unit클래스를 상속받아 만들어진 것 /  self.name, self.hp 정의할 필요x
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)  # 추가
        self.damage = damage


# ---------------------------------------------------------------------------------------------------

### 클래스 - 다중상속
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


class AttackUnit(Unit):  # Unit클래스를 상속받아 만들어진 것 /  self.name, self.hp 정의할 필요x
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)  # 추가
        self.damage = damage

        def attack(self, location):
            print(
                "{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(
                    self.name, location, self.name
                )
            )  # self가 없으면 함수에서 받은 인자를 바로 사용

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(
            "{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed)
        )


class FlyableAttacUnit(AttackUnit, Flyable):  # 다중상속
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)


valkyrie = FlyableAttacUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")

# ---------------------------------------------------------------------------------------------------

# 클래스 - 메소드 오버라이딩
### 자식클래스에서 쓰인 변수를 부모클래스에서 쓰기
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):  ###############
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))


class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

        def attack(self, location):
            print(
                "{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(
                    self.name, location, self.name
                )
            )

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(
            "{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed)
        )


class FlyableAttacUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)  # 지상 speed = 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)  ############### 메소드 오버라이딩 / move함수 재정의


vulture = AttackUnit("벌쳐", 80, 10, 20)
battlecruiser = FlyableAttacUnit("배틀크루저", 500, 25, 3)

vulture.move("11")
# battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시")

# ---------------------------------------------------------------------------------------------------

# 클래스 - pass
###
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed


class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass  # 아무것도 안하고 넘어감


supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

###
def game_start():
    print("[알림] 새로운 게임을 시작합니다.")


def game_over():
    pass


game_start()
game_over()

# ---------------------------------------------------------------------------------------------------
# 클래스 - super
### 상속
### 맨 처음 클래스만 상속받을 수 있음
class Unit:
    def __init__(self):
        print("Unit 생성자")


class Flyable:
    def __init__(self):
        print("Flyable 생성자")


# class FlyableUnit(Unit, Flyable):  # Unit클래스는 상속받지만 / Flyable 클래스는 상속받지 못함
#     def __init__(self):
#         super().__init__()


# class FlyableUnit(Flyable, Unit): # Flyable클래스는 상속받지만 / Unit 클래스는 상속받지 못함
#     def __init__(self):
#         super().__init__()


###### 해결
class FlyableUnit(Unit, Flyable):  # Unit클래스는 상속받지만 / Flyable 클래스는 상속받지 못함
    def __init__(self):
        # super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)


dropship = FlyableUnit()  # 맨 처음 클래스만 상속받을 수 있음

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
### 연습문제 - 게임

from random import *

#### 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))  # self.name도 됨

    def move(self, location):
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


#### 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

        def attack(self, location):
            print(
                "{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(
                    self.name, location, self.damage
                )
            )


#### 날 수 있는 기능
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(
            "{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed)
        )


#### 공중 공격 유닛
class FlyableAttacUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


#### "마린"
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    # 스팀팩 : 일정 시간 동안 이동 및 공격 속도 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))


#### "탱크"
class Tank(AttackUnit):
    # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가
    seize_developed = False  # 시즈모드 개발여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        # 현재 시즈모드가 아닐 때 -> 시즈모드
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        # 현재 시즈모드 일 때 -> 시즈모드 해제
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False


#### "레이스"
class Wraith(FlyableAttacUnit):
    def __init__(self):
        FlyableAttacUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False  # 클로킹 모드 (해제 상태)

    def clocking(self):
        if self.clocked == True:  # 클로킹 모드 -> 모드 해제
            print("{0} : 클로킹 모드를 해제합니다.".format(self.name))
            self.clocked = False
        else:  # 클로킹 모드 해제 -> 모드 설정
            print("{0} : 클로킹 모드를 설정합니다.".format(self.name))
            self.clocked = True


def game_start():
    print("[알림] 새로운 게임을 시작합니다.")


def game_over():
    print("Player : gg")  # good game
    print("[Player] 님이 게임에서 퇴장하셨습니다.")


#### 실제 게임 진행
game_start()
# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()
# 탱크 2기 생성
t1 = Tank()
t2 = Tank()
# 레이스 1기 생성
w1 = Wraith()

# 유닛 일괄 관리
attack_units = []  # list
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# 공격 모드 준비 (마린 : 스팀팩, 탱크: 시즈모드, 레이스 : 클로킹 모드)
for unit in attack_units:
    if isinstance(unit, Marine):  # ★★★★★★★★★★★★★★★만들어진 객체가 어떤 클래스의 인스턴스인지 확인하는 것
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 전군 공격
for unit in attack_units:  # ★★★★★★★★★★★★★★★오류발생
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 20))  # 공격은 랜덤으로 받음 ( 5~20)

# 게임 종료
game_over()

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

### 연습문제 - 매매
class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물 정보 표시
    def show_detail(self):
        # print("총 {0}대의 매물이 있습니다.".format())
        print(
            self.location,
            self.house_type,
            self.deal_type,
            self.price,
            self.completion_year,
        )


home = []
home1 = House("강남", "아파트", "매매", "18억", "2010년")
home2 = House("마포", "오피스텔", "전세", "5억", "2007년")
home3 = House("송파", "빌라", "월세", "500/50", "2000년")

home.append(home1)
home.append(home2)
home.append(home3)

print("총 {0}대의 매물이 있습니다.".format(len(home)))
for unit in home:
    unit.show_detail()
