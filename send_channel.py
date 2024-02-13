import traceback
from src.api_telegram import TelegramBot
import datetime
import pytz

TOKEN = '6654901607:AAEZcO2UTa0HNMP13pV7XCmYNf8LTkRAEA4'
MYID = '-1002088400640'
bot = TelegramBot(TOKEN, MYID)

now = datetime.datetime.now(pytz.timezone("Asia/Ho_Chi_Minh")).strftime('%Y-%m-%d %H:%M:%S')


# Run this
def send_notif_checkin():
    try:
        mess = "Hey Jace bây giờ là " + str(now) + \
               "\nCheck in đi nào không là ăn đòn vs a Thanh đó"

        bot.send_message(mess)
    # If error occurs, send the error with its trace
    except Exception as e:
        print(traceback.format_exc())
        bot.send_error_message(traceback.format_exc())


def send_notif_checkout():
    try:
        mess = "Hey Jace bây giờ là " + str(now) + \
               "\nCheck out đi nào không là ăn đòn vs a Thanh đó"

        bot.send_message(mess)
    # If error occurs, send the error with its trace
    except Exception as e:
        print(traceback.format_exc())
        bot.send_error_message(traceback.format_exc())