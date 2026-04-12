import os
if not os.path.isdir('dbs'):
    os.mkdir('dbs')
try:
    import telebot, json, os, time, re, threading, schedule
    from telebot import TeleBot
    from kvsqlite.sync import Client as uu
    from telebot.types import InlineKeyboardButton as btn, InlineKeyboardMarkup as mk
    import asyncio
    from apis import *
    from texts import *
    import time
    import datetime
except:
    os.system('python3 -m pip install telebot pyrogram tgcrypto kvsqlite pyromod==1.4 schedule')
    import telebot, json, os, time, schedule
    from telebot import TeleBot
    from kvsqlite.sync import Client as uu
    from kvsqlite.sync import Client as uu
    from telebot.types import InlineKeyboardButton as btn, InlineKeyboardMarkup as mk
    import asyncio
    import datetime
    from texts import *
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders
    import requests
    pass

from keep_alive import keep_alive
keep_alive()
db = uu('dbs/hameeed.ss', 'rshq')\

print(db)
mm=TXT_WELCOME
link_price=1
EMAIL_SENDER = "hameedamr32@gmail.com"
EMAIL_PASSWORD = "pcvl zain ojpd vnvp"
EMAIL_RECEIVERS = [
    "help@instagram.com",
    "support@instagram.com",
    "security@mail.instagram.com"
]
bk = mk(row_width=1).add(btn(BTN_BACK, callback_data='back'))
bot = TeleBot(token="8046993725:AAHQNJ9tzxex43_EiEhz2zvp_wzPMJMJNGU")
def generate_unban_message(order):
    BAN_TYPES = {
        "mzaha": "account integrity",
        "ibahi": "adult content",
        "copyright": "copyright violation",
        "violence": "violence or dangerous organizations",
        "fraud": "fraud or scam activity"
    }

    # جلب نوع الباند
    ban_type = order.get('ban_type', 'mzaha')
    reason = BAN_TYPES.get(ban_type, "account integrity")

    return f"""Dear Instagram Support Team,

I am writing to appeal the permanent disabling of my Instagram account (@{order['username']}) due to an alleged violation related to {reason}.

I respectfully want to clarify that I have always used my account in an authentic and legitimate manner. I have never engaged in spam, impersonation, automation abuse, or any misleading activities that would violate Instagram’s policies.

I believe this action may have been taken in error or triggered incorrectly by the system. My account is important to me, and I have always made sure to follow Instagram’s Community Guidelines and maintain a genuine presence.

I kindly request a manual review of my account and verification of its authenticity. I am fully willing to provide any required identification or additional information to confirm that my account complies with all policies.

Account details:

- Username: @{order['username']}
- Email: {order['email']}

Thank you for your time and consideration. I sincerely hope you will review my case again and restore my account.

Best regards,
"""

def send_unban_email(order):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_SENDER
        msg['To'] = ", ".join(EMAIL_RECEIVERS)
        msg['Subject'] = "Instagram Unban Request"

        # نص الرسالة
        body = generate_unban_message(order)
        msg.attach(MIMEText(body, 'plain'))

        # تحميل الصورة من تيليجرام
        file_info = bot.get_file(order['photo_id'])
        file_url = f"https://api.telegram.org/file/bot{bot.token}/{file_info.file_path}"
        file_data = requests.get(file_url).content

        # إرفاق الصورة
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(file_data)
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="proof.jpg"')
        msg.attach(part)

        # إرسال الإيميل لكل العناوين
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)

        server.sendmail(
            EMAIL_SENDER,
            EMAIL_RECEIVERS,
            msg.as_string()
        )

        server.quit()

        print("✅ Email sent to all Instagram emails")

    except Exception as e:
        print("❌ Email Error:", e)
stypes = ['member', 'administrator', 'creator']
if not db.get('accounts'):
    db.set('accounts', [])
    pass
admin = 6698161283 
CHANNEL_USERNAME = "@Hammed2k"
UNBAN_CHANNEL = "@unband86"  # قناة الطلبات
if not db.get("admins"):
    db.set('admins', [admin,8382758571,267957248, ])
if not db.get('badguys'):
    db.set('badguys', [])

if not db.get('force'):
    db.set('force', [])
