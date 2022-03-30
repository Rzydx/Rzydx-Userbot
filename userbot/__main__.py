# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
# Thanks Man-Userbot for autobot
""" Userbot start point """

from importlib import import_module

from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from userbot import BOTLOG_CHATID, BOT_TOKEN, BOT_USERNAME, BOT_VER, LOGS, bot
from userbot.modules import ALL_MODULES
from userbot.modules.assistant import ASST_MODULES
from userbot.utils import autobot, autopilot
from userbot.pytgcalls import call_py


INVALID_PH = '\nERROR: The Phone No. entered is INVALID' \
             '\n Tip: Use Country Code along with number.' \
             '\n or check your phone number and try again !'


try:
    bot.start()
    call_py.start()
except PhoneNumberInvalidError:
    print(INVALID_PH)
    exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

for module_name in ASST_MODULES:
    imported_module = import_module("userbot.modules.assistant." + module_name)

if not BOTLOG_CHATID:
    LOGS.info(
        "BOTLOG_CHATID Vars tidak terisi, Sabar Kontol Gw Lagi Buat Grup Otomatis..."
    )
    bot.loop.run_until_complete(autopilot())

if not BOT_TOKEN:
    LOGS.info(
        "BOT_TOKEN Vars tidak terisi, Kontol Sabar Ngapa Gua Lagi Bikin Bot Otomatis Di @Botfather..."
    )
    bot.loop.run_until_complete(autobot())

LOGS.info(
    f"Kalo Lu Bingung Terus Butuh Bantuan, Tinggal Tanya Ajah Di Grup https://t.me/Rzydx_Support")
LOGS.info(
    f"♨️Rzydx-Userbot♨️ ⚡ V{BOT_VER} [UDAH AKTIF YA KONTOL!]")


async def check_alive():
    try:
        if BOTLOG_CHATID != 0:
            await bot.send_message(BOTLOG_CHATID, "•••╼═⍟═♨️ʀᴢʏᴅx-ᴜsᴇʀʙᴏᴛ♨️═⍟═╾•••\n╒ ➠ ৯• **ᴜsᴇʀʙᴏᴛ ᴠᴇʀsɪᴏɴ** - 3.1.5\n╞ ➠ ৯• **ᴋᴇᴛɪᴋ** `.ping` **ʙᴜᴀᴛ ɴɢᴇᴄᴇᴋ ʙᴏᴛ ʟᴜ ᴛᴏᴅ**\n╘ ➠ ৯• **ᴘᴏᴡᴇʀᴇᴅ ʙʏ** @RzydxProject\n•••••╼══════⍟══════╾•••••\n🔥 **ᴜsᴇʀʙᴏᴛ ʙᴇʀʜᴀsɪʟ ᴅɪᴀᴋᴛɪꜰᴋᴀɴ** 🔥 ")
    except Exception as e:
        LOGS.info(str(e))
    try:
        await bot(JoinChannelRequest("@RzydxProject"))
    except BaseException:
        pass
    try:
        await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass
    try:
        await bot(Addbot(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass

bot.loop.run_until_complete(check_alive())
if not BOT_TOKEN:
    LOGS.info(
        "BOT_TOKEN Vars tidak terisi, Si Kontol, Sabar Tod Ini Lagi Bikin Bot Otomatis Di @Botfather..."
    )
    bot.loop.run_until_complete(autobot())

if len not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
