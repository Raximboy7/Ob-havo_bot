from telebot.types import Message
from config import KEY
from  loader import bot
from datetime import datetime
import requests

@bot.message_handler(func=lambda message:message.text == 'About🤖')
def reaction_about(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Salom men Ob-Havo malumotlarini ulashuvchi botman /Search tugmasini bosib, menga shahar nomini kriting!" )
@bot.message_handler(func=lambda message: message.text =='Search🔎')
def reaction_search(message: Message):
    chat_id = message.chat.id
    svg = bot.send_message(chat_id, "Shaxar nomini kriting!✍️" )
    bot.register_next_step_handler(svg, get_info_whater)

def get_info_whater(message:Message):
    chat_id = message.chat.id
    try:
        URL = 'https://api.openweathermap.org/data/2.5/weather'
        PATERNS = {
            'q': message.text,
            'appid': KEY
        }
        KELVIN = 273.5
        res = requests.get(URL, params=PATERNS).json()
        ob_havo = res['weather'][0]['main']
        temp = round(res['main']['temp'] - KELVIN)
        timezon = res['timezone']
        quyosh_ch = datetime.utcfromtimestamp(res['sys']['sunrise']+timezon).strftime('%H:%M:%S %D-%M-%Y')
        quyosh_b = datetime.utcfromtimestamp(res['sys']['sunset']+timezon).strftime('%H:%M:%S %D-%M-%Y')
        shamol = res['wind']['speed']
        bot.send_message(chat_id, f"""
Siz kritgan: 🏙{message.text.title()}
Ob-Havo: {ob_havo}🌤
Harorat: {temp}🌡
Quyosh_Ch: {quyosh_ch}🌅
Quyosh_B: {quyosh_b}🌅
Shamol: {shamol}💨""")
    except:
        bot.send_message(chat_id, 'Bunday shaharni topa olmadim!')