import telebot
from config import token # импорт токена
from telebot import types # для указание типов

# Создаем экземпляр бота
bot = telebot.TeleBot(token)

# Создаём функцию с начальной командой start
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Этот объект представляет клавиатуру с опциями ответа
    item1 = types.KeyboardButton("/pusk") # Название нашей кнопки
    markup.add(item1)  # Дальше к клавиатуре добавим нашу кнопку
    bot.send_message(message.chat.id, 'Привет, {0.first_name}! Со мной у тебя будет всегда вариант для ужина!'.format(message.from_user), reply_markup=markup)
    bot.send_message(message.chat.id, 'Нажми на pusk,чтобы начать работу') # Выводим сообщения для пользователя

# Создаём функцию с командой pusk
@bot.message_handler(commands=["pusk"])
def pusk(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Этот объект представляет клавиатуру с опциями ответа
    item2 = types.KeyboardButton("/menu")
    markup.add(item2)
    bot.send_message(message.chat.id,'Для того, чтобы сделать выбор перейди по кнопке menu', reply_markup=markup)

import random
# Создаем список словарей / РЕЦЕПТЫ ЛЁГКОГО УЖИНА
light_dinner = [
    {"text": "Готовим филе минтая в кляре без муки",
     "url": "https://alimero.ru/blog/recepti/gotovim-file-mintaya-v-klyare-bez-muki-ochen-prosto-i-vkusno.167762.html"},
    {"text": "Готовим куриное филе с ананасами в томатном соусе",
     "url": "https://alimero.ru/blog/recepti/kak-bistro-prigotovit-kurinoe-file-s-ananasami-v-tomatnom-souse.34402.html"},
    {"text": "Готовим Ленивые голубцы в духовке",
     "url": "https://alimero.ru/blog/recepti/lenivie-golubtsi-v-duhovke-samiy-udachniy-retsept.33459.html"},
    {"text": "Рецепт томленой в сметане картошки с куриным филе ",
     "url": "https://alimero.ru/blog/recepti/retsept-tomlenoy-v-smetane-kartoshki-s-kurinim-file-vkusno-sitno-prosto.167888.html"},
    {"text": " Готовим сочные куриные грудки с овощами",
     "url": " https://alimero.ru/blog/recepti/sochnie-kurinie-grudki-s-ovoshchami-za-20-minut.169751.html"},
    {"text": "Готовим рис с овощами в духовке ",
     "url": " https://alimero.ru/blog/recepti/ris-s-ovoshchami-v-duhovke-samiy-prostoy-retsept.171749.html"},
    {"text": " Вкуснейшая тушеная капуста с мясом, чесноком и специями",
     "url": " https://alimero.ru/blog/recepti/vkusneyshaya-tushenaya-kapusta-s-myasom-chesnokom-i-spetsiyami.173201.html"},
]

@bot.message_handler(commands=["dinner"])
def dinner(message):
    # Выбираем случайный словарь из списка
    sluchay_dinner_1 = random.choice(light_dinner)

    # Получаем текст и ссылку из выбранного словаря
    recept_1 = sluchay_dinner_1["text"]
    url_1 = sluchay_dinner_1["url"]
    # Создаём переменную, к-я включает в себя название рецепта и ссылку на сайт
    dinner_1 = recept_1 + url_1
    print(dinner_1)

    bot.send_message(message.chat.id, "Приятного аппетита!\n" + dinner_1)

# РЕЦЕПТЫ БЫСТРОГО УЖИНА
quick_dinner = [
    { "r": "Рецепт куриных ножек в духовке с корочкой ",
          "url": "https://menunedeli.ru/recipe/recept-kurinyx-nozhek-v-duxovke-s-korochkoj/"},
    { "r": "Макароны в духовке без варки",
          "url":"https://menunedeli.ru/recipe/makarony-v-duxovke-bez-varki/"},
    { "r": "Овощное рагу с кабачками и картошкой ",
          "url":"https://menunedeli.ru/recipe/ovoshhnoe-ragu-s-kabachkami-i-kartoshkoj/"},
    { "r": "Рагу из овощей со сладким перцем ",
          "url":"https://menunedeli.ru/recipe/ragu-iz-ovoshhej-so-sladkim-percem/"},
    { "r": "Пицца 'Минутка' ",
          "url":"https://povar.ru/recipes/picca_minutka-9916.html"},
    { "r": " Кета в кляре",
          "url":"https://povar.ru/recipes/keta_v_klyare-10017.html"},
    { "r": " Паста с шампиньонами",
          "url":"https://povar.ru/recipes/pasta_s_shampinonami-10780.html"},
]

@bot.message_handler(commands=["dinner2"])
def dinner2(message):
    # Выбираем случайный словарь из списка
    sluchay_dinner_2 = random.choice(quick_dinner)

    # Получаем текст и ссылку из выбранного словаря
    recept_2 = sluchay_dinner_2["r"]
    url_2 = sluchay_dinner_2["url"]
    # Создаём переменную
    dinner_2 = recept_2 + url_2
    print(dinner_2)

    bot.send_message(message.chat.id, "Приятного аппетита!\n" + dinner_2)

pp_din = [
    { "r": " Минтай с морковью и луком (в духовке)",
          "url":"https://www.iamcook.ru/showrecipe/7459"},
    { "r": "Кабачки с картошкой и помидорами в духовке ",
          "url":"https://www.iamcook.ru/showrecipe/12401"},
    { "r": "Подлива из курицы со сметаной ",
          "url":"https://www.iamcook.ru/showrecipe/16186"},
    { "r": " Диетические куриные маффины",
          "url":"https://www.iamcook.ru/showrecipe/16353"},
    { "r": "Куриное филе запеченное в кефире ",
          "url":"https://www.iamcook.ru/showrecipe/6027"},
    { "r": "Тушеная пекинская капуста ",
          "url":"https://www.iamcook.ru/showrecipe/13975"},
    { "r": "Скумбрия с овощами в горшочках в духовке ",
          "url":"https://www.iamcook.ru/showrecipe/17526"},
]

@bot.message_handler(commands=["pp_dinner"])
def pp_dinner(message):
    # Выбираем случайный словарь из списка
    sluchay_dinner_6 = random.choice(pp_din)

    # Получаем текст и ссылку из выбранного словаря
    recept_6 = sluchay_dinner_6["r"]
    url_6 = sluchay_dinner_6["url"]
    # Создаём переменную
    pp_dinner_ = recept_6 + url_6
    print(pp_dinner_)

    bot.send_message(message.chat.id, "Приятного аппетита!\n" + pp_dinner_)


# РЕЦЕПТЫ ПРАЗДНИЧНОГО УЖИНА для двоих
festive_dinner = [
{ "r": "Жульен с курицей и шампиньонами в духовке ",
      "url":"https://www.iamcook.ru/showrecipe/5481"},
{ "r": " Салат «Цезарь» с креветками",
      "url":"https://www.iamcook.ru/showrecipe/3003"},
{ "r": "Фрикадельки с сыром в томатном соусе в духовке ",
      "url":"https://www.iamcook.ru/showrecipe/16032"},
{ "r": "Куриная грудка с помидорами в фольге ",
      "url":"https://www.iamcook.ru/showrecipe/13531"},
{ "r": " Куриная грудка «под шубой» в духовке",
      "url":"https://www.iamcook.ru/showrecipe/10974"},
{ "r": "Салат «Греческий» (классический) ",
      "url":"https://www.iamcook.ru/showrecipe/9692"},
{ "r": "Запечённая курица, фаршированная печенью ",
      "url":"https://www.russianfood.com/recipes/recipe.php?rid=168754"},
{ "r": " Гармошка из свинины, с куриным филе (в фольге)",
      "url":"https://www.russianfood.com/recipes/recipe.php?rid=168327"},
{ "r": " Курица, запечённая в пикантном мандариновом маринаде",
      "url":"https://www.russianfood.com/recipes/recipe.php?rid=170095"},
{ "r": "Запечённые помидоры, фаршированные курицей и рисом ",
      "url":"https://www.russianfood.com/recipes/recipe.php?rid=163287"},
{ "r": " Салат с рукколой, помидорами черри и мидиями",
      "url":"https://menunedeli.ru/recipe/salat-s-rukkoloj-pomidorami-cherri-i-midiyami/"},
{ "r": "Чизкейк: рецепт без выпечки с печеньем ",
      "url":"https://menunedeli.ru/recipe/chizkejk-recept-bez-vypechki-s-pechenem/"},
{ "r": "Ужин из рыбы и картофеля ",
      "url":"https://www.koolinar.ru/recipe/view/149353"},
{ "r": "Пангасиус с морковью, в духовке ",
      "url":"https://www.koolinar.ru/recipe/view/168202"},
{ "r": " Пангасиус с сыром и помидорами",
      "url":"https://www.koolinar.ru/recipe/view/93285"},
{ "r": "Паста а-ля карбонара ",
      "url":"https://www.koolinar.ru/recipe/view/91495"},
{ "r": " Весенний салат с молодой капустой и овощами",
      "url":"https://www.koolinar.ru/recipe/view/172842"},
{ "r": " Хрустящий весенний салат из молодой капусты с огурцом и редисом",
      "url":"https://www.koolinar.ru/recipe/view/172798"},
]

@bot.message_handler(commands=["for_two"])
def for_two(message):
    # Выбираем случайный словарь из списка
    sluchay_dinner_7 = random.choice(festive_dinner )

    # Получаем текст и ссылку из выбранного словаря
    recept_7 = sluchay_dinner_7["r"]
    url_7 = sluchay_dinner_7["url"]
    # Создаём переменную
    for_two_din = recept_7 + url_7
    print(for_two_din)

    bot.send_message(message.chat.id, "Приятного аппетита!\n" + for_two_din)

birthday_dinner = [
    { "r": "Куриная грудка с помидорами в фольге ",
          "url":"https://www.iamcook.ru/showrecipe/13531"},
    { "r": " Пангасиус с сыром и помидорами",
          "url":"https://www.koolinar.ru/recipe/view/93285"},
    { "r": " Курица, запечённая в пикантном мандариновом маринаде",
          "url":"https://www.russianfood.com/recipes/recipe.php?rid=170095"},
    { "r": " Гармошка из свинины, с куриным филе (в фольге)",
          "url":"https://www.russianfood.com/recipes/recipe.php?rid=168327"},
    { "r": " Куриная грудка «под шубой» в духовке",
          "url":"https://www.iamcook.ru/showrecipe/10974"},
    { "r": "Жульен с курицей и шампиньонами в духовке ",
          "url":"https://www.iamcook.ru/showrecipe/5481"},
]
@bot.message_handler(commands=["birthday"])
def birthday(message):
    # Выбираем случайный словарь из списка
    sluchay_dinner_3 = random.choice(birthday_dinner)

    # Получаем текст и ссылку из выбранного словаря
    recept_3 = sluchay_dinner_3["r"]
    url_3 = sluchay_dinner_3["url"]
    # Создаём переменную
    dinner_3 = recept_3 + url_3
    print(dinner_3)

    bot.send_message(message.chat.id, "Приятного аппетита!\n" + dinner_3)

bonus_dr = [
{ "r": "Медовик на сковороде",
      "url":"https://povar.ru/recipes/medovik_na_skovorode-22563.html"},
{ "r": " Торт 'Наполеон' за 30 минут",
      "url":"https://povar.ru/recipes/tort_napoleon_za_30_minut-78026.html"},
{ "r": " Торт 'Сникерс'",
      "url":"https://www.iamcook.ru/showrecipe/27812"},
{ "r": "ПРОСТОЙ ЧИЗКЕЙК БЕЗ ТВОРОГА С ПЕЧЕНЬЕМ ",
      "url":"https://1000.menu/cooking/6402-chizkeik-iz-smetani"},
{ "r": "ТОРТ С ТВОРОЖНЫМ СЫРОМ И СЛИВКАМИ ",
      "url":"https://1000.menu/cooking/24384-tort-s-tvorojnym-syrom"},
{ "r": "ЧЕРНИЧНЫЙ МУССОВЫЙ ТОРТ ",
      "url":"https://1000.menu/cooking/42715-chernichnyi-mussovyi-tort"},
]

@bot.message_handler(commands=["bonus"])
def bonus(message):
    # Выбираем случайный словарь из списка
    sluchay_dinner_4 = random.choice(bonus_dr)

    # Получаем текст и ссылку из выбранного словаря
    recept_4 = sluchay_dinner_4["r"]
    url_4 = sluchay_dinner_4["url"]
    # Создаём переменную
    bon_dr = recept_4 + url_4
    print(bon_dr)

    bot.send_message(message.chat.id, "Приятного аппетита!\n" + bon_dr)

buffet_dinner = [
    { "r": "Быстрые закуски в тарталетках",
          "url":"https://www.koolinar.ru/recipe/view/131445"},
    { "r": " Рулетики из баклажанов с сыром и чесноком, помидорами",
          "url":"https://www.koolinar.ru/recipe/view/159514"},
    { "r": " Брускетты",
          "url":"https://www.koolinar.ru/recipe/view/170591"},
    { "r": " Закусочные рулетики",
          "url":"https://www.koolinar.ru/recipe/view/165342"},
    { "r": "Простые закуски 5 рецептов | канапе ",
          "url":"https://www.koolinar.ru/recipe/view/155601"},
]

@bot.message_handler(commands=["buffet"])
def buffet(message):
    # Выбираем случайный словарь из списка
    sluchay_dinner_5 = random.choice(buffet_dinner)

    # Получаем текст и ссылку из выбранного словаря
    recept_5 = sluchay_dinner_5["r"]
    url_5 = sluchay_dinner_5["url"]
    # Создаём переменную
    buf_dinner = recept_5 + url_5
    print(buf_dinner)

    bot.send_message(message.chat.id, "Приятного аппетита!\n" + buf_dinner)

# СОЗДАЁМ КНОПКИ / главное МЕНЮ
@bot.message_handler(commands=['menu'])
def menu(message):
    start_markup = telebot.types.InlineKeyboardMarkup()

    # первый ряд (две кнопки)
    btn1 = types.InlineKeyboardButton('Лёгкий', callback_data='1')
    btn2 = types.InlineKeyboardButton('Быстрый', callback_data='2')
    start_markup.row(btn1, btn2)

    # второй ряд (одна кнопка)
    btn3 = types.InlineKeyboardButton('Праздничный', callback_data='3')
    btn4 = types.InlineKeyboardButton('ПП-ужин', callback_data='4')
    start_markup.row(btn3, btn4)

    bot.send_message(message.chat.id, 'Варианты ужинов', reply_markup=start_markup)

# СОЗДАЁМ КНОПКИ / МЕНЮ_2 праздничный ужин
@bot.message_handler(commands=['menu_2'])
def menu(message):
    start_markup = telebot.types.InlineKeyboardMarkup()

    # первый ряд (две кнопки)
    btn1_1 = types.InlineKeyboardButton("День рождение", callback_data='1_1')
    btn2_2 = types.InlineKeyboardButton('Фуршет', callback_data='2_2')
    start_markup.row(btn1_1, btn2_2)

    btn3_3 = types.InlineKeyboardButton('Ужин для двоих', callback_data='3_3')
    btn4_4 = types.InlineKeyboardButton('Возврат в главное меню', callback_data='4_4')
    start_markup.row(btn3_3, btn4_4)

    bot.send_message(message.chat.id, 'Выберите категорию', reply_markup=start_markup)


@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    if callback.data == '1':
        bot.send_message(callback.message.chat.id, 'Вы выбрали лёгкий ужин')
        bot.send_message(callback.message.chat.id, 'Рецепт дня /dinner')
    elif callback.data == '2':
        bot.send_message(callback.message.chat.id, 'Вы выбрали быстрый ужин')
        bot.send_message(callback.message.chat.id, 'Рецепт дня /dinner2')
    elif callback.data == '3':
        bot.send_message(callback.message.chat.id, 'Вы выбрали праздничный ужин')
        bot.send_message(callback.message.chat.id, 'Выбрать событие /menu_2')
    elif callback.data == '4':
        bot.send_message(callback.message.chat.id, 'Вы выбрали ПП-ужин')
        bot.send_message(callback.message.chat.id, 'Рецепт дня /pp_dinner')

    if callback.data == '1_1':
        bot.send_message(callback.message.chat.id, 'Поздравляем именинника!!!')
        bot.send_message(callback.message.chat.id, 'Вариант праздничного ужина /birthday')
        bot.send_message(callback.message.chat.id, 'Чтобы получить рецепт торта нажните /bonus')
    elif callback.data == '2_2':
        bot.send_message(callback.message.chat.id, 'Ваш выбор ФУРШЕТ')
        bot.send_message(callback.message.chat.id, 'Просмотреть вариант рецепта /buffet')
    elif callback.data == '3_3':
        bot.send_message(callback.message.chat.id, 'Отлично! У вас сегодня особенный вечер.')
        bot.send_message(callback.message.chat.id, 'Вариант ужина для двоих /for_two')
    elif callback.data == '4_4':
        bot.send_message(callback.message.chat.id, 'Спасибо за использование бота!')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item3 = types.KeyboardButton("/menu")
        markup.add(item3)
        bot.send_message(callback.message.chat.id, 'Выберите нужную категорию /menu', reply_markup=markup)


# Запускаем бота
bot.polling(none_stop=True, interval=0)

