import random
import time

slCatHunger = 0
evolutionLevel = 0
friendship = 0
morals = 4
haveItems = []
recipes = []
sickness = False

# 음식
foods = {"박쥐파리" : 1, "팝콘" : 4}

# 아이템
items = {}

class ItemMake:
    def __init__(self, name, effect, change, explain, canMake, makeScript):
        self.name = name
        self.effect = effect
        self.change = change
        self.explain = explain
        self.canMake = canMake
        self.makeScript = makeScript

        items[name] = {"효과": effect, "변화량": change, "설명": explain, "제작가능": canMake, "제작대사": makeScript}

ItemMake("마크식 황금 스테이크", ["배고픔 증가"], [12], "슬러그캣은 마크식 황금 스테이크를 아주 맛있게 먹었다!\nʕ>.<ʔ: ♥ ♥ ♥!", False, None)
ItemMake("분홍색 진주", ["호감도 증가"], [200], "반짝이는 분홍색 진주를 슬러그캣에게 선물했다!\nʕ>.<ʔ: ♥ ♥ ♥!", False, None)
ItemMake("착한 슬러그캣이 되는 법 제 1권", ["도덕성 증가"], [10], "슬러그캣에게 책을 읽어주었다.\nʕ●.●ʔ: !", False, None)
ItemMake("푸딩", ["배고픔 증가"], [7], "슬러그캣에게 맛있는 푸딩을 먹였다!\nʕ●.●ʔ: ♥!", True, "우유를 데우고.. 젤라틴을 넣고... \nʕ●.●ʔ: !")
ItemMake("육개장 사발면", ["배고픔 증가", "호감도 증가"], [3, 30], "슬러그캣은 육개장 사발면을 매워하면서 먹었다!\nʕx.xʔ: ♥ ♥!", True, "물을 끓이고.. 기다림의 시간...\nʕu.uʔ: z..!")
ItemMake("달콤바삭 애플파이", ["배고픔 증가", "호감도 증가", "도덕성 증가"], [2, 50, 6], "슬러그캣은 달콤하고 바삭한 애플파이를 정말 좋아했다!\nʕ>.<ʔ: ♥ ♥ ♥!", True, "사과를 졸이고.. 파이에 넣어서... 굽기!\nʕ●.●ʔ: ♥!")
ItemMake("카르마 꽃", ["치유"], [1], "슬러그캣은 카르마 꽃을 달여먹었다... \nʕ●.●ʔ: !", False, None)
ItemMake("보리차", ["치유", "도덕성 증가"], [0.5, 1], "슬러그캣과 같이 따뜻한 보리차를 마셨다!\nʕu.uʔ: !", True, "보리를 볶고.. 물을 끓여서...\nʕ●.●ʔ: !")

# 발단 전개 결말

# 전투 스크립트
combatScript1 = ["슬러그캣은 독수리와 마주쳤다!", "슬러그캣은 스캐빈저에게 선빵을 쳤다!!", "조심히 기어가던 중, 도마뱀에게 딱 들켜버렸다.", "슬러그캣은 하양도마뱀을 눈치채지 못하고 밟아버렸다!", "파이프를 기어가던 중 지네와 맞닥뜨렸다!", "어두운 곳, 슬러그캣은 거미에게 발각당했다!"]
combatScript2 = ["슬러그캣은 날렵하게 공격을 피했다!", "위기의 순간, 상대에게 결정적인 한방을 꽂아넣었다!", "슬러그캣은 공격을 피하지 못하고 만신창이가 되기 일보직전이다!", "상대의 회심의 일격! 슬러그캣은 가까스로 피했다!", "슬러그캣의 지능적인 공격! 방심하던 상대의 헛점을 찔렀다.", "슬러그캣은 상대와 비등비등하게 싸우고 있다!"]
combatScript3 = ["상대가 더 강력했다... 슬러그캣은 간신히 집으로 돌아왔다.", "휴우, 슬러그캣은 무사히 집으로 돌아왔다. 전리품도 챙겼다.", "그 순간, 다른 슬러그캣이 슬러그캣을 도와주었다! 슬러그캣은 무사히 집으로 돌아올 수 있었다.", "그런 상황에서도, 슬러그캣은 전리품을 챙겨 달아났다.", "슬러그캣은 성공적으로 적을 물리쳤다!", "몸은 만신창이가 되었지만, 전리품은 얻어서 돌아갈 수 있었다."]
combatScripts = [combatScript1, combatScript2, combatScript3]

