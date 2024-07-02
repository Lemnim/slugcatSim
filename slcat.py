import random
import time

slCatHunger = 0
evolutionLevel = 0
friendship = 0
morals = 4

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
    time.sleep(1.5)
    
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

foods = {"박쥐파리" : 1, "팝콘" : 4}


print("슬러그캣 시뮬레이터!")
while True:
    a = input("무엇을 할까? ")

    if a == "먹이주기":
        b = input("어떤 음식을 먹일까? ")
        slCatHunger, friendship = feed(slCatHunger, foods[b], friendship)
        slCatHunger, evolutionLevel = evolution(slCatHunger, evolutionLevel)
    elif a == "쓰다듬기":
        friendship = pet(friendship)
    elif a == "교배하기":
        evolutionLevel, friendship = slPupMake(evolutionLevel, friendship)
    elif a == "관찰하기":
        morals, friendship = look(morals, friendship)
    elif a == "교육하기":
        morals, friendship = study(morals, friendship)
        
    else:
        break