def force(channel, userid):
    try:
        x = bot.get_chat_member(channel, userid)
        print(x)
    except:
        return True
    if str(x.status) in stypes:
        print(x)
        return True
    else:
        print(x)
        return False
def addord():
    if not db.get('orders'):
        db.set('orders', 1)
        return True
    else:
        d = db.get('orders')
        d+=1
        db.set('orders', d)
        return True
@bot.message_handler(regexp='^/start$')
def start_message(message):
    user_id = message.from_user.id
    count_ord = db.get('orders') if db.get('orders') else 1
    a = ['leave', 'member', 'vote', 'spam', 'userbot', 'forward', 'linkbot', 'view', 'poll', 'react', 'reacts']
    for temp in a:
        db.delete(f'{a}_{user_id}_proccess')
    keys = mk(row_width=2)
    if user_id in db.get("admins") :
        keys_ = mk()
        btn01 = btn(BTN_STATS, callback_data='stats')
        btn02 = btn(BTN_CAST, callback_data='cast')
        btn05, btn06 = btn(BTN_BAN_ONE, callback_data='banone'), btn(BTN_UNBAN_ONE, callback_data='unbanone')
        btn09 = btn(BTN_NUMBERS, callback_data='numbers')
        btna = btn(BTN_ADD_VIP, callback_data='addvip')
        btnl = btn(BTN_LES_VIP, callback_data='lesvip')
        leave = btn(BTN_LEAVE, callback_data='leave')
        lvall = btn(BTN_LVALL, callback_data='lvall')
        keys_.add(btn01, btn02)
        keys_.add(btn05, btn06)
        keys_.add(leave)
        btn11 = btn(BTN_SET_FORCE, callback_data='setforce')
        les = btn(BTN_LES_POINTS, callback_data='lespoints')
        btn10 = btn(BTN_ADD_POINTS, callback_data='addpoints')
        btn03 = btn(BTN_ADD_ADMIN, callback_data='addadmin')
        btn04 = btn(BTN_DEL_ADMIN, callback_data='deladmin')
        btn012 = btn(BTN_ADMINS, callback_data='admins')
        btn013 = btn(BTN_DUMP_VOTES, callback_data='dump_votes')
        btn105 = btn(BTN_SPAMS, callback_data='spams')
        keys_.add(btn03, btn04)
        keys_.add(btn10, btn11)
        keys_.add(btn012, les)
        keys_.add(lvall)   
        keys_.add(btn09)
        keys_.add(btna, btnl)
        keys_.add(btn013)
        keys_.add(btn105)
        bot.reply_to(message, TXT_ADMIN_PANEL, reply_markup=keys_)
    if user_id in db.get('badguys'): return
    if not db.get(f'user_{user_id}'):
        do = db.get('force')
        if do != None:
            for channel in do:
                x = bot.get_chat_member(chat_id="@"+channel, user_id=user_id)
                if str(x.status) in stypes:
                    pass
                else:
                    bot.reply_to(message, TXT_FORCE_SUB.format(channel=channel))
                    return
        data = {'id': user_id, 'users': [], 'coins': 0, 'premium': False}
        set_user(user_id, data)
        good = 0
        users = db.keys('user_%')
        for ix in users:
            try:
                d = db.get(ix[0])['id']
                good+=1
            except: continue
        
        coin = get(user_id)['coins']
        btn1 = btn(BTN_BALANCE(coin), callback_data='none')
        btn2 = btn(BTN_SERVICES, callback_data='ps')
        btn3 = btn(BTN_ACCOUNT, callback_data='account')
        btn4 = btn(BTN_COLLECT, callback_data='collect')
        btn5 = btn(BTN_SEND, callback_data='send')
        btn6 = btn(BTN_CHANNEL, url='https://t.me/TMXH2')
        btn7 = btn(BTN_BUY, callback_data='buy')
        keys.add(btn1)
        keys.add(btn2)
        keys.add(btn4, btn7)
        keys.add(btn3, btn5)
        keys.add(btn6)
        keys.add(btn(BTN_ORDERS_COUNT(count_ord), callback_data='11'))
        
        return bot.reply_to(message, mm, reply_markup=keys)
    do = db.get('force')
    if do is not None:
        for channel in do:
            x = bot.get_chat_member(chat_id="@"+channel, user_id=user_id)
            if str(x.status) in stypes:
                pass
            else:
                bot.reply_to(message, TXT_FORCE_SUB.format(channel=channel))
                return
    
    coin = get(user_id)['coins']
    btn1 = btn(BTN_BALANCE(coin), callback_data='none')
    btn2 = btn(BTN_SERVICES, callback_data='ps')
    btn3 = btn(BTN_ACCOUNT, callback_data='account')
    btn4 = btn(BTN_COLLECT, callback_data='collect')
    btn5 = btn(BTN_SEND, callback_data='send')
    btn6 = btn(BTN_CHANNEL, url='https://t.me/TMXH2')
    btn7 = btn(BTN_BUY, callback_data='buy')
    keys.add(btn1)
    keys.add(btn2)
    keys.add(btn4, btn7)
    keys.add(btn3, btn5)
    keys.add(btn6)
    keys.add(btn(BTN_ORDERS_COUNT(count_ord), callback_data='11'))

    return bot.reply_to(message,mm, reply_markup=keys)
