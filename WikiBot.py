from telebot import TeleBot

import wikipedia
wikipedia.set_lang("ru")

wiki_bot = TeleBot('7725311229:AAHgz3byp8yqezoJZ3RtNgLs1LSlrnoAF_A')

@wiki_bot.message_handler(commands=['wiki'])
def get_info(message):
    query = message.text.replace('/wiki', '').strip()
    try:
        summary = wikipedia.summary(query, sentences=2)
        wiki_bot.send_message(message.chat.id, summary)
    except Exception as e:
        wiki_bot.send_message(message.chat.id, 'Информация не найдена.')

wiki_bot.polling(none_stop=True)
