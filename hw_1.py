rain = int(input('На улице идёт дождь? (1: да; 2: нет): '))

if rain == 1:
    print('Советую взять зонт!')
elif rain == 2:
    print('Значит зонт не пригодится!')
else:
    print('Ничего не найдено')

money = int(input('Сколько у тебя денег?: '))

if money >= 35:
    print('Пирожок куплен')

    is_open = False

    days = int(input())

    if is_open:
        print("Магазин открыт!")
        days = days - 1

    print("Количество дней: ", days)

username = input('')
if username == 'superuser':
    print('Вам доступны права суперпользователя')
else:
    print('Вам доступны права обычного пользователя')

password = input('Введите пароль: ')

if password == 'abc_1234567890':
    print('Пароль принят')
else:
    print('Пароль неверный!')

print(10 > 5)

is_raining = True

if is_raining:
    print('На улице дождь')
else:
    print('На улице нету дождя')

    print(
        'Это викторина на знание кухни разных народов. Ответь на вопросы и узнай, насколько хорошо ты разбираешься в еде!')

    question1 = "Кто придумал эчпочмак?"
    question2 = "Луковый суп — это блюдо какой кухни?"
    question3 = "Где родина начос?"
    question4 = "Как называются китайские пельмени?"
    question5 = "В национальную кухню какой страны входят драники?"

    true_answer1 = "татары"
    true_answer2 = "Франция"
    true_answer3 = "Мексика"
    true_answer4 = "гёдза"
    true_answer5 = "Беларусь"

    score = 0

    answer1 = input(question1)
    if answer1 == 'татары':
        score += 1

    answer2 = input(question2)
    if answer2 == 'Франция':
        score += 1

    answer3 = input(question3)
    if answer3 == 'Мексика':
        score += 1

    answer4 = input(question4)
    if answer4 == 'гёдза':
        score += 1

    answer5 = input(question5)
    if answer5 == 'Беларусь':
        score += 1

    if score >= 3:
        print('Вы набрали много баллов! Вас можно считать экспертом')
    else:
        print('Вы набрали не очень много баллов. Расширяйте свой кругозор, вам есть, куда стремиться')

        print('Это тест "Кто ты из "Колобка". Отвечай на вопросы и узнаешь, на кого ты больше похож!')

        question1 = "Если тебе нечего делать, то чем ты займёшься?"
        question2 = "Как ты поздороваешься с кем-то незнакомым?"
        question3 = "Покажешь ли ты дорогу незнакомцу?"
        question4 = "Ты всегда найдёшь, что поесть?"
        question5 = "Как часто ты споришь с кем-то?"

        kolobok_points = 0

        print(question1)
        print("1. Пойду скрести по сусекам. 2. Пойду гулять.")
        answer1 = input("Введите ответ цифрой: ")

        if answer1 == 2:
            kolobok_points += 1

        print(question2)
        print("1. Вежливо. 2. Засмеюсь и поздороваюсь, как будто его знаю.")
        answer2 = input("Введите ответ цифрой: ")

        if answer2 == 2:
            kolobok_points += 1

        print(question3)
        print("1. Да. 2. Нет.")
        answer3 = input("Введите ответ цифрой: ")

        if answer3 == 1:
            kolobok_points += 1

        print(question4)
        print("1. Да. 2. Нет.")
        answer4 = input("Введите ответ цифрой: ")

        if answer4 == 1:
            kolobok_points += 1

        print(question5)
        print("1. Часто. 2. Редко.")
        answer5 = input("Введите ответ цифрой: ")

        if answer5 == 1:
            kolobok_points += 1

        if kolobok_points >= 3:
            print('Из сказки "Колобок" ты определённо сам Колобок! Такой же непосредственный и бесстрашный')
        else:
            print('Из сказки "Колобок" ты бабка, которая испекла Колобка! Вежливый и приятный человек')

            # преобразуй число в строку, используя str();
            number = 10
            str_number = str(number)

            # получи дробное число из input();
            float_number = float(input('Введите дробное число: '))

            # с помощью команды type() проверь тип числа
            print(type(str_number))
            print(type(float_number))
