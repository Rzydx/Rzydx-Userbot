""" Userbot initialization. """

import logging
import os
import time
import re
import redis
import random
import pybase64
import sys

from asyncio import get_event_loop
from base64 import b64decode
from sys import version_info
from logging import basicConfig, getLogger, INFO, DEBUG
from distutils.util import strtobool as sb
from math import ceil
from pathlib import Path

from git import Repo
from pylast import LastFMNetwork, md5
from pySmartDL import SmartDL
from pytgcalls import PyTgCalls
from pymongo import MongoClient
from datetime import datetime
from redis import StrictRedis
from dotenv import load_dotenv
from requests import get
from telethon import Button
from telethon.sync import TelegramClient, custom, events
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.tl.functions.channels import JoinChannelRequest as GetSec
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sessions import StringSession
from telethon.sync import TelegramClient, custom, events
from telethon import Button, events, functions, types
from telethon.tl.types import InputWebDocument
from telethon.utils import get_display_name
from telethon import version

from .storage import Storage


def STORAGE(n):
    return Storage(Path("data") / n)


redis_db = None

LOOP = get_event_loop()
repo = Repo()
branch = repo.active_branch.name


# Global Variables
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
ENABLE_KILLME = True
LASTMSG = {}
CMD_HELP = {}
ISAFK = False
AFKREASON = None
ZALG_LIST = {}
CMD_LIST = {}
CMD_HELP = {}
SUDO_LIST = {}
INT_PLUG = ""
LOAD_PLUG = {}

load_dotenv("config.env")

StartTime = time.time()

# Bot Logs setup:
logging.basicConfig(
    format="[%(name)s] - [%(levelname)s] - %(message)s",
    level=logging.INFO,
)
logging.getLogger("asyncio").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)
logging.getLogger("telethon.network.mtprotosender").setLevel(logging.ERROR)
logging.getLogger(
    "telethon.network.connection.connection").setLevel(logging.ERROR)
LOGS = getLogger(__name__)

CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

if CONSOLE_LOGGER_VERBOSE:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=DEBUG,
    )
else:
    basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                level=INFO)
LOGS = getLogger(__name__)

if version_info[0] < 3 or version_info[1] < 8:
    LOGS.info("You MUST have a python version of at least 3.8."
              "Multiple features depend on this. Bot quitting.")
    quit(1)

# Check if the config was edited by using the already used variable.
# Basically, its the 'virginity check' for the config file ;)
CONFIG_CHECK = os.environ.get(
    "___________PLOX_______REMOVE_____THIS_____LINE__________", None)

if CONFIG_CHECK:
    LOGS.info(
        "Please remove the line mentioned in the first hashtag from the config.env file"
    )
    quit(1)

DEVS = (
    1338853808,
    1663258664,
    1410223312,
)
# =====================================================================
SUDO_USERS = {
    int(x) for x in os.environ.get(
        "SUDO_USERS",
        "").split()}
BL_CHAT = {int(x) for x in os.environ.get("BL_CHAT", "").split()}
BLACKLIST_GCAST = {
    int(x) for x in os.environ.get(
        "BLACKLIST_GCAST",
        "").split()}

# For Blacklist Group Support
BLACKLIST_CHAT = os.environ.get("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001473548283]

# =====================================================================
# Telegram App KEY and HASH
API_KEY = int(os.environ.get("API_ID") or os.environ.get(
    "API_KEY" or "6"))
API_HASH = str(os.environ.get("API_HASH") or None)

# Userbot Session String
STRING_SESSION = os.environ.get("STRING_SESSION", None)
STRING_2 = os.environ.get("STRING_2", None)
STRING_3 = os.environ.get("STRING_3", None)
STRING_4 = os.environ.get("STRING_4", None)
STRING_5 = os.environ.get("STRING_5", None)

# Userbot Session String
VC_SESSION = os.environ.get("VC_SESSION", "")

# Logging channel/group ID configuration.
BOTLOG_CHATID = int(os.environ.get("BOTLOG_CHATID", "0"))

# Handler Userbot
CMD_HANDLER = os.environ.get("CMD_HANDLER") or "."
SUDO_HANDLER = os.environ.get("SUDO_HANDLER") or "$"

# Default .alive Name
ALIVE_NAME = os.environ.get("ALIVE_NAME", "Rzydx")

# Userbot logging feature switch.
BOTLOG = sb(os.environ.get("BOTLOG", "True"))
LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", "True"))

# Bleep Blop, this is a bot ;)
PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "False"))
PM_LIMIT = int(os.environ.get("PM_LIMIT", 6))

# Send .chatid in any group with all your administration bots (added)
G_BAN_LOGGER_GROUP = os.environ.get("G_BAN_LOGGER_GROUP", f"{BOTLOG_CHATID}")
if G_BAN_LOGGER_GROUP:
    G_BAN_LOGGER_GROUP = int(G_BAN_LOGGER_GROUP)