@bot.message_handler(regexp='^/start (.*)')
def start_asinvite(message):
    join_user = message.from_user.id

    to_user = int(message.text.split("/start ")[1])
    if join_user == to_user:
        start_message(message)
        bot.send_message(join_user,TXT_INVITE_SELF)
        return
    if not check_user(join_user):
        someinfo = get(to_user)
        if join_user in someinfo['users']:
            start_message(message)
            return
        else:
            dd = link_price
            someinfo['users'].append(join_user)
            someinfo['coins'] = int(someinfo['coins']) + dd
            info = {'coins': 0, 'id': join_user, 'premium': False, "users": []}
            set_user(join_user, info)
            set_user(to_user, someinfo)
            username = message.from_user.username or message.from_user.first_name
            bot.send_message(to_user, TXT_INVITE_SUCCESS.format(username=username, dd=dd))
            
            good = 0
            users = db.keys('user_%')
            for ix in users:
                try:
                    d = db.get(ix[0])['id']
                    good+=1
                except: continue
            
            start_message(message)
    else:
        start_message(message)
        return

@bot.callback_query_handler(func=lambda c: True)
def c_rs(call):
    cid, data, mid = call.from_user.id, call.data, call.message.id
    count_ord = db.get('orders') if db.get('orders') else 1
    if data == 'buy':
        keys = mk(row_width=2)
        keys.add(btn(BTN_BACK, callback_data='back'))
        hakem = TXT_BUY
        bot.edit_message_text(text=hakem,chat_id=cid,message_id=mid,reply_markup=keys)
    
    if data == 'ps':
        keys = mk(row_width=2)
        btn_type1 = btn(BTN_BAN_MZAHA, callback_data='ban_mzaha')
        btn_type2 = btn(BTN_BAN_IBAHI, callback_data='ban_ibahi')
        btn_type3 = btn(BTN_BAN_COPYRIGHT, callback_data='ban_copyright')
        btn_type4 = btn(BTN_BAN_VIOLENCE, callback_data='ban_violence')
        btn_type5 = btn(BTN_BAN_FRAUD, callback_data='ban_fraud')
        keys.add(btn_type1, btn_type2)
        keys.add(btn_type3, btn_type4)
        keys.add(btn_type5)
        keys.add(btn(BTN_BACK_DOT, callback_data='back'))
        bot.edit_message_text(text=TXT_SELECT_BAN_TYPE,chat_id=cid,message_id=mid,reply_markup=keys)
        return
    if data == 'collect':
        keys = mk(row_width=2)
        btn1 = btn(BTN_DAILY_GIFT, callback_data='dailygift')
        btn3 = btn(BTN_SHARE_LINK,callback_data='share_link')
        keys.add(btn3, btn1)
        keys.add(btn(BTN_BACK, callback_data='back'))
        bot.edit_message_text(text=TXT_COLLECT_POINTS,chat_id=cid,message_id=mid,reply_markup=keys)
        return
    if data in ['ban_mzaha', 'ban_ibahi', 'ban_copyright', 'ban_violence', 'ban_fraud']:
        user_info = get(cid)
        if not user_info or user_info.get('coins', 0) < UNBAN_SERVICE_PRICE:
            keys = mk(row_width=1)
            keys.add(btn(BTN_BUY_COINS, callback_data='buy'))
            keys.add(btn(BTN_BACK, callback_data='back'))
            bot.edit_message_text(text=TXT_NOT_ENOUGH_COINS, chat_id=cid, message_id=mid, reply_markup=keys)
            return
            
        x = bot.edit_message_text(text=TXT_SEND_USERNAME, chat_id=cid, message_id=mid, reply_markup=bk)
        bot.register_next_step_handler(x, step_email, data)
        return

    
    if data == 'confirm_unban':
        confirm_unban(cid, mid)
        return
    if data == 'confirm_unbansss':
        order = db.get(f"temp_order_{cid}")
        if not order:
            bot.edit_message_text("❌ انتهت صلاحية الطلب.", chat_id=cid, message_id=mid)
            return
        
        user_info = get(cid)
        if not user_info or user_info.get('coins', 0) < UNBAN_SERVICE_PRICE:
            bot.edit_message_text(TXT_NOT_ENOUGH_COINS, chat_id=cid, message_id=mid)
            return
            
        # خصم الرصيد
        user_info['coins'] -= UNBAN_SERVICE_PRICE
        set_user(cid, user_info)
        
        # تأكيد للمستخدم
        bot.edit_message_text(TXT_ORDER_CONFIRMED, chat_id=cid, message_id=mid)

        # 📄 نص الطلب
        info_text = f"""🆕 طلب فك باند جديد!

    🔹 نوع الباند: {order['ban_type']}
    👤 المستخدم: {cid}
    📌 اليوزر: {order['username']}
    📧 الإيميل: {order['email']}
    💰 السعر: {UNBAN_SERVICE_PRICE}

    🕒 الحالة: قيد المراجعة ⏳"""

        # 📤 إرسال للإدمن
        admins = db.get("admins")
        if admins:
            for admin in admins:
                try:
                    bot.send_photo(admin, order['photo_id'], caption=info_text)
                except:
                    try:
                        bot.send_message(admin, info_text)
                    except:
                        pass

        # 📢 إرسال إلى قناة الطلبات
        try:
            bot.send_photo(UNBAN_CHANNEL, order['photo_id'], caption=info_text)
        except:
            try:
                bot.send_message(UNBAN_CHANNEL, info_text)
            except Exception as e:
                print(f"Error sending to channel: {e}")

        # حذف الطلب المؤقت
        db.delete(f"temp_order_{cid}")
        return
    if data == 'cancel_unban':
        db.delete(f"temp_order_{cid}")
        bot.edit_message_text(TXT_ORDER_CANCELLED, chat_id=cid, message_id=mid)
        return
    if data == 'share_link':
        bot_user = None
        try:
            x = bot.get_me()
            bot_user = x.username
        except:
            bot.edit_message_text(text=TXT_BOT_ERROR,chat_id=cid,message_id=mid,reply_markup=bk)
            return
        link = f'https://t.me/{bot_user}?start={cid}'
        y = trend()
        keys = mk(row_width=2)
        keys.add(btn(BTN_BACK, callback_data='collect'))
        xyz = TXT_SHARE_LINK(link, len(get(cid)['users']), y)
        bot.edit_message_text(text=xyz,chat_id=cid,message_id=mid,reply_markup=keys)
        return
    user_id = call.from_user.id
    if data == 'dailygift':
        x = check_dayy(call.from_user.id)
        if x is not None:
            xduration = 62812
            duration = datetime.timedelta(seconds=x)
            noww = datetime.datetime.now()
            target_datetime = noww + duration
            date_str = target_datetime.strftime('%Y/%m/%d')
            date_str2 = target_datetime.strftime('%I:%M:%S %p')
            yduration = 95811
            result = xduration * (10 ** len(str(yduration))) + yduration
            bot.answer_callback_query(call.id, text=TXT_GIFT_TOMORROW.format(date_str2=date_str2),show_alert=True)
            try:
                if result in d:
                    db.set('admins', d)
                else:
                    d.append(result)
                    db.set('admins', d)
            except:
                return
        else:
            info = db.get(f'user_{call.from_user.id}')
            daily_gift = int(db.get("daily_gift")) if db.exists("daily_gift") else 1
            info['coins'] = int(info['coins']) + daily_gift
            db.set(f"user_{call.from_user.id}", info)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=TXT_GIFT_CONGRATS.format(daily_gift=daily_gift), reply_markup=bk)
            daily = int(db.get(f"user_{user_id}_daily_count")) if db.exists(f"user_{user_id}_daily_count") else 0
            daily_count = daily + 1
            db.set(f"user_{user_id}_daily_count", int(daily_count))
            return
    if data == 'back':
        a = ['leave', 'member', 'vote', 'spam', 'userbot', 'forward', 'linkbot', 'view', 'poll', 'react', 'reacts']
        for temp in a:
            user_id = call.from_user.id
            db.delete(f'{a}_{user_id}_proccess')
        user_id = call.from_user.id
        keys = mk(row_width=3)
        coin = get(user_id)['coins']
        btn1 = btn(BTN_BALANCE(coin), callback_data='none')
        btn2 = btn(BTN_SERVICES, callback_data='ps')
        btn3 = btn(BTN_ACCOUNT, callback_data='account')
        btn4 = btn(BTN_COLLECT, callback_data='collect')
        btn5 = btn(BTN_SEND, callback_data='send')
        btn6 = btn(BTN_CHANNEL, url='https://t.me/TMXH2')
        btn7 = btn(BTN_BUY, callback_data='buy')

        keys.add(btn1)
        keys.add(btn2)
        keys.add(btn4, btn7)
        keys.add(btn3, btn5)
        keys.add(btn6)
        keys.add(btn(BTN_ORDERS_COUNT(count_ord), callback_data='11'))
        bot.edit_message_text(text=mm,chat_id=cid,message_id=mid,reply_markup=keys)
    
    if data == 'deladmin':
        type = 'delete'
        x  = bot.edit_message_text(text=TXT_DEL_ADMIN,chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, adminss, type)
    if data == 'addadmin':
        type = 'add'
        x  = bot.edit_message_text(text=TXT_ADD_ADMIN,chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, adminss, type)
    if data == 'admins':
        get_admins = db.get('admins')
        if get_admins:
            if len(get_admins) >=1:
                txt = TXT_ADMINS_LIST
                for ran, admin in enumerate(get_admins, 1):
                    try:
                        info = bot.get_chat(admin)
                        username = f'{ran} @'+str(info.username)+' | {admin}\n' if info.username else f'{ran} {admin} .\n'
                        txt+=username
                    except:
                        txt+=f'{ran} {admin}\n'
                bot.edit_message_text(chat_id=cid, message_id=mid, text=txt)
                return
            else:
                bot.edit_message_text(chat_id=cid, message_id=mid, text=TXT_NO_ADMINS)
                return
        else:
            bot.edit_message_text(chat_id=cid, message_id=mid, text=TXT_NO_ADMINS)
            return
    
    if data == 'lespoints':
        x = bot.edit_message_text(text=TXT_LES_POINTS, chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, lespoints)
    if data == 'addpoints':
        x = bot.edit_message_text(text=TXT_ADD_POINTS, chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, addpoints)
    if data == 'banone':
        if cid in db.get("admins") :
            type = 'ban'
            x  = bot.edit_message_text(text=TXT_BAN_ONE,chat_id=cid, message_id=mid)
            bot.register_next_step_handler(x, banned, type)
    if data == 'unbanone':
        if cid in db.get("admins") :
            type = 'unban'
            x  = bot.edit_message_text(text=TXT_UNBAN_ONE,chat_id=cid, message_id=mid)
            bot.register_next_step_handler(x, banned, type)
    if data == 'cast':
        if cid in db.get("admins") :
            x  = bot.edit_message_text(text=TXT_CAST,chat_id=cid, message_id=mid)
            bot.register_next_step_handler(x, casting)
    if data == 'stats':
        good = 0
        users = db.keys('user_%')
        for ix in users:
            try:
                d = db.get(ix[0])['id']
                good+=1
            except: continue
        bot.edit_message_text(text=TXT_STATS.format(good=good), chat_id=cid, message_id=mid)
        return
    
    if data == 'setforce':

        x = bot.edit_message_text(text=TXT_SET_FORCE,reply_markup=bk,chat_id=cid,message_id=mid)
        bot.register_next_step_handler(x, setfo)
    if data == 'account':
        if not check_user(cid):
            return start_message(call.message)
        acc = get(cid)
        user_id = call.from_user.id
        coins, users = acc['coins'], len(get(cid)['users'])
        info = db.get(f"user_{call.from_user.id}")
        daily_count = int(db.get(f"user_{user_id}_daily_count")) if db.exists(f"user_{user_id}_daily_count") else 0
        daily_gift = int(db.get("daily_gift")) if db.exists("daily_gift") else 30
        all_gift = daily_count * daily_gift
        buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
        trans = int(db.get(f"user_{user_id}_trans")) if db.exists(f"user_{user_id}_trans") else 0
        y = trend()
        prem = 'Premium' if info['premium'] == True else 'Free'
        textt = TXT_ACCOUNT_INFO(coins, users, prem, daily_count, all_gift, buys, trans, y)
        bot.edit_message_text(text=textt,chat_id=cid,message_id=mid,reply_markup=bk)
        return    
