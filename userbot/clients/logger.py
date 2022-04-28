# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
#
# This file is a part of < https://github.com/mrismanaziz/Man-Userbot/ >
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio
from telethon.tl.functions.channels import EditAdminRequest, InviteToChannelRequest
from telethon.tl.types import ChatAdminRights

from userbot import BOT_VER as version
from userbot import BOTLOG_CHATID
from userbot import CMD_HANDLER as cmd
from userbot import RZYDX2, RZYDX3, RZYDX4, RZYDX5, bot, branch, tgbot
from userbot.utils import rzydxscrt

MSG_ON = """
**Rzydx - UserBot**
➖➖➖➖➖➖➖➖➖➖
**Owner**: [{OWNER}](tg://user?id={OWNER_ID})
**Assistant** : @{BOT_USERNAME}
➖➖➖➖➖➖➖➖➖➖
"""

IN_BTTS = [
    [
        Button.url(
            "Repository",
            url="https://github.com/Rzydx/Rzydx-Userbot",
        ),
        Button.url("Channel", url="https://t.me/RzydxProject"),
    ]
]


async def rzydx_ubot_on():
    new_rights = ChatAdminRights(
        add_admins=True,
        invite_users=True,
        change_info=True,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
        manage_call=True,
    )
    try:
        if bot and tgbot:
            RzydxUBOT = await tgbot.get_me()
            BOT_USERNAME = RzydxUBOT.username
            await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME]))
            await asyncio.sleep(3)
    except BaseException:
        pass
    try:
        if bot and tgbot:
            RzydxUBOT = await tgbot.get_me()
            BOT_USERNAME = RzydxUBOT.username
            await bot(EditAdminRequest(BOTLOG_CHATID, BOT_USERNAME, new_rights, "BOT"))
            await asyncio.sleep(3)
    except BaseException:
        pass
    try:
        if bot:
            await rzydxscrt(bot)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await bot.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if RZYDX2:
            await rzydxscrt(RZYDX2)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await RZYDX2.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if RZYDX3:
            await rzydxscrt(RZYDX3)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await RZYDX3.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if RZYDX4:
            await rzydxscrt(RZYDX4)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await RZYDX4.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if RZYDX5:
            await rzydxscrt(RZYDX5)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await RZYDX5.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
