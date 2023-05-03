import telebot
import psycopg2

bot = telebot.TeleBot('6010438229:AAHWAYila7ugkeCGwHK2JNkB8z6xuTbfv4k')

conn = psycopg2.connect(database="postgres",
                        user="postgres",
                        password="anel2004",
                        host="localhost",
                        port="5433")
cur = conn.cursor()
cur.execute("""
        CREATE TABLE IF NOT EXISTS telegram_bot(
            id SERIAL PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            phoneNumber VARCHAR(20) NOT NULL,
            chatid VARCHAR(255) NOT NULL
        );        
""")
conn.commit()
cur.close()
conn.close()


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    conn = psycopg2.connect(database="postgres",
                        user="postgres",
                        password="anel2004",
                        host="localhost",
                        port="5433")
    cur = conn.cursor()
    cur.execute("SELECT * FROM telegram_bot WHERE chatid=%s", (str(message.chat.id),))
    user = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    if user is not None:
        bot.reply_to(message, f"С возвращением, {user[1]}!")
    else:
        bot.reply_to(message, "Приветствую! Это мини чадо Анель. Давай я тебе помогу")
        bot.send_message(message.chat.id, "Но сначала тебя нужно зарегестрировать. Как тебя зовут?")
        bot.register_next_step_handler(message, user_name)

def user_name(message):
    global name, chat_id
    name = message.text.strip()
    chat_id = message.chat.id
    bot.send_message(message.chat.id, "Окей, теперь твой номер телефона плиз")
    bot.register_next_step_handler(message, phonenumber)

def phonenumber(message):
    number = message.text.strip()
    conn = psycopg2.connect(database = "postgres",
                            user = "postgres",
                            password = "anel2004", 
                            host = "localhost", 
                            port = "5433")
    cur = conn.cursor()
    cur.execute("INSERT INTO telegram_bot(username, phoneNumber, chatid) VALUES ('%s', '%s', '%s')" % (name, number, chat_id))
    conn.commit()
    cur.close()
    conn.close()
    bot.send_message(message.chat.id, "Вы успешно зарегестрированы!")


@bot.message_handler(commands = ['copywriting'])
def main(message):
    bot.send_message(message.chat.id ,'Вот нейронки, которые могли бы тебе помочь(сори, мне было лень писать их фичи):\nGPT-3\nNeuralWriter\nArticle Forge\nWritesonic\nCopy.ai\nArticoolo\nTextio\nQuill\nHugging FaceRytr\nShortlyAI\nJarvis.ai\nCopySmith\nAI-Writer\nContentBot')

@bot.message_handler(commands = ['media'])
def main(message):
    bot.send_message(message.chat.id ,'Вот нейронки, которые могли бы тебе помочь(сори, мне было лень писать их фичи):\nAdobeSensei\nPixelmator Pro\nSkylum Luminar AI\nVideoProc\nDaVinci Resolve\nPixelSquid\nMagisto\nCanva\nWondershare Fotophir\nClipDrop')

@bot.message_handler(commands = ['coding'])
def main(message):
    bot.send_message(message.chat.id ,'Вот нейронки, которые могли бы тебе помочь(сори, мне было лень писать их фичи):\nKite\nTabNine\nDeepCode\nCodota\nIntelliCode\nGitHub Copilot\nSourcery\nCodeGuru\nCodeAI\nCodeworks')

@bot.message_handler(commands = ['video'])
def main(message):
    bot.send_message(message.chat.id ,'Вот нейронки, которые могли бы тебе помочь(сори, мне было лень писать их фичи):\nMagisto\nAdobe Premiere Pro\nLumen5\nAnimoto\nFilmora\nFlexClip\nShotcut\nOpenShot\nFilmstock\nRocketium')

@bot.message_handler(commands = ['sound'])
def main(message):
    bot.send_message(message.chat.id ,'Вот нейронки, которые могли бы тебе помочь(сори, мне было лень писать их фичи):\nAuphonic\nAmper Music\nLANDR\nAudio Design Desk\nMelodrive\nEcrett Music\nSoundtrap\nHumOn\nJukedeck\nLyrical AI')


bot.polling(non_stop=True)