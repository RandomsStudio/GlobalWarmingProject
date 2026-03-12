import random
import telebot

bot = telebot.TeleBot("Token")

facts_data = [
    {
        "fact": "За последние 100 лет средняя температура на Земле повысилась на 1°C",
        "pic": "pictures/temperature_rise.jpg"
    },
    {
        "fact": "Уровень Мирового океана поднимается на 3.3 мм каждый год",
        "pic": "pictures/sea_level.jpg"
    },
    {
        "fact": "Арктический лед тает со скоростью 13% за десятилетие",
        "pic": "pictures/arctic_ice.jpg"
    }
]

memes_data = [
    {
        "mem": "За последние 100 лет средняя температура на Земле повысилась на 1°C",
        "mempic": "pictures/temperature_rise.jpg"
    },
    {
        "mem": "Уровень Мирового океана поднимается на 3.3 мм каждый год",
        "mempic": "pictures/sea_level.jpg"
    },
    {
        "mem": "Арктический лед тает со скоростью 13% за десятилетие",
        "mempic": "pictures/arctic_ice.jpg"
    }
]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    with open('pictures/wildlife_mini.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)
    bot.reply_to(message, "Привет! Хочешь узнать полезные факты про глобальное потепление и понять почему оно опасно? Посмотреть рандомный факт - /fact , Посмотреть рандомный мем - /meme")

@bot.message_handler(commands=['fact'])
def send_fact(message):
    random_item = random.choice(facts_data)
    
    random_fact = random_item["fact"]
    random_pic = random_item["pic"]
    
    try:
        with open(random_pic, 'rb') as f:
            bot.send_photo(message.chat.id, f, caption=random_fact)
    except FileNotFoundError:
        bot.reply_to(message, f"Факт: {random_fact}\n(Извините, картинка временно недоступна)")
    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {e}")

@bot.message_handler(commands=['meme'])
def send_fact(message):
    random_item = random.choice(facts_data)
    
    random_meme = random_item["mem"]
    random_mempic = random_item["mempic"]
    
    try:
        with open(random_mempic, 'rb') as f:
            bot.send_photo(message.chat.id, f, caption=random_meme)
    except FileNotFoundError:
        bot.reply_to(message, f"{random_meme}\n(Извините, картинка временно недоступна)")
    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {e}")

bot.polling()
