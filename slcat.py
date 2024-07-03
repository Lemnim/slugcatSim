import random
import time

slCatHunger = 0
evolutionLevel = 0
friendship = 0
morals = 4

# 발단 전개 결말
combatScript1 = ["슬러그캣은 독수리와 마주쳤다!", "슬러그캣은 스캐빈저에게 선빵을 쳤다!!", "조심히 기어가던 중, 도마뱀에게 딱 들켜버렸다."]
combatScript2 = ["슬러그캣은 날렵하게 공격을 피했다!", "위기의 순간, 상대에게 결정적인 한방을 꽂아넣었다!", "슬러그캣은 공격을 피하지 못하고 만신창이가 되기 일보직전이다!"]
combatScript3 = ["상대가 더 강력했다... 슬러그캣은 간신히 집으로 돌아왔다.", "슬러그캣은 무사히 집으로 돌아왔다. 전리품도 챙겼다.", "그 순간, 다른 슬러그캣이 슬러그캣을 도와주었다! 슬러그캣은 무사히 집으로 돌아올 수 있었다."]
combatScripts = [combatScript1, combatScript2, combatScript3]


def evolution(hunger, evoLev):
    if hunger >= 4:
        hunger -= 4
        evoLev += 1
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
    
    if moral > 6:
        friship -= 30
        print("슬러그캣은 흙을 주워 먹는다!!!")
        print("ʕx.xʔ: ! ! ! ! !")
        return moral, friship
    else:
        moral += 1
        print("슬러그캣은 다른 슬러그캣들과 놀고 있다.")
        print("ʕ●.●ʔ: ? ?")
        print("ʕ>.<ʔ: ! !")
        return moral, friship
        
def study(moral, friship):
    moral -= 3
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

def combat(friship, combatscript):
    for i in combatscript:
        print(random.choice(i))
        time.sleep(0.65)
    friship += 50
    print("격렬한 전투를 마친 슬러그캣은 당신에게 깊은 호감을 보인다!")
    print("ʕ●.<ʔ: ♥ ♥ ♥!")
    print(f"현재 호감도는 {friship}이다!")
    return friship

foods = {"박쥐파리" : 1, "팝콘" : 4}


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
        friendship = combat(friendship, combatScripts)
        
    else:
        break