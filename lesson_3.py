temperature = int(input('Укажите температуру воздуха: '))

if temperature >= 25:
    print('На улице жарко!')
elif temperature <= 15:
    print('На улице холодно!')
elif 16 <= temperature < 25:
    print('На улице тепло!')
else:
    print('Погода не определена.')