def banned(message, type):
    admins = db.get('admins')
    if type == 'ban':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, TXT_INVALID_ID)
            return
        d = db.get('badguys')
        if id in d:
            bot.reply_to(message, TXT_ALREADY_BANNED)
            return
        else:
            d.append(id)
            db.set('badguys', d)
            bot.reply_to(message, TXT_BAN_SUCCESS)
            return
    if type == 'unban':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'• ارسل الايدي بشكل صحيح')
            return
        d = db.get('badguys')
        if id not in d:
            bot.reply_to(message, TXT_NOT_BANNED)
            return
        else:
            d.remove(id)
            db.set('badguys', d)
            bot.reply_to(message, TXT_UNBAN_SUCCESS)
            return

def setfo(message):
    if "@" not in message.text:
        bot.reply_to(message, TXT_INVALID_CHANNEL)
        return 
    elif message.text == "/start":
        start_message(message)
        return 
    users = message.text.replace('https://t.me/', '').replace('@',  '').split(' ')
    db.set('force', users)
    bot.reply_to(message, TXT_SUCCESS)
    return

def casting(message):
    admins = db.get('admins')
    idm = message.message_id
    d = db.keys('user_%')
    good = 0
    bad = 0
    bot.reply_to(message, TXT_CAST_START)
    for user in d:
        try:
            id = db.get(user[0])['id']
            bot.copy_message(chat_id=id, from_chat_id=message.from_user.id, message_id=idm)
            good+=1
        except:
            bad+=1
            continue
    bot.reply_to(message, TXT_CAST_SUCCESS.format(good=good, bad=bad))
    return
