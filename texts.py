# texts.py

TXT_WELCOME = "مرحباً بك في أقوى بوت متخصص في فك الحسابات المبندة على انستقرام 🔓"
TXT_ADMIN_PANEL = "**• اهلا بك في لوحة الأدمن الخاصة بالبوت 🤖**\n\n- يمكنك التحكم في البوت الخاص بك من هنا \n\n==================="
TXT_FORCE_SUB = "• عليك الاشتراك بقناة البوت اولا لتتمكن من استخدام خدمات فك الباند \n• @{channel}"
TXT_INVITE_SELF = "لا يمكنك الدخول عبر الرابط الخاص بك ❌"
TXT_INVITE_SUCCESS = "• قام {username} بالدخول الى رابط الدعوة الخاص بك وحصلت على {dd} نقطة ✨"

TXT_BUY = '''💳 معلومات الدفع

يمكنك شحن رصيدك عبر الطرق التالية:

📱 جوال / محفظة جيب:
775130555

🏦 كريمي:
🔹 السعودي: 3144700723
🔹 اليمني: 3144724037
🔹 الدولار: 3132695309

🔶 Binance (عملات رقمية):
💳 معرّف الحساب: 484530509

👤 للتواصل أو تأكيد الدفع:
يرجى إرسال الحوالة إلى أحد الحسابات التالية:
@mddo87


💰 سعر الخدمة:
3000 ريال يمني (قديم)

📌 مهم:
بعد التحويل، يرجى إرسال صورة الحوالة أو إثبات الدفع لإتمام إضافة الرصيد بنجاح.'''

TXT_FREE_SERVICES_GREET = 'اهلا بك بقسم الخدمات المجانية لفك الباند 🔓'
TXT_COLLECT_POINTS = '• مرحبا بك في قسم تجميع النقاط \n\n• يمكنك تجميع النقاط لطلب فك الباند عبر الازرار التي امامك'
TXT_BOT_ERROR = '• حدث خطأ ما في البوت'

def TXT_SHARE_LINK(link, users_count, y):
    return f'''
 
انسخ الرابط ثم قم بمشاركته مع اصدقائك لجمع النقاط!!
 
~  كل شخص يقوم بالدخول ستحصل على 1 نقطة تستخدمها لفك حسابك المبند

🌀 رابط الدعوة : \n {link}  .

~ مشاركتك للرابط :  {users_count}  .

{y}
        '''

TXT_GIFT_TOMORROW = 'طالب بالهدية غدا في: {date_str2}'
TXT_GIFT_CONGRATS = "• تهانيناً، لقد حصلت على هدية يومية بقيمة {daily_gift} نقطة 🎁"
TXT_DEL_ADMIN = '• ارسل ايدي العضو المراد ازالته من الادمن'
TXT_ADD_ADMIN = '• ارسل ايدي العضو المراد اضافته كأدمن بالبوت '
TXT_ADMINS_LIST = 'الادمنية : \n'
TXT_NO_ADMINS = 'لا يوجد ادمنية بالبوت'
TXT_LES_POINTS = '• ارسل ايدي الشخص المراد خصم النقاط منه'
TXT_ADD_POINTS = '• ارسل ايدي الشخص المراد اضافة النقاط له'
TXT_BAN_ONE = '• ارسل ايدي العضو المراد حظره من استخدام البوت'
TXT_UNBAN_ONE = '• ارسل ايدي العضو المراد الغاء حظره من استخدام البوت '
TXT_CAST = 'ارسل الاذاعة التي تريد إرسالها... صورة، فيديو، ملصق، نص، متحركة ..'
TXT_STATS = '• عدد مستخدمي البوت : {good}'
TXT_SET_FORCE = '• قم بارسال معرفات القنوات هكذا \n@TMXH2 @TMXH2'

def TXT_ACCOUNT_INFO(coins, users, prem, daily_count, all_gift, buys, trans, y):
    return f'''
معلومات حسابك لفك الباند 🔓:
• [❇️] أداة فك الباند (النقاط) : {coins}
• [🌀] عدد عمليات الاحالة التي قمت بها : {users}
• [👤] نوع اشتراكك داخل البوت : {prem}
• [🎁] عدد الهدايا اليومية التي جمعتها : {daily_count}
• [❇️] إجمالي النقاط المكتسبة من الهدايا : {all_gift}
• [📮] عدد الحسابات التي طلبت فكها : {buys}
• [♻️] عدد التحويلات التي قمت بها : {trans}

{y}'''