# Heroku Credentials for updater.
HEROKU_MEMEZ = sb(os.environ.get("HEROKU_MEMEZ", "True"))
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", "")
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "")

# JustWatch Country
WATCH_COUNTRY = os.environ.get("WATCH_COUNTRY", "ID")

# Github Credentials for updater and Gitupload.
GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)

# Custom (forked) repo URL for updater.
UPSTREAM_REPO_URL = os.environ.get(
    "UPSTREAM_REPO_URL",
    "https://github.com/Rzydx/Rzydx-Userbot")
UPSTREAM_REPO_BRANCH = os.environ.get(
    "UPSTREAM_REPO_BRANCH", "Rzydx-Userbot")

# Console verbose logging
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

# SQL Database URI
DB_URI = os.environ.get("DATABASE_URL", None)

# OCR API key
OCR_SPACE_API_KEY = os.environ.get(
    "OCR_SPACE_API_KEY") or "12dc42a0ff88957"

# remove.bg API key
REM_BG_API_KEY = os.environ.get(
    "REM_BG_API_KEY") or "ihAEGNtfnVtCsWnzqiXM1GcS"

# Redis URI & Redis Password
REDIS_URI = os.environ.get('REDIS_URI', None)
REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD', None)

if REDIS_URI and REDIS_PASSWORD:
    try:
        REDIS_HOST = REDIS_URI.split(':')[0]
        REDIS_PORT = REDIS_URI.split(':')[1]
        redis_connection = redis.Redis(
            host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD
        )
        redis_connection.ping()
    except Exception as e:
        logging.exception(e)
        print()
        logging.error(
            "Make sure you have the correct Redis endpoint and password "
            "and your machine can make connections."
        )

# Chrome Driver and Headless Google Chrome Binaries
CHROME_BIN = os.environ.get("CHROME_BIN", "/app/.apt/usr/bin/google-chrome")
CHROME_DRIVER = os.environ.get("CHROME_DRIVER") or "/usr/bin/chromedriver"
GOOGLE_CHROME_BIN = os.environ.get(
    "GOOGLE_CHROME_BIN") or "/usr/bin/google-chrome"

# set to True if you want to log PMs to your PM_LOGGR_BOT_API_ID
NC_LOG_P_M_S = bool(os.environ.get("NC_LOG_P_M_S", False))
# send .get_id in any channel to forward all your NEW PMs to this group
PM_LOGGR_BOT_API_ID = int(os.environ.get("PM_LOGGR_BOT_API_ID", "-100"))

# OpenWeatherMap API Key
OPEN_WEATHER_MAP_APPID = os.environ.get(
    "OPEN_WEATHER_MAP_APPID") or "5ed2fcba931692ec6bd0a8a3f8d84936"
WEATHER_DEFCITY = os.environ.get("WEATHER_DEFCITY", "Indonesia")

# Lydia API
LYDIA_API_KEY = os.environ.get(
    "LYDIA_API_KEY") or "632740cd2395c73b58275b54ff57a02b607a9f8a4bbc0e37a24e7349a098f95eaa6569e22e2d90093e9c1a9cc253380a218bfc2b7af2e407494502f6fb76f97e"

# For MONGO based DataBase
MONGO_URI = os.environ.get("MONGO_URI", None)

# set blacklist_chats where you do not want userbot's features
UB_BLACK_LIST_CHAT = os.environ.get("UB_BLACK_LIST_CHAT", None)

# Anti Spambot Config
ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))
ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))

# Youtube API key
YOUTUBE_API_KEY = os.environ.get(
    "YOUTUBE_API_KEY") or "AIzaSyACwFrVv-mlhICIOCvDQgaabo6RIoaK8Dg"

# Untuk Perintah .ralive
RZYDX_TEKS_KUSTOM = os.environ.get(
    "RZYDX_TEKS_KUSTOM",
    "I'am Using Rzydx-Userbot 🔥")


# Time & Date - Country and Time Zone
COUNTRY = str(os.environ.get("COUNTRY", "ID"))
TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))

# Clean Welcome
CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))

# Zipfile Module
ZIP_DOWNLOAD_DIRECTORY = os.environ.get("ZIP_DOWNLOAD_DIRECTORY", "./zips")

# bit.ly Module
BITLY_TOKEN = os.environ.get(
    "BITLY_TOKEN") or "o_1fpd9299vp"

# Bot Name
TERM_ALIAS = os.environ.get("TERM_ALIAS", "Rzydx-Userbot")

# Bot Version
BOT_VER = os.environ.get("BOT_VER", "2.1.2")

# Default .alive Username
ALIVE_USERNAME = os.environ.get("ALIVE_USERNAME", None)

# Sticker Custom Pack Name
S_PACK_NAME = os.environ.get("S_PACK_NAME", None)