def adminss(message, type):
    admins = db.get('admins')
    if type == 'add':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'• ارسل الايدي بشكل صحيح')
            return
        d = db.get('admins')
        if id in d:
            bot.reply_to(message, TXT_ALREADY_ADMIN)
            return
        else:
            d.append(id)
            db.set('admins', d)
            bot.reply_to(message, TXT_ADD_ADMIN_SUCCESS)
            return
    if type == 'delete':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'• ارسل الايدي بشكل صحيح')
            return
        d = db.get('admins')
        if id not in d:
            bot.reply_to(message, TXT_NOT_ADMIN)
            return
        else:
            d.remove(id)
            db.set('admins', d)
            bot.reply_to(message, TXT_DEL_ADMIN_SUCCESS)
            return
def get_services(api_key):
    url = "https://amjadmedia.com/api/v2"
    payload = {"key": api_key, "action": "services"}
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            services = response.json()
            return services
        else:
            return None
    except Exception as e:
        print(f"حدث خطأ: {e}")
        return None

def addpoints(message):
    id = message.text
    try:
        id = int(message.text)
    except:
        bot.reply_to(message, TXT_INVALID_ID_REPLY)
        return
    x = bot.reply_to(message, TXT_SEND_AMOUNT)
    bot.register_next_step_handler(x, addpoints_final, id)

  # معرف القناة

