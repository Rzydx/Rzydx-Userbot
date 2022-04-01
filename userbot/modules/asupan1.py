# recode by : ramadhani892

import random

from userbot import CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import rzydx_cmd
from userbot import owner
from telethon.tl.types import InputMessagesFilterVoice
from telethon.tl.types import InputMessagesFilterPhotos


@rzydx_cmd(pattern=r"ayang$")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@CeweLogoPack", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f" [Ayangnya Si Kontol {owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("Silahkan Masuk Ke Bot Asistant, Lalu Klik start.")

@rzydx_cmd(pattern=r"cedesah$")
async def _(event):
    try:
        desahnya = [
            desah
            async for desah in event.client.iter_messages(
                "@desahancewesangesange", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(desahnya),
            caption=f"Ini Bacol Mu Tuan! [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("`Stay Halal Kontol...`")


@rzydx_cmd(pattern=r"codesah$")
async def _(event):
    try:
        desahnya = [
            desah
            async for desah in event.client.iter_messages(
                "@desahancowo", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(desahnya),
            caption=f"Ini Bacol Mu Nyonya [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("`Stay Halal Memek...`")


@rzydx_cmd(pattern=r"ngaji$")
async def _(event):
    try:
        qurannya = [
            quran
            async for quran in event.client.iter_messages(
                "@kureenkeryam", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(qurannya),
            caption=f"Dengarkan Dengan Khusyu [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("`Lu Haram jd gabisa denger Qur'an...`")


CMD_HELP.update(
    {
        "asupan1": f"**Plugin : **`asupan1`\
        \n\n  •  **Syntax :** `{cmd}ayang`\
        \n  •  **Function : **Untuk Mengirim video asupan secara random.\
        \n\n  •  **Syntax :** `{cmd}codesah` or  `{cmd}cedesah`\
        \n  •  **Function : **Untuk Mengirim suara desah buat lu yang sange.\
    "
    }
)
