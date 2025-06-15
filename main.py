import telebot
import json
import random
token = "7711176374:AAG4lNhQBsLrAUlzGMyJozI2dsmugqt2OKs"
bot = telebot.TeleBot(token)
aa1 = True
file = open("ttr.json", "r", encoding="UTF-8")
all_words = json.load(file)
file.close()
def true(message):
    return True


@bot.message_handler(["start"])
def handle_start(message):
    print("privet")

@bot.message_handler(["help"])
def handle_help(message):
    bot.send_message(message.chat.id,"/new_word - добавит новое слово в словарь\n" + "/show_words - отобразит все слова пользователя\n" + "/show_word - отобразит перевод английского слова\n" + "/quiz - создаст викторину (указать кол-во слов)")
    print("help")
@bot.message_handler(["new_word"])
def handle_new_word(message):
    words = message.text.split(" ")
    if len(words) == 3:
        english = words[1]
        russian = words[2]
        if str(message.chat.id) in all_words:
            id_dict = all_words[str(message.chat.id)]
            id_dict[english] = russian
            print(message.chat.id)
        else:
            all_words[str(message.chat.id)] = {english: russian}  
        file = open("ttr.json", "w", encoding="UTF-8")
        json.dump(all_words,file,ensure_ascii=False,indent=4)
        file.close()
        bot.send_message(message.chat.id,"слово " + english + " добавлено!")
    else:
        bot.send_message(message.chat.id,"Неправильный ввод. Чтобы добавить слова напишите команду: /new_word [слово на англиском] [слово на русском]")
    print("new_word")
@bot.message_handler(["show_word"])
def handle_show_word(message):
    words = message.text.split(" ")
    if len(words) > 2:
        word = words[1]
        if str(message.chat.id) in all_words:
            id_dict = all_words[str(message.chat.id)]
            if word in id_dict:
                russian = id_dict[word]
                bot.send_message(message.chat.id,russian)
            else:    
                bot.send_message(message.chat.id,"Нет такого слова в словаре")
        else:
            bot.send_message(message.chat.id,"У вас ещё нет слов. Чтобы добавить слова напишите команду: /new_word [слово на англиском] [слово на русском]")
    else:
         bot.send_message(message.chat.id,"можно вводить только слова без пробелов")
    print("show_word")
def hello(message):
    bot.send_message(message.chat.id,"Привет " + message.text)


@bot.message_handler(["hello"])
def handle_show_word(message):
    bot.send_message(message.chat.id,"скажите своё имя")
    
    print("name")
    bot.register_next_step_handler_by_chat_id(message.chat.id,hello)
    






@bot.message_handler(["show_words"])
def handle_show_words(message):
    if str(message.chat.id) in all_words:
        user_words = all_words[str(message.chat.id)]
        for i in user_words:
            bot.send_message(message.chat.id,i + " - " + user_words[i])
    else:
        bot.send_message(message.chat.id,"У вас ещё нет слов. Чтобы добавить слова напишите команду: /new_word [слово на англиском] [слово на русском]")
    print("show_Words")


def id_words(id):
    words = []
    user_words = all_words[str(id)]
    if str(id) in all_words:
        for i in user_words:
            words.append(i)
    return words

def checker(message,rus_word,number,false,true):
    
    
    if rus_word.lower() == message.text.lower():
        bot.send_message(message.chat.id,"Верно!!!")
        true += 1
    else:
        bot.send_message(message.chat.id,"НЕТ!!! " + "Верное слово- " + rus_word)
        false += 1
    if number > 0:
        user_words = all_words[str(message.chat.id)]
        eng_words = id_words(message.chat.id)
        rand_word  = eng_words[random.randint(0,len(eng_words) - 1)]
        rus_word = user_words[rand_word]
        bot.send_message(message.chat.id,"переведи данное слово на русский язык: " + rand_word)
        bot.register_next_step_handler_by_chat_id(message.chat.id,checker,rus_word,number - 1,false, true)
    else:
         bot.send_message(message.chat.id,"Конец... " + "верно: " + str(true) + " неверно: " + str(false))
        


@bot.message_handler(["quiz"])
def handle_quiz(message):
    true = 0
    false = 0
    words = message.text.split(" ")
    if len(words) == 2:
        number = int(words[1])
        user_words = all_words[str(message.chat.id)]
        eng_words = id_words(message.chat.id)
        rand_word  = eng_words[random.randint(0,len(eng_words) - 1)]
        rus_word = user_words[rand_word]
        bot.send_message(message.chat.id,"переведи данное слово на русский язык: " + rand_word)
        bot.register_next_step_handler_by_chat_id(message.chat.id,checker,rus_word,number - 1,false,true)
    else:
        bot.send_message(message.chat.id,"Вы не указали количество слов!")
    print("quiz")




@bot.message_handler(func=true)
def handle_no_command(message):
    if message.text == "Привет":
        bot.send_message(message.chat.id,"Здарова")
    elif message.text == "Пока":
        bot.send_message(message.chat.id,"Пака")
    else:
        bot.send_message(message.chat.id,"Нет такой команды")


    








#-----------------------------------------------
bot.polling()