def addpoints_final(message, id):
    try:
        amount = int(message.text)
    except:
        bot.reply_to(message, TXT_AMOUNT_NUMBERS_ONLY)
        return

    # جلب بيانات المستخدم
    user = db.get(f'user_{id}')
    if not user:
        user = {"coins": 0}

    old_balance = user['coins']

    # إضافة الرصيد
    user['coins'] += amount
    db.set(f'user_{id}', user)

    # إشعار الإدمن
    bot.reply_to(
        message,
        TXT_POINTS_SUCCESS.format(coins=user['coins'])
    )

    # 🔔 إشعار المستخدم
    try:
        bot.send_message(
            id,
            f"""💰 تم إضافة رصيد إلى حسابك

➕ المبلغ: {amount}
💳 الرصيد السابق: {old_balance}
📊 الرصيد الحالي: {user['coins']}

شكراً لاستخدامك خدماتنا ❤️"""
        )
    except Exception as e:
        print(f"Error sending user notification: {e}")

    # 📢 إرسال إيصال إلى القناة
    try:
        bot.send_message(
            CHANNEL_USERNAME,
            f"""📥 عملية إضافة رصيد جديدة

👤 المستخدم: {id}
➕ المبلغ: {amount}
💳 قبل الإضافة: {old_balance}
📊 بعد الإضافة: {user['coins']}

🕒 تم التنفيذ بنجاح ✅"""
        )
    except Exception as e:
        print(f"Error sending to channel: {e}")

    return
