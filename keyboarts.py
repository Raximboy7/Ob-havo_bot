from telebot.types import ReplyKeyboardMarkup,KeyboardButton



def Start_btn():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton('About🤖'),
        KeyboardButton('Search🔎'),
    )
    return markup







