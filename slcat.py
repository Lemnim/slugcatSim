import random
import time

slCatHunger = 0
evolutionLevel = 0
friendship = 0
morals = 4
haveItems = []

# 음식
foods = {"박쥐파리" : 1, "팝콘" : 4}

# 아이템
items = {
    "마크식 황금 스테이크": {"효과" : "배고픔 증가", "변화량": 12, "설명": "슬러그캣은 마크식 황금 스테이크를 아주 맛있게 먹었다!\nʕ>.<ʔ: ♥ ♥ ♥!"},
    "분홍색 진주": {"효과": "호감도 증가", "변화량": 200, "설명": "반짝이는 분홍색 진주를 슬러그캣에게 선물했다!\nʕ>.<ʔ: ♥ ♥ ♥!"},
    "착한 슬러그캣이 되는 법 제 1권": {"효과": "도덕성 증가", "변화량": 10, "설명": "슬러그캣에게 책을 읽어주었다.\nʕ●.●ʔ: !"}
}

# 발단 전개 결말
combatScript1 = ["슬러그캣은 독수리와 마주쳤다!", "슬러그캣은 스캐빈저에게 선빵을 쳤다!!", "조심히 기어가던 중, 도마뱀에게 딱 들켜버렸다."]
combatScript2 = ["슬러그캣은 날렵하게 공격을 피했다!", "위기의 순간, 상대에게 결정적인 한방을 꽂아넣었다!", "슬러그캣은 공격을 피하지 못하고 만신창이가 되기 일보직전이다!"]
combatScript3 = ["상대가 더 강력했다... 슬러그캣은 간신히 집으로 돌아왔다.", "슬러그캣은 무사히 집으로 돌아왔다. 전리품도 챙겼다.", "그 순간, 다른 슬러그캣이 슬러그캣을 도와주었다! 슬러그캣은 무사히 집으로 돌아올 수 있었다."]
combatScripts = [combatScript1, combatScript2, combatScript3]


def evolution(hunger, evoLev):
    if hunger >= 4:
        c = hunger // 4
        hunger %= 4
        evoLev += c
        print("배를 가득 채운 슬러그캣은 진화했다!")
        print(f"현재 진화단계는 {evoLev}단계이다!")
        return hunger, evoLev
    else:
        return hunger, evoLev

def feed(hunger, food, friship):
    hunger += food
    friship += 5
    print("슬러그캣은 배를 채웠다!")
    return hunger, friship

def slPupMake(evoLev, friship):
    if evoLev >= 2 and friship >= 100:
        evoLev -= 2
        friship -= 100
        print("슬러그캣은 교배를 시도했다!")
        c = random.random()
        
        for i in range(3):
            print("교배를 시도하는 중." + i * ".")
            time.sleep(1)
    
        
        if c < 0.5:
            print("슬러그캣은 슬러그펍을 낳았다!")
            print("ʕ>.<ʔ: ♥ ♥ ♥!")
            return evoLev, friship
        
        else:
            print("슬러그캣은 다른 슬러그캣에게 차이고 말았다...")
            print("ʕx.xʔ: ...")
            return evoLev, friship
        
    else:
        print("슬러그캣은 아직 다른 슬러그캣에게 관심이 없어보인다...")
        return evoLev, friship

def look(moral, friship):
    friship += 20
    print("슬러그캣은 자신을 관찰하는 당신에게 호감을 느낀다...")
    time.sleep(1)
    
    if moral < 3:
        friship -= 30
        print("슬러그캣은 다른 슬러그캣들과 싸우기 시작했다!!!")
        print("ʕx.xʔ: ! ! ! ! !")
        return moral, friship
    else:
        moral -= 1
        print("슬러그캣은 다른 슬러그캣들과 놀고 있다.")
        print("ʕ●.●ʔ: ? ?")
        print("ʕ>.<ʔ: ! !")
        return moral, friship
        
def study(moral, friship):
    moral += 3
    friship -= 15
    print("슬러그캣을 올바르게 교육시켰다. 그러면 안돼, 슬러그캣!")
    print("ʕ~.~ʔ: ..!")
    return moral, friship

def pet(friship):
    friship += 10
    print("슬러그캣을 쓰담쓰담...")
    print("ʕ●.●ʔ: ♥ ♥ ♥!")
    print(f"현재 호감도는 {friship}이다!")
    return friship

def combat(friship, haveItem):
    for i in combatScripts:
        c = random.choice(i)
        print(c)
        time.sleep(0.65)
        if "전리품" in c:
            drop(haveItem)
        else:
            pass
            
    friship += 50
    print("격렬한 전투를 마친 슬러그캣은 당신에게 깊은 호감을 보인다!")
    print("ʕ●.<ʔ: ♥ ♥ ♥!")
    print(f"현재 호감도는 {friship}이다!")
    return friship, haveItem

def drop(haveItem:list):
    c = items.keys()
    c = random.choice(list(c))
    haveItem.append(c)
    print(f"전리품으로 {c}을(를) 획득했다!")
    return haveItem

def status():
    print("### 슬러그캣의 상태 ###")
    print(f"배고픔: {slCatHunger}")
    print(f"진화 단계: {evolutionLevel}")
    print(f"호감도: {friendship}")
    print(f"도덕성: {morals}")
    print(f"아이템: {haveItems}")
    print("#######################")

def use_item(item, hunger, evoLev, friship, moral):
    effect = item["효과"]
    change = item["변화량"]
    explain = item["설명"]
    
    if effect == "배고픔 증가":
        hunger += change
        print(explain)
        hunger, evoLev = evolution(hunger, evoLev)
        return hunger, evoLev, friship, moral
    elif effect == "호감도 증가":
        friship += change
        print(explain)
        return hunger, evoLev, friship, moral
    elif effect == "도덕성 증가":
        moral += change
        print(explain)
        return hunger, evoLev, friship, moral
    else:
        pass





print("슬러그캣 시뮬레이터!")
while True:
    a = input("무엇을 할까? ")

    if a == "먹이주기":
        b = input("어떤 음식을 먹일까? ")
        if b in foods:
            slCatHunger, friendship = feed(slCatHunger, foods[b], friendship)
            slCatHunger, evolutionLevel = evolution(slCatHunger, evolutionLevel)
        else:
            print("그런 음식은 없다.")
    elif a == "쓰다듬기":
        friendship = pet(friendship)
    elif a == "교배하기":
        evolutionLevel, friendship = slPupMake(evolutionLevel, friendship)
    elif a == "관찰하기":
        morals, friendship = look(morals, friendship)
    elif a == "교육하기":
        morals, friendship = study(morals, friendship)
    elif a == "전투하기":
        friendship, haveItems = combat(friendship, haveItems)
    elif a == "상태창":
        status()
    elif a == "아이템 사용":
        b = input("어떤 아이템을 사용할까? ")
        if b in haveItems:
            slCatHunger, evolutionLevel, friendship, morals = use_item(items[b], slCatHunger, evolutionLevel, friendship, morals)
            haveItems.remove(b)
        else:
            print("그런 아이템은 없다.")
        
    else:
        break