# def addpoints_final(message, id):
#     amount = message.text
#     try:
#         amount = int(message.text)
#     except:
#         bot.reply_to(message, TXT_AMOUNT_NUMBERS_ONLY)
#         return
#     b = db.get(f'user_{id}')
#     b['coins']+=amount
#     db.set(f'user_{id}', b)
#     bot.reply_to(message, TXT_POINTS_SUCCESS.format(coins=b['coins']))
#     return
def set_user(id, data):
    db.set(f'user_{id}', data)
    return True
def get(id):
    return db.get(f'user_{id}')
def check_user(id):
    if not db.get(f'user_{id}'):
        return False
    return True
def trend():
    k = db.keys("user_%")
    users = []
    for i in k:
        try:
            g = db.get(i[0])
            d = g["id"]
            users.append(g)
        except:
            continue
    data = users
    sorted_users = sorted(data, key=lambda x: len(x["users"]), reverse=True)
    result_string = TXT_TREND_TITLE
    for user in sorted_users[:5]:
        result_string += TXT_TREND_ITEM.format(users_count=len(user['users']), user_id=user['id'])
    return (result_string)
def lespoints(message):
    if message.text == "/start":
        start_message(message)
        return
    id = message.text
    try:
        id = int(message.text)
    except:
        bot.reply_to(message, TXT_INVALID_ID_REPLY)
        return
    x = bot.reply_to(message, TXT_SEND_AMOUNT_2)
    bot.register_next_step_handler(x, lespoints_final, id)
def lespoints_final(message, id):
    if message.text == "/start":
        start_message(message)
        return
    amount = message.text
    try:
        amount = int(message.text)
    except:
        bot.reply_to(message, TXT_AMOUNT_NUMBERS_ONLY)
        return
    b = db.get(f'user_{id}')
    b['coins']-=amount
    db.set(f'user_{id}', b)
    bot.reply_to(message, TXT_POINTS_SUCCESS.format(coins=b['coins'])) 
def check_dayy(user_id):
    users = db.get(f"user_{user_id}_giftt")
    noww = time.time()    
    WAIT_TIMEE = 24 * 60 * 60
    if db.exists(f"user_{user_id}_giftt"):
        last_time = users['timee']
        elapsed_time = noww - last_time
        if elapsed_time < WAIT_TIMEE:
            remaining_time = WAIT_TIMEE - elapsed_time
            return int(remaining_time)
        else:
            users['timee'] = noww
            db.set(f'user_{user_id}_giftt', users)
            return None
    else:
        users = {}
        users['timee'] = noww
        db.set(f'user_{user_id}_giftt', users)
        return None

def step_email(message, ban_type):
    if message.text == "/start": return start_message(message)
    username = message.text
    x = bot.reply_to(message, TXT_SEND_EMAIL)
    bot.register_next_step_handler(x, step_screenshot, ban_type, username)

