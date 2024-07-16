from enum import Enum

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
    item = items[name]
    for i in item.material:
        if i in haveItems:
            haveItems.remove(i)
        else:
            print("재료가 부족해서 제작할 수 없다!")
            return
        
    print(f"{name}을(를) 제작했다!")
    haveItems.append(name)
    return haveItems

def status():
    print(f"돈: {money}")
    print(f"아이템: {haveItems}")
        
Item("빵", ["밀"], 80)
Item("밀", [Base.FARMING], 10)


while True:
    a = input("무엇을 할까? ")
    
    if a == "제작하기":
        b = input("무엇을 제작할까? ")
        haveItems = craft(b, haveItems)
    elif a == "판매하기":
        b = input("무엇을 판매할까? ")
        money, haveItems = sell(b, money, haveItems)
    elif a == "상태창":
        status()