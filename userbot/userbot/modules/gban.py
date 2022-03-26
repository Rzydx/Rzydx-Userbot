import asyncio
from datetime import datetime
from io import BytesIO

from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import Channel

import userbot.modules.sql_helper.gban_sql as gban_sql
from userbot import BOTLOG_CHATID
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, DEVG, DEVS, ramblacklist
from userbot.events import register
from userbot.utils import chataction, edit_or_reply, get_user_from_event, ram_cmd

from .admins import BANNED_RIGHTS, UNBAN_RIGHTS


async def admin_groups(grp):
    admgroups = []
    async for dialog in grp.client.iter_dialogs():
        entity = dialog.entity
        if (
            isinstance(entity, Channel)
            and entity.megagroup
            and (entity.creator or entity.admin_rights)
        ):
            admgroups.append(entity.id)
    return admgroups


def mentionuser(name, userid):
    return f"[{name}](tg://user?id={userid})"


@ram_cmd(pattern="gbanb(?: |$)(.*)")
@register(pattern=r"^\.cgbanb(?: |$)(.*)", sudo=True)
async def gban(event):
    if event.fwd_from:
        return
    gbun = await edit_or_reply(event, "`Gbanning...`")
    start = datetime.now()
    user, reason = await get_user_from_event(event, gbun)
    if not user:
        return
    if user.id == (await event.client.get_me()).id:
        await gbun.edit("**Kurang kerjaan bat tolol Gban diri sendiri 😔✋**")
        return
    if user.id in DEVS:
        await gbun.edit("**Maaf Masszeh, Lo gabisa gban Dia karna dia Pembuat Gua tolol!!**")
        return
    if user.id in DEVG:
        await gbun.edit("**Maaf Maszeh, Dia temen gua, Gabisa gua gban hehehe!!!**")
        return
    if gban_sql.is_gbanned(user.id):
        await gbun.edit(
            f"**Si** [TOLOL](tg://user?id={user.id}) **ini sudah ada di daftar gbanned**"
        )
    else:
        gban_sql.freakgban(user.id, reason)
    san = []
    san = await admin_groups(event)
    count = 0
    fiz = len(san)
    if fiz == 0:
        await gbun.edit("**Gabisa gban, Soal nya Lu gada GC 😔**")
        return
    await gbun.edit(
        f"**initiating gban of the** [KONTOL](tg://user?id={user.id}) **in** `{len(san)}` **groups**"
    )
    for i in range(fiz):
        try:
            await event.client(EditBannedRequest(san[i], user.id, BANNED_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"**Anda tidak memiliki izin Banned di :**\n**Group Chat :** `{event.chat_id}`",
            )
    end = datetime.now()
    timetaken = (end - start).seconds
    if reason:
        await gbun.edit(
            f"**GBanned** [{user.first_name}](tg://user?id={user.id}) **in** `{count}` **groups in** `{timetaken}` **seconds**!!\n**Reason :** `{reason}`"
        )
    else:
        await gbun.edit(
            f"**GBanned** [{user.first_name}](tg://user?id={user.id}) **in** `{count}` **groups in** `{timetaken}` **seconds**!!\n**Added to gbanlist.**"
        )


@ram_cmd(pattern="ungbanb(?: |$)(.*)")
@register(pattern=r"^\.cungbanb(?: |$)(.*)", sudo=True)
async def ungban(event):
    if event.fwd_from:
        return
    ungbun = await edit_or_reply(event, "`UnGbanning...`")
    start = datetime.now()
    user, reason = await get_user_from_event(event, ungbun)
    if not user:
        return
    if gban_sql.is_gbanned(user.id):
        gban_sql.freakungban(user.id)
    else:
        await ungbun.edit(
            f"**Si** [Jamet](tg://user?id={user.id}) **ini tidak ada dalam daftar gban Anda**"
        )
        return
    san = []
    san = await admin_groups(event)
    count = 0
    fiz = len(san)
    if fiz == 0:
        await ungbun.edit("**Anda Tidak mempunyai GC yang anda admin 🥺**")
        return
    await ungbun.edit(
        f"**initiating ungban of the** [Jamet](tg://user?id={user.id}) **in** `{len(san)}` **groups**"
    )
    for i in range(fiz):
        try:
            await event.client(EditBannedRequest(san[i], user.id, UNBAN_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"**Anda tidak memiliki izin Banned di :**\n**Group Chat :** `{event.chat_id}`",
            )
    end = datetime.now()
    timetaken = (end - start).seconds
    if reason:
        await ungbun.edit(
            f"**Ungbanned** [{user.first_name}](tg://user?id={user.id}`) **in** `{count}` **groups in** `{timetaken}` **seconds**!!\n**Reason :** `{reason}`"
        )
    else:
        await ungbun.edit(
            f"**Ungbanned** [{user.first_name}](tg://user?id={user.id}) **in** `{count}` **groups in** `{timetaken}` **seconds**!!\n**Removed from gbanlist**"
        )


@ram_cmd(pattern="listgban$")
async def gablist(event):
    if event.fwd_from:
        return
    gbanned_users = gban_sql.get_all_gbanned()
    GBANNED_LIST = "**List Global Banned Saat Ini**\n"
    if len(gbanned_users) > 0:
        for a_user in gbanned_users:
            if a_user.reason:
                GBANNED_LIST += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) **Reason** `{a_user.reason}`\n"
            else:
                GBANNED_LIST += (
                    f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) `No Reason`\n"
                )
    if len(gbanned_users) >= 4096:
        with BytesIO(str.encode(GBANNED_LIST)) as fileuser:
            fileuser.name = "list-gban.txt"
            await event.client.send_file(
                event.chat_id,
                fileuser,
                force_document=True,
                thumb="userbot/utils/styles/.RAMUBOT.jpg",
                caption="**List Global Banned**",
                allow_cache=False,
            )
    else:
        GBANNED_LIST = "Belum ada Pengguna yang Di-Gban"
    await edit_or_reply(event, GBANNED_LIST)


@chataction()
async def _(event):
    if event.user_joined or event.added_by:
        user = await event.get_user()
        chat = await event.get_chat()
        if gban_sql.is_gbanned(user.id) and ramblacklist and chat.admin_rights:
            try:
                await event.client.edit_permissions(
                    chat.id,
                    user.id,
                    view_messages=False,
                )
                await event.reply(
                    f"**#GBanned_User** Joined.\n\n** • First Name:** [{user.first_name}](tg://user?id={user.id})\n • **Action:** `Banned`"
                )
            except BaseException:
                pass


# Ported by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot


CMD_HELP.update(
    {
        "gban": f"**Plugin : **`gban`\
        \n\n  •  **Syntax :** `{cmd}gban` <username/id>\
        \n  •  **Function : **Melakukan Banned Secara Global Ke Semua Grup Dimana anda Sebagai Admin.\
        \n\n  •  **Syntax :** `{cmd}ungban` <username/id>\
        \n  •  **Function : **Membatalkan Global Banned\
        \n\n  •  **Syntax :** `{cmd}listgban`\
        \n  •  **Function : **Menampilkan List Global Banned\
    "
    }
)
