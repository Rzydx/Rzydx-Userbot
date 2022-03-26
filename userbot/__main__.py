# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot start point """

import sys
from importlib import import_module

import requests
from telethon.tl.functions.channels import InviteToChannelRequest as Addbot
from userbot import (
    BOTLOG_CHATID,
    BOT_USERNAME,
    BOT_TOKEN,
    BOT_VER,
    LOGS,
    bot,
    call_py,
)
from userbot.modules import ALL_MODULES
from userbot.utils import autobot, autopilot

try:
    bot.start()
    call_py.start()
    user = bot.get_me()
    rzydxblacklist = requests.get(
        "https://raw.githubusercontent.com/Rzydx/Rzydxblack/master/rzydxblacklist.json"
    ).json()
    if user.id in rzydxblacklist:
        LOGS.warning(
            "MAKANYA GAK USAH BELAGU KONTOL, USERBOTnya GUA MATIIN NAJIS BANGET DIPAKE AMA ORANG KEK LU.\nCredits: @Ngapain_Ngetag"
        )
        sys.exit(1)
except Exception as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

if not BOTLOG_CHATID:
    LOGS.info(
        "BOTLOG_CHATID Vars tidak terisi, Memulai Membuat Grup Otomatis..."
    )
    bot.loop.run_until_complete(autopilot())

LOGS.info(
    f"Kalo {user.first_name} Bingung dan Perlu Bantuan, Silahkan Tanya Aja di Grup https://t.me/Rzydx_Support")
LOGS.info(
    f"♨️Rzydx-Userbot♨️ ⚡ V{BOT_VER} [UDAH AKTIF YA KONTOL!]")


async def check_alive():
    try:
        if BOTLOG_CHATID != 0:
            await bot.send_message(BOTLOG_CHATID, "♨️ **Rzydx Userbot Udah Aktif Kontol**!!\n━━━━━━━━━━━━━━━\n➠ **Userbot Version** - 3.1.5@Rzydx-Userbot\n➠ **Ketik** `.ping` **Buat Ngecheck Bot Lu Tod**\n━━━━━━━━━━━━━━━\n➠ **Powered By:** @Aksara_Rassa ")
    except Exception as e:
        LOGS.info(str(e))
    try:
        await bot(Addbot(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass

bot.loop.run_until_complete(check_alive())
if not BOT_TOKEN:
    LOGS.info(
        "BOT_TOKEN Vars tidak terisi, Memulai Membuat BOT Otomatis di @Botfather..."
    )
    bot.loop.run_until_complete(autobot())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