# Default .alive Logo
ALIVE_LOGO = os.environ.get(
    "ALIVE_LOGO") or "https://telegra.ph/file/a43123fb4508e7eb69de6.jpg"

# Default pmpermit logo
PMPERMIT_PIC = os.environ.get(
    "PMPERMIT_PIC") or "https://telegra.ph/file/a43123fb4508e7eb69de6.jpg"

# Default .helpme Logo
INLINE_PIC = os.environ.get(
    "INLINE_PIC") or "https://telegra.ph/file/a43123fb4508e7eb69de6.jpg"

# Picture For VCPLUGIN
PLAY_PIC = (os.environ.get("PLAY_PIC")
            or "https://telegra.ph/file/6213d2673486beca02967.png")

QUEUE_PIC = (os.environ.get("QUEUE_PIC")
             or "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
# Last.fm Module
BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
DEFAULT_BIO = os.environ.get("DEFAULT_BIO", "Rzydx-Userbot ♨️")

LASTFM_API = os.environ.get(
    "LASTFM_API") or "73d42d9c93626709dc2679d491d472bf"

LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
LASTFM_PASS = md5(LASTFM_PASSWORD_PLAIN)
if LASTFM_API and LASTFM_SECRET and LASTFM_USERNAME and LASTFM_PASS:
    lastfm = LastFMNetwork(api_key=LASTFM_API,
                           api_secret=LASTFM_SECRET,
                           username=LASTFM_USERNAME,
                           password_hash=LASTFM_PASS)
else:
    lastfm = None

# Google Drive Module
G_DRIVE_DATA = os.environ.get("G_DRIVE_DATA", None)
G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
G_DRIVE_FOLDER_ID = os.environ.get("G_DRIVE_FOLDER_ID", None)
TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY",
                                         "./downloads")
# Google Photos
G_PHOTOS_CLIENT_ID = os.environ.get("G_PHOTOS_CLIENT_ID", None)
G_PHOTOS_CLIENT_SECRET = os.environ.get("G_PHOTOS_CLIENT_SECRET", None)
G_PHOTOS_AUTH_TOKEN_ID = os.environ.get("G_PHOTOS_AUTH_TOKEN_ID", None)
if G_PHOTOS_AUTH_TOKEN_ID:
    G_PHOTOS_AUTH_TOKEN_ID = int(G_PHOTOS_AUTH_TOKEN_ID)

# Genius Lyrics  API
GENIUS = os.environ.get(
    "GENIUS") or "vDhUmdo_ufwIvEymMeMY65IedjWaVm1KPupdx0L"

# Quotes API Token
QUOTES_API_TOKEN = os.environ.get(
    "QUOTES_API_TOKEN") or "33273f18-4a0d-4a76-8d78-a16faa002375"

# Wolfram Alpha API
WOLFRAM_ID = os.environ.get("WOLFRAM_ID") or None

# Deezloader
DEEZER_ARL_TOKEN = os.environ.get("DEEZER_ARL_TOKEN", None)

# Photo Chat - Get this value from http://antiddos.systems
API_TOKEN = os.environ.get("API_TOKEN", None)
API_URL = os.environ.get("API_URL", "http://antiddos.systems")

# Inline bot helper
BOT_TOKEN = os.environ.get("BOT_TOKEN") or None
BOT_USERNAME = os.environ.get("BOT_USERNAME") or None

# Jangan di hapus Nanti ERROR
while 0 < 6:
    _BLACKLIST = get(
        "https://raw.githubusercontent.com/mrismanaziz/Reforestation/master/manblacklist.json"
    )
    if _BLACKLIST.status_code != 200:
        if 0 != 5:
            continue
        blacklistman = []
        break
    blacklistman = _BLACKLIST.json()
    break

while 0 < 6:
    _WHITELIST = get(
        "https://raw.githubusercontent.com/mrismanaziz/Reforestation/master/whitelist.json"
    )
    if _WHITELIST.status_code != 200:
        if 0 != 5:
            continue
        WHITELIST = []
        break
    WHITELIST = _WHITELIST.json()
    break

del _WHITELIST

# Init Mongo
MONGOCLIENT = MongoClient(MONGO_URI, 27017, serverSelectionTimeoutMS=1)
MONGO = MONGOCLIENT.userbot


def is_mongo_alive():
    try:
        MONGOCLIENT.server_info()
    except BaseException:
        return False
    return True


# Init Redis
# Redis will be hosted inside the docker container that hosts the bot
# We need redis for just caching, so we just leave it to non-persistent
REDIS = StrictRedis(host='localhost', port=6379, db=0)


def is_redis_alive():
    try:
        REDIS.ping()
        return True
    except BaseException:
        return False


# Setting Up CloudMail.ru and MEGA.nz extractor binaries,
# and giving them correct perms to work properly.
if not os.path.exists('bin'):
    os.mkdir('bin')

