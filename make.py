from enum import Enum
import time

items = {}
money = 0
haveItems = []

class Base(Enum):
    FARMING = 1
    LIVESTOCK = 2
    FISHING = 3

class Item:
    def __init__(self, name, material, price):
        self.name = name
        self.material = material
        self.price = price
        
        items[name] = self
        haveItems.append(name)

# 아이템
# 제작
Item("빵", ["밀"], 80)

# 기본 재료
Item("밀", [(Base.FARMING, 0, 2)], 10)
Item("우유", [(Base.LIVESTOCK, 10)])

def sell(name, money, haveItems:list):
    if name in haveItems:
        item = items[name]
        money += item.price
        print(f"{name}을(를) 판매했다!")
        print(f"현재 돈: {money}")
        haveItems.remove(name)
    else:
        print("판매할 수 없는 물건이다!")
        
    return money, haveItems

def craft(name, haveItems:list):
    if name not in items.keys() or isinstance(items[name].material[0][0], Base):
        print("제작할 수 없는 물건이다!")
        return haveItems
    
    item = items[name]
    for i in item.material:
        if i not in haveItems:
            print("재료가 부족해서 제작할 수 없다!")
            return haveItems
    
    for i in item.material:
        haveItems.remove(i)
    
    haveItems.append(name)
    print(f"{name}을(를) 제작했다!")
    return haveItems

def status():
    print(f"돈: {money}")
    print(f"아이템: {haveItems}")
    
def farm(name, money, haveItems:list):
    seed = items[name]
    if items[name].material[0][0] == Base.FARMING:
        money -= seed.material[0][1]
        print("씨앗이 자라나는 중...")
        time.sleep(seed.material[0][2])
        print(f"{name}을(를) 수확했다!")
        haveItems.append(name)
    else:
        print("재배할 수 없는 것이다!")
    
    return money, haveItems

while True:
    a = input("무엇을 할까? ")
    
    if a == "제작":
        b = input("무엇을 제작할까? ")
        haveItems = craft(b, haveItems)
    elif a == "판매":
        b = input("무엇을 판매할까? ")
        money, haveItems = sell(b, money, haveItems)
    elif a == "상태창":
        status()
    elif a == "농사":
        b = input("어떤 작물을 재배할까? ")
        money, haveItems = farm(b, money, haveItems)