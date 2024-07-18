from enum import Enum
import time
import random

items = {}
money = 500
haveItems = []
haveAnimals = []

class Base(Enum):
    FARMING = 1
    LIVESTOCK = 2
    FISHING = 3

# 낙농업은 기반이 되는 동물(소, 양등)을 먼저 구매해서 농장에 넣어두고, 그후 일정 시간마다 들어가서 아이템을 얻을수 있게함.
# 어업은 돈을 넣고, 그 돈과 비슷한 정도의 물고기를 랜덤으로 낚을수 있게함.

class Item:
    def __init__(self, name, material, sellPrice):
        self.name = name
        self.material = material
        self.sellPrice = sellPrice
        
        items[name] = self
            
        
    def sell(self, money, haveItems:list):
        if self.name in haveItems:
            money += self.sellPrice
            print(f"{self.name}을(를) 판매했다!")
            print(f"현재 돈: {money}")
            haveItems.remove(self.name)
        else:
            print("가지고 있지 않다!")
            
        return money, haveItems
    
    def craft(self, haveItems:list):
        if isinstance(items[self.name].material[0], Base):
            print("제작할 수 없다!")
            return haveItems
        
        for i in self.material:
            if i not in haveItems:
                print("재료가 부족해서 제작할 수 없다!")
                return haveItems
        
        for i in self.material:
            haveItems.remove(i)
        
        haveItems.append(self.name)
        print(f"{self.name}을(를) 제작했다!")
        return haveItems
        
class Farm(Item):
    def __init__(self, name, material, sellPrice, growTime, seedPrice):
        super().__init__(name, material, sellPrice)
        self.growTime = growTime
        self.seedPrice = seedPrice
        
        items[name] = self

    def farming(self, money, haveItems:list):
        if money >= self.seedPrice:
            money -= self.seedPrice
            print(f"{self.name}이(가) 자라나는 중...")
            time.sleep(self.growTime)
            print(f"{self.name}을(를) 수확했다!")
            haveItems.append(self.name)
        else:
            print("돈이 부족해서 재배할 수 없다...")
            
        return money, haveItems

    

class Animal(Item):
    def __init__(self, name, material, sellPrice, gainTime, animalPrice, milk, meat, breedPer):
        super().__init__(name, material, sellPrice)
        self.gainTime = gainTime
        self.animalPrice = animalPrice
        self.milk = milk
        self.meat = meat
        self.breedPer = breedPer

        self.lastTime = 0

    def buy_animal(self, money, haveAnimals:list):
        if self.animalPrice <= money:
            haveAnimals.append(self.name)
            money -= self.animalPrice
            print(f"{self.name}을(를) {self.animalPrice}에 구매했다!")
        else:
            print(f"{self.name}을(를) 구매하기에는 돈이 부족하다...")

        return money, haveAnimals    

    def can_gain(self):
        nowTime = time.time()
        if nowTime - self.lastTime >= self.gainTime:
            self.lastTime = nowTime
            return True
        else:
            return False

    def milking(self, haveItems:list):
        if self.can_gain():
            for i in range(haveAnimals.count(self.name)):
                haveItems.append(self.milk.name)
            print(f"{self.milk.name}을(를) {haveAnimals.count(self.name)}개 짜냈다!")
        else:
            print(f"아직 {self.milk.name}을(를) 짜낼 수 없다!")
        return haveItems

    def kill(self, haveItems:list, haveAnimals:list):
        haveAnimals.remove(self.name)
        if not self.meat == None:
            a = random.randint(2, 4)
            for i in range(1, a):
                haveItems.append(self.meat.name)
            print(f"{self.name}을(를) 도축해서 {self.meat.name}을(를) {a-1}개 얻었다!")
        else:
            print(f"{self.name}을 죽였다.")

        return haveItems, haveAnimals
    
    def breeding(self, money, haveAnimals:list):
        if haveAnimals.count(self.name) >= 2:
            print(f"{self.name}의 번식 확률 {self.breedPer * 100}%, 번식 비용 {self.animalPrice * 0.5}원")
            if check("번식"):
                money -= self.animalPrice * 0.5
                if random.random() <= self.breedPer:
                    haveAnimals.append(self.name)
                    print(f"{self.name}은(는) 번식에 성공했다!")
                else:
                    print(f"{self.name}은(는) 번식에 실패했다...")
        else:
            print("번식을 시도하기에는 개체수가 부족하다...")
        
        return money, haveAnimals
            

        