binaries = {
    "https://raw.githubusercontent.com/adekmaulana/megadown/master/megadown":
    "bin/megadown",
    "https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py":
    "bin/cmrudl"
}

for binary, path in binaries.items():
    downloader = SmartDL(binary, path, progress_bar=False)
    downloader.start()
    os.chmod(path, 0o755)

# 'bot' variable
if STRING_SESSION:
    session = StringSession(str(STRING_SESSION))
else:
    session = "Rzydx-UserBot"
try:
    bot = TelegramClient(
        session=session,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py = PyTgCalls(bot)
except Exception as e:
    print(f"STRING_SESSION - {e}")
    sys.exit()

if STRING_2:
    session2 = StringSession(str(STRING_2))
    RZYDX2 = TelegramClient(
        session=session2,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py2 = PyTgCalls(RZYDX2)
else:
    call_py2 = None
    RZYDX2 = None


if STRING_3:
    session3 = StringSession(str(STRING_3))
    RZYDX3 = TelegramClient(
        session=session3,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py3 = PyTgCalls(RZYDX3)
else:
    call_py3 = None
    RZYDX3 = None


if STRING_4:
    session4 = StringSession(str(STRING_4))
    RZYDX4 = TelegramClient(
        session=session4,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py4 = PyTgCalls(RZYDX4)
else:
    call_py4 = None
    RZYDX4 = None


if STRING_5:
    session5 = StringSession(str(STRING_5))
    RZYDX5 = TelegramClient(
        session=session5,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py5 = PyTgCalls(RZYDX5)
else:
    call_py5 = None
    RZYDX5 = None


if BOT_TOKEN is not None:
    tgbot = TelegramClient(
        "TG_BOT_TOKEN",
        api_id=API_KEY,
        api_hash=API_HASH).start(
        bot_token=BOT_TOKEN)
else:
    tgbot = None


def paginate_help(page_number, loaded_modules, prefix):
    number_of_rows = 6
    number_of_cols = 2
    global lockpage
    lockpage = page_number
    helpable_modules = [p for p in loaded_modules if not p.startswith("_")]
    helpable_modules = sorted(helpable_modules)
    modules = [
        custom.Button.inline(
            "{} {} ✘".format(
                "✘", x), data="ub_modul_{}".format(x))
        for x in helpable_modules
    ]
    pairs = list(zip(modules[::number_of_cols],
                     modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows: number_of_rows * (
                modulo_page + 1)] + [
            (custom.Button.inline(
                "««", data="{}_prev({})".format(
                    prefix, modulo_page)), custom.Button.inline(
                        "•ᴄʟᴏsᴇ•", data="{}_close({})".format(
                            prefix, modulo_page)), custom.Button.inline(
                                "»»", data="{}_next({})".format(
                                    prefix, modulo_page)), )]
    return pairs


def ibuild_keyboard(buttons):
    keyb = []
    for btn in buttons:
        if btn[2] and keyb:
            keyb[-1].append(Button.url(btn[0], btn[1]))
        else:
            keyb.append([Button.url(btn[0], btn[1])])
    return keyb


with bot:
    try:

        from userbot.modules.sql_helper.bot_blacklists import check_is_black_list
        from userbot.modules.sql_helper.bot_pms_sql import add_user_to_db, get_user_id
        from userbot.utils import reply_id

        dugmeler = CMD_HELP
        me = bot.get_me()
        logo = ALIVE_LOGO
        user = bot.get_me()
        uid = user.id
        ALIVE_NAME = user.first_name
        owner = user.first_name
        BTN_URL_REGEX = re.compile(
            r"(\[([^\[]+?)\]\<buttonurl:(?:/{0,2})(.+?)(:same)?\>)"
        )

        rzydxlogo = INLINE_PIC
        plugins = CMD_HELP
        vr = BOT_VER

        main_help_button = [
            [
                Button.inline("• ᴘʟᴜɢɪɴs", data="open"),
                Button.inline("ᴠᴄ ᴘʟᴜɢɪɴs •", data="rzydx_inline"),
            ],
            [
                Button.url("⚙ sᴇᴛᴛɪɴɢs", f"t.me/{BOT_USERNAME}?start=set"),
                Button.inline("ᴏᴡɴᴇʀ ᴛᴏᴏʟs ⚙", data="ownrmn"),
            ],
            [Button.inline("•ᴄʟᴏsᴇ•", data="close")],
        ]

        @tgbot.on(events.NewMessage(incoming=True,
                  func=lambda e: e.is_private))
        async def bot_pms(event):
            chat = await event.get_chat()
            if check_is_black_list(chat.id):
                return
            if chat.id != uid:
                msg = await event.forward_to(uid)
                try:
                    add_user_to_db(
                        msg.id, get_display_name(chat), chat.id, event.id, 0, 0
                    )
                except Exception as e:
                    LOGS.error(str(e))
                    if BOTLOG:
                        await event.client.send_message(
                            BOTLOG_CHATID,
                            f"**ERROR:** Saat menyimpan detail pesan di database\n`{str(e)}`",
                        )
            else:
                if event.text.startswith("/"):
                    return
                reply_to = await reply_id(event)
                if reply_to is None:
                    return
                users = get_user_id(reply_to)
                if users is None:
                    return
                for usr in users:
                    user_id = int(usr.chat_id)
                    reply_msg = usr.reply_id
                    user_name = usr.first_name
                    break
                if user_id is not None:
                    try:
                        if event.media:
                            msg = await event.client.send_file(
                                user_id,
                                event.media,
                                caption=event.text,
                                reply_to=reply_msg,
                            )
                        else:
                            msg = await event.client.send_message(
                                user_id,
                                event.text,
                                reply_to=reply_msg,
                                link_preview=False,
                            )
                    except UserIsBlockedError:
                        return await event.reply(
                            "❌ **Bot ini diblokir oleh pengguna.**"
                        )
                    except Exception as e:
                        return await event.reply(f"**ERROR:** `{e}`")
                    try:
                        add_user_to_db(
                            reply_to,
                            user_name,
                            user_id,
                            reply_msg,
                            event.id,
                            msg.id)
                    except Exception as e:
                        LOGS.error(str(e))
                        if BOTLOG:
                            await event.client.send_message(
                                BOTLOG_CHATID,
                                f"**ERROR:** Saat menyimpan detail pesan di database\n`{e}`",
                            )

        @tgbot.on(events.CallbackQuery(data=b"keluar"))
        async def keluar(event):
            await event.delete()

        @tgbot.on(events.NewMessage(pattern=r"/repo"))
        async def handler(event):
            if event.message.from_id != uid:
                u = await event.client.get_entity(event.chat_id)
                await event.reply(
                    f"👋🏻 Hai [{get_display_name(u)}](tg://user?id={u.id}) Jika anda\n"
                    f"Ingin melihat repository ini dan Cara deploynya\n\n"
                    f"👇🏻 __Klik button url di bawah ini__ 👇🏻\n\n"
                    f"**RZYDX USERBOT**\n",
                    buttons=[
                        [
                            Button.url("Repository",
                                       "https://github.com/Rzydx/Rzydx-Userbot"),
                            Button.url("Tutorial",
                                       "https://t.me/RzydxProject")],
                    ]
                )

        @tgbot.on(events.NewMessage(pattern=r"/alive"))
        async def handler(event):
            if event.message.from_id != uid:
                u = await event.client.get_entity(event.chat_id)
                await event.message.get_sender()
                text = (
                    f"**Hello** [{get_display_name(u)}](tg://user?id={u.id}) **Is Its Alive Bot**\n\n"
                    f"         🔥 𝐑𝐳𝐲𝐝𝐱-𝐔𝐬𝐞𝐫𝐛𝐨𝐭 🔥 \n"
                    "▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱\n"
                    f"          I'ᴍ Aʟɪᴠᴇ​ ✨ \n"
                    "▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱ \n"
                    f"`Pengguna  :` [{get_display_name(u)}](tg://user?id={u.id}) \n"
                    f"`Branch    :` {UPSTREAM_REPO_BRANCH} \n"
                    f"`Versi     :` {BOT_VER} \n"
                    f"`Bahasa    :` Python \n"
                    f"`Database  :` Mongo db \n"
                    f"`Owner     :` {ALIVE_NAME} \n\n"
                    "▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱ \n"
                    f"       Tᴇʟᴇɢʀᴀᴍ Usᴇʀʙᴏᴛ \n"
                    "▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱")
                await tgbot.send_file(event.chat_id, file=logo,
                                      caption=text,
                                      buttons=[
                                              [
                                                  custom.Button.url(
                                                      text="Rᴇᴘᴏ",
                                                      url="https://github.com/Rzydx/Rzydx-Userbot"),
                                                  custom.Button.url(
                                                      text="Lɪsᴇɴsɪ​",
                                                      url="https://github.com/Rzydx/Rzydx-Userbot/blob/Rzydx-Userbot/LICENSE"
                                                  )
                                              ]
                                      ]
                                      )

        @ tgbot.on(events.NewMessage(pattern=r"/string"))
        async def handler(event):
            if event.message.from_id != uid:
                reply = "**STRING SESSION**"
                await event.reply(
                    f"**Hai Kamu!**\n\n"
                    f"Ingin Mengambil String Session?\n\n"
                    f"Cukup Ambil Dibawah Button URL Ini\n\n"
                    f"[⚠️](https://telegra.ph/file/69ff21e48b49af969fd8f.jpg) **Gunakan String Session Dengan Bijak!!**\n\n"
                    f"{reply}\n",
                    buttons=[
                        [
                            Button.url("Dengan Web",
                                       "https://replit.com/@fjgaming212/StringSession#main.py"),
                            Button.url("Dengan Bot",
                                       "https://t.me/RzydxStringbot")],
                    ]
                )

        @tgbot.on(events.NewMessage(pattern="/ping"))
        async def handler(event):
            if event.message.from_id != uid:
                start = datetime.now()
                end = datetime.now()
                ms = (end - start).microseconds / 1000
                await tgbot.send_message(
                    event.chat_id,
                    f"**PONG!!**\n `{ms}ms`",
                )

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"get_back")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                current_page_number = int(lockpage)
                buttons = paginate_help(current_page_number, plugins, "helpme")
                text = f"\n**​🔥 𝐑𝐳𝐲𝐝𝐱-𝐔𝐬𝐞𝐫𝐛𝐨𝐭 🔥​**\n\n**• Oᴡɴᴇʀ {ALIVE_NAME}**\n**• Vᴇʀsɪᴏɴ : `{BOT_VER}`**\n**• Pʟᴜɢɪɴs :** `{len(plugins)}`\n"
                await event.edit(
                    text,
                    file=rzydxlogo,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                reply_pop_up_alert = f"Kamu Tidak diizinkan, ini Userbot Milik {ALIVE_NAME}"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"open")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                buttons = paginate_help(0, plugins, "helpme")
                text = f"\n**​🔥 𝐑𝐳𝐲𝐝𝐱-𝐔𝐬𝐞𝐫𝐛𝐨𝐭 🔥​**\n\n**• Oᴡɴᴇʀ {ALIVE_NAME}**\n**• Vᴇʀsɪᴏɴ : `{BOT_VER}`**\n**• Pʟᴜɢɪɴs :** `{len(plugins)}`\n"
                await event.edit(
                    text,
                    file=rzydxlogo,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                reply_pop_up_alert = f"Kamu Tidak diizinkan, ini Userbot Milik {ALIVE_NAME}"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(events.InlineQuery)
        async def inline_handler(event):
            builder = event.builder
            result = None
            query = event.text
            if event.query.user_id == uid and query.startswith(
                    "@Rzydx_Userbot"):
                result = builder.photo(
                    file=rzydxlogo,
                    link_preview=False,
                    text=f"\n**​🔥 𝐑𝐳𝐲𝐝𝐱-𝐔𝐬𝐞𝐫𝐛𝐨𝐭 🔥​**\n\n**• Oᴡɴᴇʀ {ALIVE_NAME}**\n**• Vᴇʀsɪᴏɴ : `{BOT_VER}`**\n**• Pʟᴜɢɪɴs :** `{len(plugins)}`".format(
                        len(dugmeler),
                    ),
                    buttons=main_help_button,
                )
            elif query.startswith("rzydxalive"):
                result = builder.article(
                    "Rzydx-Userbot ",
                    text=f"""
[⁣]({ALIVE_LOGO})**Rzydx Userbot**
{RZYDX_TEKS_KUSTOM}
┏━━━━━━━━━━━━━━━━━━━
┣  **Master**   : {ALIVE_NAME}
┣  **Telethon** :` 1.24.0 `
┣  **Bahasa**   : `Python`
┣  **Branch**   :` {UPSTREAM_REPO_BRANCH} `
┣  **Bot Ver**  :` {BOT_VER} `
┣  **Modules**  :` {len(plugins)} Modules `
┣  **Support**  : @margamodedisini
┗━━━━━━━━━━━━━━━━━━━
""",
                    buttons=[
                        [
                            custom.Button.url(
                                "ᴅᴇᴘʟᴏʏ​",
                                "https://heroku.com/deploy?template=https://github.com/Rzydx/Rzydx-Userbot"),
                            custom.Button.url(
                                "ʀᴇᴘᴏ",
                                "https://github.com/Rzydx/Rzydx-Userbot")],
                        [custom.Button.url(
                            "ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ​",
                            "t.me/RzydxProject")]],
                    link_preview=True)
            elif query.startswith("Inline buttons"):
                markdown_note = query[14:]
                prev = 0
                note_data = ""
                buttons = []
                for match in BTN_URL_REGEX.finditer(markdown_note):
                    n_escapes = 0
                    to_check = match.start(1) - 1
                    while to_check > 0 and markdown_note[to_check] == "\\":
                        n_escapes += 1
                        to_check -= 1
                    if n_escapes % 2 == 0:
                        buttons.append(
                            (match.group(2), match.group(3), bool(
                                match.group(4))))
                        note_data += markdown_note[prev: match.start(1)]
                        prev = match.end(1)
                    elif n_escapes % 2 == 1:
                        note_data += markdown_note[prev:to_check]
                        prev = match.start(1) - 1
                    else:
                        break
                else:
                    note_data += markdown_note[prev:]
                message_text = note_data.strip()
                tl_ib_buttons = ibuild_keyboard(buttons)
                result = builder.article(
                    title="Inline creator",
                    text=message_text,
                    buttons=tl_ib_buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    " 🔥 𝐑𝐳𝐲𝐝𝐱-𝐔𝐬𝐞𝐫𝐛𝐨𝐭 🔥",
                    text=f"""**•••╼⍟═🔥ʀᴢʏᴅx-ᴜsᴇʀʙᴏᴛ🔥═⍟╾•••**\n╒ ➠ ৯• **Oᴡɴᴇʀ​** {ALIVE_NAME}\n╞ ➠ ৯• **Vᴇʀsɪᴏɴ :** {BOT_VER}\n╞ ➠ ৯• **ᴘʟᴜɢɪɴs** : {len(plugins)}\n╘ ➠ ৯• **ᴀssɪsᴛᴇɴ :** @{BOT_USERNAME}\n**•••╼══════⍟══════╾•••**""",
                    buttons=[
                        [
                            custom.Button.url(
                                "sᴜᴘᴘᴏʀᴛ",
                                "t.me/margamodedisini"),
                            custom.Button.url(
                                "ᴄʜᴀɴɴᴇʟ​​",
                                "t.me/RzydxProject")],
                        [custom.Button.url(
                            "ʀᴇᴘᴏ",
                            "https://github.com/Rzydx/Rzydx-Userbot")]],
                    link_preview=False,
                )
            await event.answer(
                [result], switch_pm=f"ASSISTANT BOT OF {ALIVE_NAME}", switch_pm_param="start"
            )

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"helpme_next\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # pylint:disable=E0602
                current_page_number = int(
                    event.data_match.group(1).decode("UTF-8"))
                buttons = paginate_help(
                    current_page_number + 1, dugmeler, "helpme")
                # https://t.me/TelethonChat/115200
                await event.edit(buttons=buttons)
            else:
                reply_pop_up_alert = f"Jangan Menggunakan Milik {ALIVE_NAME}."
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"helpme_close\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # @Rzydx_Userbot
                # https://t.me/TelethonChat/115200
                await event.edit(
                    file=rzydxlogo,
                    link_preview=True,
                    buttons=main_help_button)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"gcback")
            )
        )
        async def gback_handler(event):
            if event.query.user_id == uid:  # @Rzydx_Userbot
                # https://t.me/TelethonChat/115200
                text = (
                    f"\n**​🔥 𝐑𝐳𝐲𝐝𝐱-𝐔𝐬𝐞𝐫𝐛𝐨𝐭 🔥​**\n\n**• Oᴡɴᴇʀ {ALIVE_NAME}**\n**• Vᴇʀsɪᴏɴ : `{BOT_VER}`**\n**• Pʟᴜɢɪɴs :** `{len(plugins)}`\n")
                await event.edit(
                    text,
                    file=rzydxlogo,
                    link_preview=True,
                    buttons=main_help_button)

        @ tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"ownrmn")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                text = (
                    f"Owner menu untuk {ALIVE_NAME} \n"
                    f"`Branch    :` {UPSTREAM_REPO_BRANCH} \n"
                    f"`Versi Bot :` {BOT_VER} \n"
                    f"`Plugins   :` {len(plugins)} \n"
                    f"`Bahasa    :` Python \n"
                    f"`Database  :` SQL \n")
                await event.edit(
                    text,
                    file=rzydxlogo,
                    link_preview=True,
                    buttons=[
                        [
                            Button.inline("Ping ⚡",
                                          data="pingbot"),
                            Button.inline("Info ?",
                                          data="about")],
                        [custom.Button.inline(
                            "Back", data="gcback")],
                    ]
                )
            else:
                reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @ tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"pingbot")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                start = datetime.now()
                end = datetime.now()
                ms = (end - start).microseconds / 1000
                await event.answer(
                    f"**PONG!!**\n `{ms}ms`", cache_time=0, alert=True)
            else:
                reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @ tgbot.on(events.CallbackQuery(data=b"about"))
        async def about(event):
            await event.edit(f"""
Owner - {ALIVE_NAME}
OwnerID - {uid}
[Link To Profile 👤](tg://user?id={uid})
Owner repo - [ Rzydx ](tg://openmessage?user_id=5169252959)
Support - @margamodedisini
Rzydx-Userbot [v{BOT_VER}](https://github.com/Rzydx/Rzydx-Userbot)
""",
                             buttons=[
                                 [
                                     Button.url("Repo",
                                                "https://github.com/Rzydx/Rzydx-Userbot"),
                                     custom.Button.inline("ʙᴀᴄᴋ​",
                                                          data="ownrmn")],
                             ]
                             )

        @tgbot.on(events.CallbackQuery(data=b"rzydx_inline"))
        async def about(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                await event.edit(f"""
Voice chat group menu untuk [{user.first_name}](tg://user?id={user.id})
""",
                                 buttons=[
                                     [
                                         Button.inline("ᴠᴄ ᴘʟᴜɢɪɴ ⚙️",
                                                       data="vcplugin"),
                                         Button.inline("ᴠᴄ ᴛᴏᴏʟs ⚙️",
                                                       data="vctools")],
                                     [custom.Button.inline(
                                         "ʙᴀᴄᴋ", data="gcback")],
                                 ]
                                 )
            else:
                reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"vcplugin")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                text = (
                    f"""
✘ **Commands available in vcplugin** ✘

  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 : `{cmd}play` <Judul Lagu/Link YT>
  ↳ : Untuk Memutar Lagu di voice chat group dengan akun kamu

  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 : `{cmd}vplay` <Judul Video/Link YT>
  ↳ : Untuk Memutar Video di voice chat group dengan akun kamu

  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 : `{cmd}end`
  ↳ : Untuk Memberhentikan video/lagu yang sedang putar di voice chat group

  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 : `{cmd}skip`
  ↳ : Untuk Melewati video/lagu yang sedang di putar

  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 : `{cmd}pause`
  ↳ : Untuk memberhentikan video/lagu yang sedang diputar

  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 : `{cmd}resume`
  ↳ : Untuk melanjutkan pemutaran video/lagu yang sedang diputar

  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 : `{cmd}volume` 1-200
  ↳ : Untuk mengubah volume (Membutuhkan Hak admin)

  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 : `{cmd}playlist`
  ↳ : Untuk menampilkan daftar putar Lagu/Video
""")
                await event.edit(
                    text,
                    file=rzydxlogo,
                    link_preview=True,
                    buttons=[Button.inline("ʙᴀᴄᴋ", data="rzydx_inline")])
            else:
                reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"vctools")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                text = (
                    f"""
✘ **Commands available in vctools** ✘

  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 : `{cmd}startvc`
  ↳ : Untuk Memulai voice chat group

  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 : `{cmd}stopvc`
  ↳ : Untuk Memberhentikan voice chat group

  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 : `{cmd}vctitle` <title vcg>
  ↳ : Untuk Mengubah title/judul voice chat group

  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 : `{cmd}vcinvite`
  ↳ : Mengundang Member group ke voice chat group

  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 : `{cmd}joinvc`
  ↳ : Melakukan Fake voice chat group

  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 : `{cmd}leavevc`
  ↳ : Memberhentikan Fake voice chat group
""")
                await event.edit(
                    text,
                    file=rzydxlogo,
                    link_preview=True,
                    buttons=[Button.inline("ʙᴀᴄᴋ", data="rzydx_inline")])
            else:
                reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @ tgbot.on(events.CallbackQuery(data=b"close"))
        async def close(event):
            buttons = [
                (custom.Button.inline("Bᴜᴋᴀ Mᴇɴᴜ", data="gcback"),),
            ]
            await event.edit("**Mᴇɴᴜ Dɪᴛᴜᴛᴜᴘ​!**", file=rzydxlogo, buttons=buttons)

        @ tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"helpme_prev\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # pylint:disable=E0602
                current_page_number = int(
                    event.data_match.group(1).decode("UTF-8"))
                buttons = paginate_help(
                    current_page_number - 1, dugmeler, "helpme"  # pylint:disable=E0602
                )
                # https://t.me/TelethonChat/115200
                await event.edit(buttons=buttons)
            else:
                reply_pop_up_alert = f"🔒 Tombol Hanya bisa digunakan oleh {ALIVE_NAME} 🔒."
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @ tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"ub_modul_(.*)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # pylint:disable=E0602
                modul_name = event.data_match.group(1).decode("UTF-8")

                cmdhel = str(CMD_HELP[modul_name])
                if len(cmdhel) > 4030:
                    help_string = (
                        str(CMD_HELP[modul_name]).replace(
                            '__', '')[:4030] + "..."
                        + "\n\nBaca Text Berikutnya Ketik .help "
                        + modul_name
                        + " "
                    )
                else:
                    help_string = str(CMD_HELP[modul_name]).replace('`', '')

                reply_pop_up_alert = (
                    help_string
                    if help_string is not None
                    else "{} No document has been written for module.".format(
                        modul_name
                    )
                )

                await event.edit(
                    reply_pop_up_alert, buttons=[
                        Button.inline("Back", data="get_back")]
                )
            else:
                reply_pop_up_alert = f"""Jangan Menggunakan Milik {ALIVE_NAME} !"""
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    except BaseException:
        LOGS.info(
            "Mode Inline Bot Mu Nonaktif. "
            "Untuk Mengaktifkannya, Silahkan Gunakan Perintah .inlineon. ")
