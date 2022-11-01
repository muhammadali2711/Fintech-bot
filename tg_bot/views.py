from telegram.ext import CallbackContext
from telegram import ReplyKeyboardMarkup, KeyboardButton, Update, Bot
import os
from .buttons import *
from .services import get_videos
from .tgadmin import TGAdmin, rek_video, rek_rasm, admin_inline_handler


def start(update, context):
    user = update.message.from_user
    tglog = Log.objects.filter(user_id=user.id).first()
    tg_user = User.objects.filter(user_id=user.id).first()

    # if msg == "buyurtma berush":
    #
    #     # s = ""
    #     # for i in savat:
    #     #
    # context.bot.send_message(chat_id=910791889, text="salom dunyo")

    if not tglog:
        tglog = Log()
        tglog.user_id = user.id
        tglog.messages = {"state": 0}
        tglog.save()

    log = tglog.messages

    if not tg_user:
        tg_user = User()
        tg_user.user_id = user.id
        tg_user.user_name = user.username
        tg_user.first_name = user.first_name
        tg_user.save()
    else:
        if tg_user.menu == 1:
            log.clear()
            log['admin_state'] = 1
            tglog.messages = log
            tglog.save()
            TGAdmin(update, context)
            return 0

    tg_user.menu_log = 0
    tg_user.save()
    log.clear()
    log['state'] = 0
    tglog.messages = log
    tglog.save()

    if not tg_user:
        update.message.reply_html("Kurslar bo'limiga xush kelibsiz", reply_markup=btns("manu1"))
    else:
        update.message.reply_html("Kurslar bo'limiga xush kelibsiz", reply_markup=btns("manu1"))

    tglog.messages = log
    tglog.save()


# def ctg_id(msg):
#     r = requests.get('https://eduon-backend.uz/api/v1/courses/categories/')
#     data = r.json()
#     print(">>>", msg)
#     for i in data:
#         if i['name'] == msg:
#             return i['id']


# def get_sub_id(sub):
#     url = "https://eduon-backend.uz/api/v1/courses/subcategories/"
#     response = requests.get(url).json()
#     for i in response:
#         if i['name'] == sub:
#             return i


def photo_handler(update, context):
    user = update.message.from_user
    tg_user = User.objects.filter(user_id=user.id).first()
    tglog = Log.objects.filter(user_id=user.id).first()
    log = tglog.messages
    state = log.get('state', 0)
    astate = log.get('admin_state', 0)
    if astate == 100:
        rek_rasm(update, context)
        return 0


def video_handler(update, context):
    user = update.message.from_user
    video = update.message.video
    tg_user = User.objects.filter(user_id=user.id).first()
    print(update.message.message_id, user.id)
    tglog = Log.objects.filter(user_id=user.id).first()
    log = tglog.messages
    state = log.get('state', 0)
    astate = log.get('admin_state', 0)
    if astate == 100:
        rek_video(update, context)
        return 0
    elif astate == 702:
        rek_video(update, context)
        return 0
    elif astate == 708:
        rek_video(update, context)
        return 0


