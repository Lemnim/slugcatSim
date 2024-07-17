from enum import Enum
import time

items = {}
money = 0
haveItems = []

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
            print("가지고 있지 않은 물건이다!")
            
        return money, haveItems
    
    def craft(self, haveItems:list):
        if isinstance(items[self.name].material[0], Base):
            print("제작할 수 없는 물건이다!")
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
    def __init__(self, name, material, sellPrice, gainTime, animalPrice,):
        super().__init__(name, material, sellPrice)
        
    

# 아이템
# 제작
Item("빵", ["밀"], 16)

# 농업
Farm("밀", [Base.FARMING], 8, 1, 0)
Farm("옥수수", [Base.FARMING], 30, 2.5, 10)

def status():
    print(f"돈: {money}원")
    print(f"아이템: {haveItems}")
    

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