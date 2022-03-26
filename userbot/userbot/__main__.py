# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot start point """

import sys
from importlib import import_module
from pytgcalls import idle
from userbot import LOOP, BOT_TOKEN, BOTLOG_CHATID, BOT_VER, LOGS, bot, ramblacklist, call_py
from userbot.modules import ALL_MODULES
from userbot.utils.utils import autobot, creatgr
from userbot.clients.logger import ram_ubot_on
try:
    for module_name in ALL_MODULES:
        imported_module = import_module("userbot.modules." + module_name)
    bot.start()
    call_py.start()
    user = bot.get_me()
    if user.id in ramblacklist:
        LOGS.warning(
            "MAKANYA GA USAH BERTINGKAH GOBLOK, USERBOTnya GUA MATIIN NAJIS BANGET DIPAKE JAMET KEK LU.\nCredits: @merdhni"
        )
        sys.exit(1)
    LOGS.info(f"⚡RAM - UBOT⚡ ⚙️ V{BOT_VER} [ TELAH DIAKTIFKAN! ]")
except BaseException as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)

LOOP.run_until_complete(ram_ubot_on())
if not BOTLOG_CHATID:
    LOOP.run_until_complete(creatgr())
if not BOT_TOKEN:
    LOOP.run_until_complete(autobot())
idle()
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    try:
        bot.run_until_disconnected()
    except ConnectionError:
        pass