TXT_INVALID_ID = 'أرسل الايدي بشكل صحيح'
TXT_INVALID_ID_REPLY = '• أرسل الايدي بشكل صحيح رجاءً'
TXT_ALREADY_BANNED = '• هذا العضو محظور من قبل '
TXT_BAN_SUCCESS = '• تم حظر العضو من استخدام البوت'
TXT_NOT_BANNED = '• هذا العضو غير محظور '
TXT_UNBAN_SUCCESS = '• تم الغاء حظر العضو بنجاح ✅'
TXT_INVALID_CHANNEL = '• رجاءً أرسل القناة بشكل صحيح'
TXT_SUCCESS = 'تمت العملية بنجاح ✅'
TXT_CAST_START = '• جاري الاذاعة الى مستخدمين البوت الخاص بك '
TXT_CAST_SUCCESS = '• اكتملت الاذاعة بنجاح ✅\n• تم الارسال الى : {good}\n• لم يتم الارسال الى : {bad} '
TXT_ALREADY_ADMIN = '• هذا العضو ادمن بالفعل'
TXT_ADD_ADMIN_SUCCESS = '• تم اضافته كأدمن بنجاح ✅'
TXT_NOT_ADMIN = '• هذا العضو ليس من الادمنية بالبوت'
TXT_DEL_ADMIN_SUCCESS = '• تم ازالة العضو من الادمنية بنجاح ✅'
TXT_SEND_AMOUNT = '• ارسل الان الكمية'
TXT_SEND_AMOUNT_2 = '• ارسل الان الكمية :'
TXT_AMOUNT_NUMBERS_ONLY = 'يجب ان تكون الكمية أرقام فقط'
TXT_POINTS_SUCCESS = 'تم بنجاح، رصيده الآن : {coins} نقطة'

TXT_TREND_TITLE = "• المستخدمين الاكثر مشاركة لرابط الدعوة : \n"
TXT_TREND_ITEM = "🏅: ({users_count}) إحالة > {user_id}\n"


# BUTTONS
BTN_BACK = 'رجوع'
BTN_BACK_DOT = 'رجوع .'
BTN_STATS = '🤍الاحصائيات'
BTN_CAST = '⚠️اذاعة'
BTN_BAN_ONE = '➖حظر شخص'
BTN_UNBAN_ONE = 'فك حظر'
BTN_NUMBERS = '🔥معرفة عدد الارقام'
BTN_ADD_VIP = '➕تفعيل ViP للفك'
BTN_LES_VIP = '➖الغاء ViP'
BTN_LEAVE = '➖مغادرة كل الحسابات من قناة'
BTN_LVALL = '➖مغادرة كل القنوات والمجموعات'
BTN_SET_FORCE = 'تعيين قنوات الاشتراك'
BTN_LES_POINTS = '➖خصم نقاط'
BTN_ADD_POINTS = 'اضافة نقاط '
BTN_ADD_ADMIN = '➕اضافة ادمن'
BTN_DEL_ADMIN = '➖مسح ادمن'
BTN_ADMINS = '⚠️الادمنية '
BTN_DUMP_VOTES = '➖سحب اصوات'
BTN_SPAMS = '〽️سبام رسائل (بوتات ، جروبات ، حسابات) '

def BTN_BALANCE(coin): return f'نقاطك : {coin}'
BTN_SERVICES = 'خدمات فك الباند 🔓'
BTN_ACCOUNT = 'معلومات حسابك 🗃'
BTN_COLLECT = 'تجميع النقاط ❇️'
BTN_SEND = 'تحويل نقاط ♻️'
BTN_CHANNEL = 'قناة البوت 🩵'
BTN_BUY = 'شراء نقاط 💰'
def BTN_ORDERS_COUNT(count_ord): return f'طلبات الفك : {count_ord} ✅'

BTN_FREE_SERVICES = 'خدمات الفك المجانية'
BTN_VIP_SERVICES = 'الخدمات الـ ViP للفك'
BTN_DAILY_GIFT = 'الهدية اليومية 🎁'
BTN_SHARE_LINK = 'رابط الدعوة 🌀'

# BAN TYPES
BTN_BAN_MZAHA = 'نزاهة'
BTN_BAN_IBAHI = 'اباحي'
BTN_BAN_COPYRIGHT = 'حقوق'
BTN_BAN_VIOLENCE = 'عنف'
BTN_BAN_FRAUD = 'احتيال'
TXT_SELECT_BAN_TYPE = 'اختر نوع الباند الخاص بحسابك لتقديم طلب الفك 🔓:'
TXT_UNBAN_REQUEST_RECEIVED = 'تم استلام طلبك بنجاح ✅\nسيتم مراجعة الطلب من قبل المختصين والرد عليك قريباً.'

TXT_NOT_ENOUGH_COINS = "⚠️ عذراً، لا تملك رصيد كافي لتنفيذ هذه الخدمة."
BTN_BUY_COINS = "💰 شراء رصيد"

TXT_SEND_USERNAME = "أدخل اسم المستخدم أو رابط الحساب المراد تنفيذ الخدمة عليه:"
TXT_SEND_EMAIL = "أدخل البريد الإلكتروني المرتبط بالحساب المبند:"
TXT_SEND_SCREENSHOT = "أرسل لقطة شاشة (صورة) تثبت أن الحساب مبند:"
TXT_ORDER_SUMMARY = "ملخص الطلب:\n- نوع الباند: {ban_type}\n- الحساب: {username}\n- الإيميل: {email}\n\nهل أنت متأكد من تقديم الطلب وخصم الرصيد؟"

BTN_CONFIRM_ORDER = "تأكيد الطلب ✅"
BTN_CANCEL_ORDER = "إلغاء ❌"
TXT_ORDER_CONFIRMED = "تم تأكيد طلبك وخصم الرصيد بنجاح! سيتم مراجعة الطلب قريباً."
TXT_ORDER_CANCELLED = "تم إلغاء الطلب."
TXT_MUST_SEND_PHOTO = "يرجى إرسال صورة كلقطة شاشة، حاول مجدداً:"
UNBAN_SERVICE_PRICE = 3000