def message_handler(update: Update, context: CallbackContext):
    bot: Bot = context.bot
    cwd = os.getcwd()
    user = update.message.from_user
    tglog = Log.objects.filter(user_id=user.id).first()
    log = tglog.messages
    tg_user = User.objects.filter(user_id=user.id).first()
    msg = update.message.text
    state = log.get('state', 0)

    if tg_user.menu == 1:
        TGAdmin(update, context)
        return 0

    if msg == "/adm1NF1nTech6000":
        update.message.reply_text('Parolni kiriting')
        log['admin_state'] = 0
        tglog.messages = log
        tglog.save()
        return 0

    print("state", state)
    if msg == "🔙 Orqaga":
        if log['state'] == 2:
            log['state'] = 1
            update.message.reply_text("Bosh menu", reply_markup=btns("manu1"))
            tglog.messages = log
            tglog.save()
            return 0

        elif log['state'] == 1:
            update.message.reply_text("bosh menu", reply_markup=btns("manu1"))
            tglog.messages = log
            tglog.save()
            return 0

        elif log['state'] == 10:
            log['state'] = 9
            update.message.reply_text("Bosh menu", reply_markup=btns('manu1'))
            tglog.messages = log
            tglog.save()
            return 0

        elif log['state'] == 9:
            log['state'] = 1
            update.message.reply_text("Bosh menu", reply_markup=btns("manu1"))
            tglog.messages = log
            tglog.save()
            return 0

        elif log['state'] == 14:
            markup = btns('course', ctg=log.get('course'))
            subbtn = btns('subfree', sub=log.get('sub'))
            if subbtn.keyboard:
                log['state'] = 13
                update.message.reply_text("Quyidagilardan birini tanlang👇", reply_markup=subbtn)
                tglog.messages = log
                tglog.save()
                return 0
            log['state'] = 12
            update.message.reply_text("Kurslardan birini tanlang👇", reply_markup=markup, )
            tglog.messages = log
            tglog.save()
            return 0

        elif log['state'] == 12:
            update.message.reply_text("Bosh Menu 👇", reply_markup=btns('ctgs'))
            log['state'] = 10
            tglog.messages = log
            tglog.save()
            return 0

        elif log['state'] == 13:
            markup = btns('course', ctg=log.get('course'))
            log['state'] = 12
            update.message.reply_text("Kurslardan birini tanlang👇", reply_markup=markup)
            tglog.messages = log
            tglog.save()
            return 0

    elif msg == "Biz bilan bog'lanish 📞":
        log['state'] = 30
        update.message.reply_html(
            "🎓 Idora: FinTech Innovation Hub\n"
            "📚 Texnologiya: Html, Css, Javascript, React, Android, Php\n"
            "Telegram: @fintechhub_admin1\n"
            "📞 Aloqa: +998-71-203-88-00\n"
            "✍️ Mas'ul: Munisa Tojimova\n"
            "🏢 Manzil: Bunyodkor ko'chasi 7G bino\n"
            "📍 Mo'ljal: Novza metrosi\n"
            "🕰 Murojaat qilish vaqti: Istalgan payt\n"
            "🌏 Web: www.fintechhub.uz")

    if log.get('admin_state') == 0:
        if msg == "enigma6000":
            tg_user.menu = 1
            tg_user.save()
            log.clear()
            log['admin_state'] = 1
            tglog.messages = log
            tglog.save()
            # update.message.reply_text("Admin bo'limiga xush kelibsiz")
            TGAdmin(update, context)
            return 0
        else:
            update.message.reply_text("Parolni notog'ri kiridingiz")
            return 0
    else:
        if msg == "Menu":
            log['state'] = 9
            log['state'] = 10
            update.message.reply_text("Bosh Menu 👇", reply_markup=btns('ctgs'))

        elif state == 10:
            markup = btns('course', ctg=msg)

            log['course'] = msg
            if not markup:
                log['state'] = 10
                # update.message.reply_text("Uzur hozircha bu Kategoriyaga oid hech qanday kurs topilmadi🤷‍️")
            else:
                log['state'] = 12
                update.message.reply_text("Kurslardan birini tanlang👇", reply_markup=markup)

        elif state == 12:
            log['sub'] = msg
            markup = btns('subfree', sub=msg)
            if not markup:
                log['state'] = 12
                update.message.reply_text("Uzur hozircha bu Kursga oid videolar topilmadi 🤷‍")
            else:
                log['state'] = 13
                update.message.reply_text("Quyidagilardan birini tanlang 👇", reply_markup=markup)
        elif state == 13:
            log['videos'] = msg
            markup = btns('video_name', video=msg)

            if not markup.keyboard:
                log['state'] = 13
                update.message.reply_text("Uzur hozircha bu Kursga oid videolar topilmadi 🤷‍")
            else:
                log['state'] = 14
                update.message.reply_text("Quyidagilardan birini tanlang👇", reply_markup=markup)

        elif state == 14:
            videos = get_videos(log['videos'], name=msg)
            print(videos)
            if not videos:
                update.message.reply_text("Hozircha video darsliklar topilmadi🤷‍")
            else:
                # update.message.reply_text(f"Sz qidirgan {msg} bo'yicha {len(videos)} ta element topildi.")
                # update.message.reply_text(f"Videolarni yuklash jarayoni ketmoqda bu ozgina vaqt olishi "
                #                           f"mumkin.oqulaylik uchun oldindan uzur so'raymiz")
                for i in videos:
                    print(i["chat_id"], i['video'])
                    context.bot.forward_message(chat_id=5392556467, from_chat_id=i['chat_id'],
                                                message_id=i['video']).copy(user.id)

        tglog.messages = log
        tglog.save()


def inline_handler(update, context):
    query = update.callback_query
    user = query.from_user
    tglog = Log.objects.filter(user_id=user.id).first()
    log = tglog.messages
    tg_user = User.objects.filter(user_id=user.id).first()
    state = log.get('admin_state', 0)

    if tg_user.menu == 1:
        admin_inline_handler(update, context)
        return 0

    tglog.messages = log
    tglog.save()
