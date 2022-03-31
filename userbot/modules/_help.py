#    TeleBot - UserBot
#    Copyright (C) 2020 TeleBot

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

#    Recode by Fariz <Github.com/farizjs>
#    From Flicks-Userbot
#    <t.me/TheFlicksUserbot>


from telethon import Button
from userbot import BOT_USERNAME, CMD_HELP, bot
from userbot.utils import flicks_cmd

user = bot.get_me()
DEFAULTUSER = user.first_name
CUSTOM_HELP_EMOJI = "✘"
main_help_menu = [
    [
        Button.inline("•ᴘʟᴜɢɪɴs", data="open"),
        Button.inline("ᴠᴄ ᴘʟᴜɢɪɴs•", data="flicks_inline"),
    ],
    [
        Button.url("•sᴇᴛᴛɪɴɢs", f"t.me/{BOT_USERNAME}"),
    ],
    [Button.inline("•ᴄʟᴏsᴇ•", data="close")],
]


@flicks_cmd(pattern="help ?(.*)")
async def cmd_list(event):
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(f"**🔥 Commands available in {args} 🔥** \n\n" + str(CMD_HELP[args]) + "\n\n**⚡ @RzydxProject**")
        else:
            await event.edit(f"**Module** `{args}` **Tidak tersedia!**")
    else:
        try:
            results = await bot.inline_query(  # pylint:disable=E0602
                BOT_USERNAME, "@margamodedisini"
            )
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        except BaseException:
            await event.edit(
                f"** Sepertinya obrolan atau bot ini tidak mendukung inline mode.**"
            )
