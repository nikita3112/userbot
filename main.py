from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from time import sleep
import random



app = Client("my_account")


@app.on_message(filters.command('help', prefixes='.') & filters.me)
def help(_, msg):
    commands = '''
                .help - Выводит все доступные команды\n
                .type text - Анимация печчати\n
                .gay - Гей тест (выбирает рандом челика из группы или лс)\n
                .gaytest - Аналог .gay предназначенный для проверки одного пользвателя (в ответ на его сообщение отправить команду)\n
                .love text - Анимация сердечка\n
                .random from to - Рандомное число от и до
                '''
    msg.edit(commands)

@app.on_message(filters.command('type', prefixes='.') & filters.me)
def type(_, msg):
    orig_text = msg.text.split('.type ', maxsplit=1)[1]
    text = orig_text
    tbp = ''
    typing_symbol = '▒'

    while tbp != orig_text:
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05)

            tbp += text[0]
            text = text[1:]
            msg.edit(tbp)
            sleep(0.05)

        except FloodWait as e:
            sleep(e.x)

@app.on_message(filters.command('gay', prefixes='.') & filters.me)
def gay(_, msg):
    proc = 0

    while proc < 100:
        try:
            text = '💩 Поиск гея ... ' + str(proc) + '%'
            msg.edit(text)

            proc += random.randint(1, 5)
            sleep(0.1)
        except FloodWait as e:
            sleep(e.x)

    if msg.chat.type in ['group', 'supergroup']:
        members = [i for i in app.get_chat_members(msg.chat.id) if not i.user.is_bot]

        text = f'Гей обнаружен 😧\n👉 @{random.choice(members).user.username}'
    elif msg.chat.type == 'private':
        text = f'Гей обнаружен 😧\n👉 @{random.choice([msg.from_user.username, msg.chat.username])}'
    msg.edit(text)

@app.on_message(filters.command('gaytest', prefixes='.') & filters.me)
def gay_test(_, msg):
    text = '💩 Проверка пользователя на пидора ... '
    proc = 0

    while proc < 100:
        try:
            msg.edit(text + str(proc) + '%')
            proc += random.randint(1, 5)
        except FloodWait as e:
            sleep(e.x)
    
    if bool(random.getrandbits(1)):
        try:
            msg.edit('Пользователь пидор 😧')
        except FloodWait as e:
            sleep(e.x)
    else:
        try:
            msg.edit('Пользователь не пидор 😃')
        except FloodWait as e:
            sleep(e.x)

@app.on_message(filters.command('love', prefixes='.') & filters.me)
def love(_, msg):
    '''❤️🧡💛💚💙💜🖤🤍🤎'''
    orig_text = msg.text.split('.love ', maxsplit=1)[1]
    harts = ['🧡', '💛', '💚', '💙', '💜', '🖤', '🤎']
    arr = ['🤍❤️❤️🤍❤️❤️🤍\n', '❤️❤️❤️❤️❤️❤️❤️\n', '❤️❤️❤️❤️❤️❤️❤️\n', '🤍❤️❤️❤️❤️❤️🤍\n', '🤍🤍❤️❤️❤️🤍🤍\n', '🤍🤍🤍❤️🤍🤍🤍']
    text = ''
    for i in arr:
        text += i
        try:
            msg.edit(text)
        except FloodWait as e:
            sleep(e.x)
        sleep(0.5)

    main_hart = '❤️'
    for i in range(len(harts)):
        text = text.replace(main_hart, harts[i])
        try:
            msg.edit(text)
            sleep(0.5)
        except FloodWait as e:
            sleep(e.x)
        main_hart = harts[i]
    
    text = '🤍❤️❤️🤍❤️❤️🤍\n❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️\n🤍❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️🤍🤍\n🤍🤍🤍❤️🤍🤍🤍'
    msg.edit(text)
    sleep(0.5)

    for i in range(10):
        new_text = text
        while '❤️' in new_text:
            new_text = new_text.replace('❤️', random.choice(harts), 1)
        try:
            msg.edit(new_text)
            sleep(0.5)
        except FloodWait as e:
            sleep(e.x)
    
    text = '🤍❤️❤️🤍❤️❤️🤍\n❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️\n🤍❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️🤍🤍\n🤍🤍🤍❤️🤍🤍🤍'
    msg.edit(text)
    sleep(0.5)

    while '🤍' in text:
        text = text.replace('🤍', '❤️', 1)
        try:
            msg.edit(text)
            sleep(0.1)
        except FloodWait as e:
            sleep(e.x)
    
    text = [
        '❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️',
        '❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️',
        '❤️❤️❤️❤️\n❤️❤️❤️❤️\n❤️❤️❤️❤️\n❤️❤️❤️❤️',
        '❤️❤️❤️\n❤️❤️❤️\n❤️❤️❤️',
        '❤️❤️\n❤️❤️',
        '❤️',
        f'||__{orig_text}__||'
    ]

    for i in text:
        try:
            msg.edit(i)
            sleep(0.3)
        except FloodWait as e:
            sleep(e.x)

@app.on_message(filters.command('x', prefixes='.') & filters.me)
def x(_, msg):
    '''⬜️🟥🟧🟨🟩🟦🟪⬛️🟫'''
    cubes = ['🟥', '🟧', '🟨', '🟩', '🟦', '🟪', '⬛️', '🟫', '⬜️']
    text = '⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️'

    msg.edit(text)

    new_text = text
    old_cube = cubes[-1]
    while True:
        for i in cubes:
            while old_cube in new_text:
                new_text = new_text.replace(old_cube, i, 1)
                try:
                    msg.edit(new_text)
                except FloodWait as e:
                    sleep(e.x)
                sleep(1)
            old_cube = i

@app.on_message(filters.command('random', prefixes='.') & filters.me)
def random_num(_, msg):
    text = msg.text.split('.random ', maxsplit=1)[1]
    nums = text.split(maxsplit=1)

    for i, num in enumerate(nums):
        try:
            num = int(num)
        except ValueError:
            msg.edit('Вы ввели не число')
        nums[i] = num
    
    msg.edit(random.randint(nums[0], nums[1]))

app.run()