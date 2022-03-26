import asyncio

from telethon.tl.functions.channels import EditAdminRequest, InviteToChannelRequest
from telethon.tl.types import ChatAdminRights
from userbot import BOT_VER as version
from userbot import BOTLOG_MSG
from userbot import BOTLOG_CHATID
from userbot import CMD_HANDLER as cmd
from userbot import bot, branch, tgbot
from userbot.utils import hadeh_ajg



async def ram_ubot_on():
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
            RamUbot = await tgbot.get_me()
            BOT_USERNAME = RamUbot.username
            await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME]))
            await asyncio.sleep(3)
    except BaseException:
        pass
    try:
        if bot and tgbot:
            RamUbot = await tgbot.get_me()
            BOT_USERNAME = RamUbot.username
            await bot(EditAdminRequest(BOTLOG_CHATID, BOT_USERNAME, new_rights, "BOT"))
            await asyncio.sleep(3)
    except BaseException:
        pass
    try:
        if BOTLOG_CHATID != 0:
            await bot.send_message(
                BOTLOG_CHATID,
                f"{BOTLOG_MSG}",
             )
    except BaseException:
        pass
