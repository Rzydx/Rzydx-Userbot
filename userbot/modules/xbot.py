# Copyright (C) 2021 King - Userbot
# Created by Apis
# Jangan hapus credit asu!!!
# Recode back team Flicks - Userbot

from random import choice

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import rzydx_cmd

# ================= CONSTANT =================
XBOT_STRINGS = [
    "** Aku Userbot Bang 😎**",
    "** Berani lawan ku gban kau 😁**",
    "** Lawak cuman user telegram belum jadi userbot 😂**",
    "** Userbot ni bos 😎**",

]


@rzydx_cmd(pattern="xbot")
async def xbot(xbotrzydx):
    await xbotrzydx.edit(choice(XBOT_STRINGS))

CMD_HELP.update(
    {
        "xbot": f"**• Plugin Xbot •**\
        \n\n  •  **Perintah :** `{cmd}xbot`\
        \n  •  **Function :** Xbot random untuk bersenang senang saja\
    "
    }
)
