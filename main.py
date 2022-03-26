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
                .random from to - Рандомное число от и до\n
                .autodroch - Автоматически фармит @xyu_epta_bot в группе
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

@app.on_message(filters.command('flag', prefixes='.') & filters.me)
def flag(_, msg):
    '''⬜️🟦🟥🟨'''
    ru = '⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️\n🟦🟦🟦🟦🟦🟦\n🟦🟦🟦🟦🟦🟦\n🟥🟥🟥🟥🟥🟥\n🟥🟥🟥🟥🟥🟥'
    ua = '🟦🟦🟦🟦🟦🟦\n🟦🟦🟦🟦🟦🟦\n🟦🟦🟦🟦🟦🟦\n🟨🟨🟨🟨🟨🟨\n🟨🟨🟨🟨🟨🟨\n🟨🟨🟨🟨🟨🟨'
    plus = '⬜️⬜️🟥🟥⬜️⬜️\n⬜️⬜️🟥🟥⬜️⬜️\n🟥🟥🟥🟥🟥🟥\n🟥🟥🟥🟥🟥🟥\n⬜️⬜️🟥🟥⬜️⬜️\n⬜️⬜️🟥🟥⬜️⬜️'
    ravno = '🟥🟥🟥🟥🟥🟥\n🟥🟥🟥🟥🟥🟥\n⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️\n🟥🟥🟥🟥🟥🟥\n🟥🟥🟥🟥🟥🟥'

    msg.edit(ru)
    sleep(1)
    msg.edit(plus)
    sleep(1)
    msg.edit(ua)
    sleep(1)
    msg.edit(ravno)
    sleep(1)
    msg.edit(ru)

@app.on_message((filters.command('autodroch', prefixes='.') & filters.me) | (filters.user(1303228016) & filters.reply))
def autodroch(_, msg):
    minutes = ['минуты', 'минуту', 'минут']
    hours = ['часа', 'часов', 'час']

    if msg.from_user.is_self:
        msg.edit('Автодроч запущен!')
        app.send_message(msg.chat.id, '/drochnut@xyu_epta_bot')
        sleep(1)
        app.send_message(msg.chat.id, '/dick@xyu_epta_bot')
        sleep(1)
        app.send_message(msg.chat.id, '/case@xyu_epta_bot')
    elif msg.reply_to_message.from_user.is_self and msg.reply_to_message.text == "/drochnut@xyu_epta_bot":
        time = msg.text.split('через ')[1].split(' ⏰')[0]
        hour = minute = 0

        for i in hours:
            if i in time:
                hour = int(time.split(i)[0].strip())
                time = time.split(i)[1].strip()
                break
        
        for j in minutes:
            if j in time:
                minute = int(time.split(j)[0].strip())
                break
        
        text = 'Ждем ' + (str(hour) + ' час ' if hour else '') + (str(minute) + ' минуты' if minute else '')
        print('DROCH -- ' + text)

        wait_time = (hour * 3600 if hour else 0) + (minute * 60 if minute else 0)
        sleep(wait_time + 60)

        app.send_message(msg.chat.id, '/drochnut@xyu_epta_bot')
        print('DROCH -- Дрочим')
    elif msg.reply_to_message.from_user.is_self and msg.reply_to_message.text == "/dick@xyu_epta_bot":
        print('DICK -- Ждем 6 часов')
        sleep((6 * 3600) + 60)
        app.send_message(msg.chat.id, '/dick@xyu_epta_bot')
        print('DICK -- Растим письку')
    elif msg.reply_to_message.from_user.is_self and msg.reply_to_message.text == "/case@xyu_epta_bot":
        print('CASE -- Ждем сутки')
        sleep((24 * 3600) + 60)
        app.send_message(msg.chat.id, '/case@xyu_epta_bot')
        print('CASE -- Открываем кейс')

app.run()