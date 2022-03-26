import asyncio

from telethon.errors.rpcerrorlist import FloodWaitError

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, DEVG, DEVS, owner
from userbot.events import register
from userbot.utils import edit_delete, edit_or_reply, ram_cmd

GCAST_BLACKLIST = [
    -1001473548283,  # SharingUserbot
    -1001752592753,  # TedeSupport
    -1001476936696,  # AnosSupport
    -1001327032795,  # UltroidSupport
    -1001294181499,  # UserBotIndo
    -1001419516987,  # VeezSupportGroup
    -1001459812644,  # GeezSupportGroup
    -1001296934585,  # X-PROJECT BOT
    -1001481357570,  # UsergeOnTopic
    -1001459701099,  # CatUserbotSupport
    -1001109837870,  # TelegramBotIndonesia
    -1001752592753,  # Skyzusupport
    -1001302879778,  # Karmantot
    -1001462425381,  # GRUP GUA
    -1001512737035,  # hirosi
    -1001267233272,  # POCONG SEREM
    -1001692751821,  # ramsupportt
    -1001489233533,  # rumahkitaro
    -1001234685537,  # ze
]

# BLACKLIST NYA JANGAN DI HAPUS NGENTOD.


@ram_cmd(pattern="gcast(?: |$)(.*)")
@register(pattern=r"^\.cgcast(?: |$)(.*)", sudo=True)
async def gcast(event):
    xx = event.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        return await edit_delete(
            event, "**Anak ngentot, kalo males ngasih teks, MINIMAL REPLY ANJING!!**"
        )
    kk = await edit_or_reply(
        event, f"`{owner} kontol, Limit jangan salain gua tod, Lg gua kirim ni....`"
    )
    er = 0
    done = 0
    # user = await bot.get_me()
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            if chat not in GCAST_BLACKLIST:
                try:
                    await event.client.send_message(chat, msg)
                    await asyncio.sleep(0.1)
                    done += 1
                except FloodWaitError as anj:
                    await asyncio.sleep(int(anj.seconds))
                    await event.client.send_message(chat, msg)
                    done += 1
                except BaseException:
                    er += 1
    await kk.edit(
        f"**{owner} Berhasil Mengirim Pesan Ke** `{done}` **Grup, Gagal Mengirim Pesan Ke** `{er}` **Grup**"
    )


@ram_cmd(pattern="gucast(?: |$)(.*)")
@register(pattern=r"^\.cgucast(?: |$)(.,)", sudo=True)
async def gucast(event):
    xx = event.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        return await edit_delete(
            event, "**anak ngentot, Kalo males ngasih teks, MINIMAL REPLY ANJING!!!**"
        )
    kk = await edit_or_reply(
        event, f"`{owner} sedang mengirim pesan siaran ke beberapa chat pribadi....`"
    )
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            if chat not in DEVS and chat not in DEVG:
                try:
                    await event.client.send_message(chat, msg)
                    await asyncio.sleep(0.1)
                    done += 1
                except FloodWaitError as anj:
                    await asyncio.sleep(int(anj.seconds))
                    await event.client.send_message(chat, msg)
                    done += 1
                except BaseException:
                    er += 1
    await kk.edit(
        f"**{owner} Berhasil Mengirim Pesan Ke** `{done}` **chat, Gagal Mengirim Pesan Ke** `{er}` **chat**"
    )


CMD_HELP.update(
    {
        "gcast": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}gcast`\
         \n↳ : Mengirim Pesan Group Secara Global."
    }
)

CMD_HELP.update(
    {
        "gucast": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}gucast`\
         \n↳ : Mengirim Pesan Pribadi Secara Global."
    }
)
