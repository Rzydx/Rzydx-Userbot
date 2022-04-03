# Thanks Full To Team Ultroid
# Fiks By Kyy @IDnyaKosong


from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc
from telethon.tl.functions.phone import EditGroupCallTitleRequest as settitle

from telethon.tl import types
from telethon.utils import get_display_name

from userbot import owner
from userbot import CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import edit_delete, edit_or_reply, rzydx_cmd
from userbot.events import register

NO_ADMIN = "`Maaf Kamu Bukan Admin 👮`"


def vcmention(user):
    full_name = get_display_name(user)
    if not isinstance(user, types.User):
        return full_name
    return f"[{full_name}](tg://user?id={user.id})"


async def get_call(kyy):
    kyym = await kyy.client(getchat(kyy.chat_id))
    hehe = await kyy.client(getvc(kyym.full_chat.call, limit=1))
    return hehe.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i: i + n]


@rzydx_cmd(pattern="startvc$")
@register(pattern=r"^\.startvcs$", sudo=True)
async def start_voice(c):
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await edit_delete(c, f"**Maaf {owner} Bukan Admin 👮**")
        return
    try:
        await c.client(startvc(c.chat_id))
        await edit_or_reply(c, "`Memulai Obrolan Suara`")
    except Exception as ex:
        await edit_or_reply(c, f"**ERROR:** `{ex}`")


@rzydx_cmd(pattern="stopvc$")
@register(pattern=r"^\.stopvcs$", sudo=True)
async def stop_voice(c):
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await edit_delete(c, f"**Maaf {owner} Bukan Admin 👮**")
        return
    try:
        await c.client(stopvc(await get_call(c)))
        await edit_or_reply(c, "`Mematikan Obrolan Suara`")
    except Exception as ex:
        await edit_delete(c, f"**ERROR:** `{ex}`")


@rzydx_cmd(pattern="vcinvite")
async def _(rzydx):
    await edit_or_reply(rzydx, "`Sedang Menginvite Member...`")
    users = []
    z = 0
    async for x in rzydx.client.iter_participants(rzydx.chat_id):
        if not x.bot:
            users.append(x.id)
    hmm = list(user_list(users, 6))
    for p in hmm:
        try:
            await rzydx.client(invitetovc(call=await get_call(rzydx), users=p))
            z += 6
        except BaseException:
            pass
    await edit_or_reply(rzydx, f"`Menginvite {z} Member`")


@rzydx_cmd(pattern="vctitle(?: |$)(.*)")
@register(pattern=r"^\.cvctitle$", sudo=True)
async def change_title(e):
    title = e.pattern_match.group(1)
    me = await e.client.get_me()
    chat = await e.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not title:
        return await edit_delete(e, "**Silahkan Masukan Title Obrolan Suara Grup**")

    if not admin and not creator:
        await edit_delete(e, f"**Maaf {me.first_name} Bukan Admin 👮**")
        return
    try:
        await e.client(settitle(call=await get_call(e), title=title.strip()))
        await edit_or_reply(e, f"**Berhasil Mengubah Judul VCG Menjadi** `{title}`")
    except Exception as ex:
        await edit_delete(e, f"**ERROR:** `{ex}`")


@rzydx_cmd(pattern="joinvc(?: |$)(.*)")
@register(pattern=r"^\.joinvcs(?: |$)(.*)", sudo=True)
async def _(event):
    Man = await edit_or_reply(event, "`Processing...`")
    if len(event.text.split()) > 1:
        chat_id = event.text.split()[1]
        try:
            chat_id = await event.client.get_peer_id(int(chat_id))
        except Exception as e:
            return await rzydx.edit(f"**ERROR:** `{e}`")
    else:
        chat_id = event.chat_id
    file = "./userbot/resources/audio-man.mp3"
    if chat_id:
        try:
            await call_py.join_group_call(
                chat_id,
                InputStream(
                    InputAudioStream(
                        file,
                    ),
                ),
                stream_type=StreamType().local_stream,
            )
            await rzydx.edit(
                f"❏ **Berhasil Join Ke Obrolan Suara**\n└ **Chat ID:** `{chat_id}`"
            )
        except AlreadyJoinedError:
            await call_py.leave_group_call(chat_id)
            await edit_delete(
                rzydx,
                "**ERROR:** `Karena akun sedang berada di obrolan suara`\n\n• Silahkan coba `.joinvc` lagi",
                45,
            )
        except Exception as e:
            await rzydx.edit(f"**INFO:** `{e}`")


@rzydx_cmd(pattern="leavevc(?: |$)(.*)")
@register(pattern=r"^\.leavevcs(?: |$)(.*)", sudo=True)
async def vc_end(event):
    Man = await edit_or_reply(event, "`Processing...`")
    if len(event.text.split()) > 1:
        chat_id = event.text.split()[1]
        try:
            chat_id = await event.client.get_peer_id(int(chat_id))
        except Exception as e:
            return await rzydx.edit(f"**ERROR:** `{e}`")
    else:
        chat_id = event.chat_id
    if chat_id:
        try:
            await call_py.leave_group_call(chat_id)
            await edit_delete(
                rzydx,
                f"❏ **Berhasil Turun dari Obrolan Suara**\n└ **Chat ID:** `{chat_id}`",
            )
        except Exception as e:
            await rzydx.edit(f"**INFO:** `{e}`")


CMD_HELP.update(
    {
        "vcg": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}startvc`\
         \n↳ : Memulai Obrolan Suara dalam Group.\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}stopvc`\
         \n↳ : `Menghentikan Obrolan Suara Pada Group.`\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}vctittle <tittle vcg>`\
         \n↳ : `Mengubah tittle/judul Obrolan Suara.`\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}vcinvite`\
         \n↳ : Invite semua member yang berada di group."
        \n\n  • ** Syntax: ** `{cmd}joinvc` atau `{cmd}joinvc` < chatid / username gc > n  • ** Function: **Untuk Bergabung ke voice chat group
         \n\n  • ** Syntax: ** `{cmd}leavevc` atau `{cmd}leavevc` < chatid / username gc > n  • ** Function: **Untuk Turun dari voice chat group
        "
    }
)
