# Preexposition for the the text adventure.

print("Добро пожаловать в текстовое путешествие за \n",
"бутербродом в Новосибирском Государственном Университете! \n \n")


# defining ans for all further while cycles
ans = 0

# STORY BEGINNING
while ans < 1, ans > 2:
    # question block asks a question, asks for an input and proposes answers
    ans = input("Вы решили сьесть бутерброд в Новосибирском \n",
    "Государственном Университете. У вас есть 2 выбора: \n",
    "1) Сходить за ним в Торговый Центр. \n",
    "2) Купить его в Новосибирском Государственном Университете.")
    try:
        ans = int(ans)
    except TypeError:
        print("Неправильный ввод, попробуйте ещё.")
        ans = 0
# FIRST BRANCHING


# TC ROUTE
if ans = 1:
    ans = 0
    while ans < 1, ans > 2:
    ans = input("Вы решили сходить за бутербродом в Торговый\n",
    "Центр. Первое препятствие - перекрёсток: \n",
    "1) Перебежать на красный свет и не ждать. \n",
    "2) Подождать зелёного и безопасно перейти.")
    try:
        ans = int(ans)
    except Typeerror:
        print("Неправильный ввод, попробуйте ещё.")
        ans = 0
    
    # CROSSROADS BAD END
    if ans = 1:
    print("К сожалению, вас сбила машина, что не позволило \n",
    "вам получить бутерброд ещё несколько дней. Плохая концовка.")
    
    # CROSSROADS SAFE CONTINUATION
    if ans = 2:
    ans = 0
    while ans < 1, ans > 2:
    ans = input("Вы безопасно пришли в Торговый Центр \n",
    "следующий вопрос - какой магазин продает бутерброды?: \n",
    "1) Суши - Маке. \n",
    "2) Продуктовый.")
    try:
        ans = int(ans)
    except TypeError:
        print("Неправильный ввод, попробуйте ещё.")
        ans = 0
        
        # BAD STORE END
        if ans = 1:
            print("Внимательно изучив ассортимент Суши - Маке, \n",
            "вы разочаровались в отсутствии бутербродов, но, не унывая, \n",
            "отправились в продуктовый, где, купив бутербров, побежали \n",
            "на пару, однако опоздали на пять минут. Плохая концовка.")
        
        # GOOD STORE END
        if ans = 2:
            print("Вы неспешно купили бутерброд в продуктовом магазине, \n",
            "спокойно пошли на пару и даже успели сьесть бутерброд по дороге \n",
            "и успели на пару. Хорошая концовка.")

# NSU ROUTE
if ans = 2:
    ans = 0
    while ans < 1, ans > 2:
    ans = input("Вы решили купить бутерброд в Новосибирском\n",
    "Государственном Университете. Куда вы идёте: \n",
    "1) 3333 кабинет \n",
    "2) Кафе Ca'Va в первом блоке.")
    try:
        ans = int(ans)
    except TypeError:
        print("Неправильный ввод, попробуйте ещё.")
        ans = 0

    # 3333 ROUTE OF HEAVEN (?)
    if ans = 1:
        ans = 0
    while ans < 1, ans > 2:
    ans = input("Вы решили купить бутерброд в 3333, \n",
    "однако, бутербродов много, глаза расходятся.. \n",
    "Какой именно бутерброд вы возмёте?: \n",
    "1) Чёрный с котлетой \n",
    "2) Нарезанное мясо в лаваше.")
    try:
        ans = int(ans)
    except TypeError:
        print("Неправильный ввод, попробуйте ещё.")
        ans = 0
    print("Вы всё же что-то взяли, и оно было вкусно. \n",
    "Бутерброд получен. Хорошая концовка.")


    # CA'VA ROUTE OF DOOM
    if ans = 2:
        ans = 0
    while ans < 1, ans > 2:
    ans = input("Вы решили купить бутерброд в Ca'Va \n",
    "однако, бутербродов не оказалось в наличии. \n",
    "Что вы возмёте взамен?: \n",
    "1) Эклеры \n",
    "2) Кофе.")
    try:
        ans = int(ans)
    except TypeError:
        print("Неправильный ввод, попробуйте ещё.")
        ans = 0
    print("Несмотря на то, что вы всё же что-то взяли, \n",
    "бутерброд не получен. Плохая концовка.")
        

    
