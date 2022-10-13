def minimario():
    orochimary = int(input("Дай первые циферки: "))
    jiraia = int(input("Ну там, короче ещё нужно: "))
    cynade = int(input("Обещаю,это последнее: "))
    print("Минимальное число: ", min(orochimary, jiraia, cynade))

def skolkovsego():
    print("Ах ты проказник, ну вот держи :", len(input("Над каким числом хочешь поиздеваться?:")))
def sumka():
    itachi = int(input('Откуды-докуды: '))
    print('Ох,как же было сложно тааа:', sum(range(1, itachi + 1)))
def factortipo():
    n = int(input('Какое число факторнуть: '))
    naruto = 1
    while n > 1:
        naruto *= n
        n -= 1
    print('На получай:', naruto)
print("Ай, шо хочещъ дарагой?")
print('1- Мои минимальные числа')
print('2 - Там типо сколько цифр в твоём числе')
print('3 - Ох,сложна, в общем сумма всех чисел от 1 до твоего числа, понел?')
print('4 - Мистер Факториал, хочет с вами познакомиться')
number = int(input())
if number == 1:
    minimario()
else:
    if number == 2:
        skolkovsego()
    else:
        if number == 3:
            sumka()
        else:
            if number == 4:
                factortipo()