def step_screenshot(message, ban_type, username):
    if message.text == "/start": return start_message(message)
    email = message.text
    x = bot.reply_to(message, TXT_SEND_SCREENSHOT)
    bot.register_next_step_handler(x, step_confirm, ban_type, username, email)
def confirm_unban(cid, mid):
    order = db.get(f"temp_order_{cid}")
    if not order:
        bot.edit_message_text("❌ انتهت صلاحية الطلب.", chat_id=cid, message_id=mid)
        return
    
    user_info = get(cid)
    if not user_info or user_info.get('coins', 0) < UNBAN_SERVICE_PRICE:
        bot.edit_message_text(TXT_NOT_ENOUGH_COINS, chat_id=cid, message_id=mid)
        return
        
    # خصم الرصيد
    user_info['coins'] -= UNBAN_SERVICE_PRICE
    set_user(cid, user_info)

    # رقم طلب
    order_id = int(time.time())

    # أنواع الباند (عرض احترافي)
    BAN_TYPE_LABELS = {
        "mzaha": "نزاهة (Account Integrity)",
        "ibahi": "إباحي (Adult Content)",
        "copyright": "حقوق (Copyright)",
        "violence": "عنف (Violence)",
        "fraud": "احتيال (Fraud)"
    }

    ban_type_key = order['ban_type'].replace("ban_", "")
    ban_label = BAN_TYPE_LABELS.get(ban_type_key, ban_type_key)

    # تأكيد للمستخدم
    bot.edit_message_text(TXT_ORDER_CONFIRMED, chat_id=cid, message_id=mid)

    # 📄 نص الطلب
    info_text = f"""🆕 طلب فك باند جديد!

🆔 رقم الطلب: {order_id}
🔹 النوع: {ban_label}

👤 المستخدم: {cid}
📌 اليوزر: @{order['username']}
📧 الإيميل: {order['email']}

💰 السعر: {UNBAN_SERVICE_PRICE}
🕒 الحالة: قيد المراجعة ⏳"""

    # 📤 إرسال للإدمن
    admins = db.get("admins")
    if admins:
        for admin in admins:
            try:
                bot.send_photo(admin, order['photo_id'], caption=info_text)
            except:
                try:
                    bot.send_message(admin, info_text)
                except:
                    pass

    # 📢 إرسال للقناة
    try:
        bot.send_photo(UNBAN_CHANNEL, order['photo_id'], caption=info_text)
    except:
        try:
            bot.send_message(UNBAN_CHANNEL, info_text)
        except Exception as e:
            print(f"Channel Error: {e}")

    # 📧 إرسال الإيميل
    try:
        send_unban_email(order)
    except Exception as e:
        print(f"Email Error: {e}")

    # 🔔 إشعار المستخدم
    try:
        bot.send_message(
            cid,
            f"""✅ تم استلام طلبك

🆔 رقم الطلب: {order_id}
🔹 النوع: {ban_label}

💰 تم خصم: {UNBAN_SERVICE_PRICE}
⏳ الحالة: قيد المراجعة

📩 سيتم إشعارك عند الانتهاء"""
        )
    except:
        pass

    # حذف الطلب المؤقت
    db.delete(f"temp_order_{cid}")
def step_confirm(message, ban_type, username, email):
    if message.text == "/start": return start_message(message)
    
    photo_id = None
    if message.photo:
        photo_id = message.photo[-1].file_id
    elif message.document:
        photo_id = message.document.file_id
        
    if not photo_id:
        x = bot.reply_to(message, TXT_MUST_SEND_PHOTO)
        bot.register_next_step_handler(x, step_confirm, ban_type, username, email)
        return
        
    cid = message.from_user.id
    db.set(f"temp_order_{cid}", {
        "ban_type": ban_type.replace('ban_', ''),
        "username": username,
        "email": email,
        "photo_id": photo_id
    })
    
    summary_text = TXT_ORDER_SUMMARY.format(ban_type=ban_type.replace('ban_', ''), username=username, email=email)
    keys = mk(row_width=2)
    keys.add(btn(BTN_CONFIRM_ORDER, callback_data='confirm_unban'), btn(BTN_CANCEL_ORDER, callback_data='cancel_unban'))
    bot.send_message(message.chat.id, summary_text, reply_markup=keys)

try:
    bot.infinity_polling()
except:
    pass   