# 관찰(불량) 스크립트
badMoralScript = ["슬러그캣은 다른 슬러그캣들과 싸우기 시작했다!!!\nʕx.xʔ: ! ! ! ! !", "슬러그캣은 흙을 주워먹는다!!!\nʕo.oʔ: ? ? ?", "슬러그캣은 스캐빈저에게 손가락 욕을 날린다!\nʕ-.-ʔ: ㅗ", "슬러그캣은 껄렁한 포즈를 취한다!\nʕo.oʔ: ㅗ", "슬러그캣은 벽에다가 발길질을 하기 시작했다!!\nʕ-.-ʔ: ! !"]

# 관찰(일반) 스크립트
goodMoralScript = ["슬러그캣은 다른 슬러그캣들과 놀고 있다.\nʕ●.●ʔ: ? ?\nʕ>.<ʔ: ! !", "슬러그캣은 높은 하늘을 관찰하고 있다. \nʕ●.●ʔ: ..!", "슬러그캣은 열심히 창을 갈고 닦고 있다.\nʕ●.●ʔ: ! !", "슬러그캣은 조용히 명상하고 있다...\nʕu.uʔ: ...", "슬러그캣은 잠시 낮잠을 자는 것 같다.\nʕu.uʔ: Zzz..."]

def evolution(hunger, evoLev):
    if hunger >= 4:
        evoLev += hunger // 4
        hunger %= 4
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
    print("슬러그캣은 자신을 관찰하는 당신에게 호감을 느낀다...")
    time.sleep(0.6)
    moral -= random.randint(1, 2)
    
    if moral <= 0:
        friship -= 10
        print(random.choice(badMoralScript))
        return moral, friship
    else:
        friship += 35
        print(random.choice(goodMoralScript))
        
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

def combat(friship, haveItem, sick):
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

    if 0.2 >= random.random():
        sick = True
        print("슬러그캣은 이번 전투에서 병에 걸렸다! 콜록 콜록...")
    else:
        pass

    return friship, haveItem, sick

def drop(haveItem:list):
    c = random.choice(list(items.keys()))
    haveItem.append(c)
    print(f"전리품으로 {c}을(를) 획득했다!")
    return haveItem

def status():
    print("####슬러그캣의 상태####")
    print(f"배고픔: {slCatHunger}")
    print(f"진화 단계: {evolutionLevel}")
    print(f"호감도: {friendship}")
    print(f"도덕성: {morals}")
    print(f"아이템: {haveItems}")
    print(f"질병: {sickness}")
    print("#######################")

def use_item(item, hunger, evoLev, friship, moral, sick):
    print(item["설명"])
    for i in range(len(item["효과"])):
        effect = item["효과"][i]
        change = item["변화량"][i]

        if effect == "배고픔 증가":
            hunger += change
            hunger, evoLev = evolution(hunger, evoLev)
        elif effect == "호감도 증가":
            friship += change
        elif effect == "도덕성 증가":
            moral += change
        elif effect == "치유" and sick:
            if change >= random.random():
                sick = False
                print("병이 치유되었다!")
            else:
                print("슬러그캣은 아직 병에서 회복하지 못했다...")
    
    return hunger, evoLev, friship, moral, sick

def cook(friship, haveItem:list, whatMake):
    friship -= 75
    haveItem.append(whatMake)
    print(items[whatMake]["제작대사"])
    time.sleep(0.5)
    print(f"슬러그캣과 같이 {whatMake}을(를) 요리했다!")
    return friship, haveItem

def sick(friship, moral):
    print("슬러그캣은 병에 걸려있다... 어서 치유해주자!")
    print("ʕx.xʔ: ! !")
    if 0.5 > random.random():
        c = random.randint(5, 55)
        friship -= c
        print(f"아파서 호감도가 {c}만큼 하락했다...")
    if 0.5 > random.random():
        c = random.randint(1, 3)
        moral -= c
        print(f"아파서 도덕성이 {c}만큼 하락했다...")

    return friship, moral

print("슬러그캣 시뮬레이터!")
while True:
    if sickness:
        friendship, morals = sick(friendship, morals)
    else:
        pass

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
        friendship, haveItems, sickness = combat(friendship, haveItems, sickness)
    elif a == "상태창":
        status()
    elif a == "아이템 사용":
        b = input("어떤 아이템을 사용할까? ")
        if b in haveItems:
            slCatHunger, evolutionLevel, friendship, morals, sickness = use_item(items[b], slCatHunger, evolutionLevel, friendship, morals, sickness)
            haveItems.remove(b)
        else:
            print("그런 아이템은 없다.")
    elif a == "요리하기":
        if friendship >= 75:
            b = input("어떤 음식을 요리할까? ")
            if items[b]["제작가능"]:
                friendship, haveItems = cook(friendship, haveItems, b)
            else:
                print("요리할 수 없는 것이다.")
        else:
            print("슬러그캣은 요리하고 싶지 않은 것 같다...")
        
    else:
        break