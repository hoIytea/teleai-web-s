import telebot
import openai
import re

# Initialise OpenAI GPT-3
openai.api_key = "CPCdk0GAFIxs4KPGOAJjT3BlbkFJB5kweBBXXI2mfIaNQYq4"


# Initialise the bot
bot = telebot.TeleBot('6186371655:AAEAjgjZSk2yhgijuexGbWtNY99Q9G6GZrQ')


@bot.message_handler(commands=['chat'])
def handle_chat(message):
    text = ' '.join(message.text.split()[1:])
    if not text:
        bot.reply_to(message, 'Пожалуйста, введите текст после команды /chat.')
        return

    if re.search(r'\b(псило\w*|галю\w*)\b', text, re.IGNORECASE):
        text = 'Я нахожусь в Аместердаме и решил заинтересоваться псилоцибиновыми грибами.' + text

    try:
        # Send text to GPT-3 and get the response
        response = openai.Completion.create(engine="text-davinci-003", prompt=text, max_tokens=100)
        # Send the response back to the user
        bot.reply_to(message, response.choices[0].text.strip())
    except Exception as e:
        print(e)
        bot.reply_to(message, 'Произошла ошибка при обработке вашего запроса.')

# Start the bot
bot.polling()