class Livestock(Item):
    def __init__(self, name, material, sellPrice):
        super().__init__(name, material, sellPrice)

# 아이템
# 제작
Item("빵", ["밀"], 16)
Item("면", ["밀"], 12)
Item("팝콘", ["옥수수"], 30)
Item("치즈", ["우유"], 25)
Item("크림", ["우유"], 25)
Item("크림빵", ["빵", "크림"], 40)
Item("콘치즈", ["옥수수", "치즈"], 70)
Item("치즈버거", ["빵", "치즈", "소고기"], 100)
Item("토마토 케첩", ["토마토"], 15)
Item("핫도그", ["빵", "토마토 케첩", "돼지고기"], 75)
Item("로제 파스타", ["면", "토마토", "크림"], 68)

# 농업
Farm("밀", [Base.FARMING], 8, 1, 0)
Farm("옥수수", [Base.FARMING], 20, 2.5, 10)
Farm("토마토", [Base.FARMING], 12, 2, 6)

# 낙농업
Livestock("우유", [Base.LIVESTOCK], 15)
Livestock("소고기", [Base.LIVESTOCK], 50)
Livestock("돼지고기", [Base.LIVESTOCK], 25)

# 동물
Animal("소", [Base.LIVESTOCK], 50, 45, 150, items["우유"], items["소고기"], 0.2)
Animal("돼지", [Base.LIVESTOCK], 20, None, 70, None, items["돼지고기"], 0.6)

def status():
    print(f"돈: {money}원")
    print("아이템: " + ", ".join(haveItems))
    print("가축: " + ", ".join(haveAnimals))
    
def check(what):
    while True:
        a = input(f"{what}을(를) 시도할까? Y/N ")
        if a == "Y":
            return True
        elif a == "N":
            return False
        else:
            print("Y 혹은 N으로만 입력하자!")

while True:
    a = input("무엇을 할까? ")
    
    if a == "판매":
        b = input("무엇을 판매할까? ")
        if b in items:
            money, haveItems = items[b].sell(money, haveItems)
        else:
            print("판매할 수 없다.")
    elif a == "제작":
        b = input("무엇을 제작할까? ")
        if b in items:
            haveItems = items[b].craft(haveItems)
        else:
            print("제작할 수 없다.")
    elif a == "상태창":
        status()
    elif a == "농사":
        b = input("어떤 작물을 재배할까? ")
        if b in items and isinstance(items[b], Farm):
            money, haveItems = items[b].farming(money, haveItems)
        else:
            print("재배할 수 없다.")
    elif a == "가축 구매":
        b = input("어떤 가축을 구매할까? ")
        if b in items and isinstance(items[b], Animal):
            money, haveAnimals = items[b].buy_animal(money, haveAnimals)
        else:
            print("구매할 수 없다.")
    elif a == "착유":
        b = input("어떤 가축의 젖을 짤까? ")
        if b in haveAnimals and not items[b].milk == None:
            haveItems = items[b].milking(haveItems)
        else:
            print("착유할 수 없다.")
    elif a == "도축":
        b = input("어떤 가축을 도축할까? ")
        if b in haveAnimals:
            haveItems, haveAnimals = items[b].kill(haveItems, haveAnimals)
    elif a == "번식":
        b = input("어떤 가축을 번식시킬까? ")
        if b in haveAnimals:
            money, haveAnimals = items[b].breeding(money, haveAnimals)
        else:
            print("번식할 수 없다.")