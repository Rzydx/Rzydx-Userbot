from time import sleep
from userbot import CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import rzydx_cmd


@rzydx_cmd(pattern='rzydx(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hai Perkenalkan Nama Gua Rizky Yudha`")
    sleep(3)
    await typew.edit("`Asli Majalengka`")
    sleep(1)
    await typew.edit("`Umurku Sembilan Belas, Tapi Aku Tidak Malas, Salam Kenal:)`")
# Create by myself @localheart


@rzydx_cmd(pattern='jhor(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Yo Halo Semua Perkenalkan, Nama Gua jhor`")
    sleep(3)
    await typew.edit("`Biasa Di Panggil Bang Jhor`")
    sleep(1)
    await typew.edit("`Tingga Di Jakarta Barat, Salam Kenal Ya:)`")
# Create by myself @localheart



@rzydx_cmd(pattern='sayang(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Cuma Mau Bilang`")
    sleep(3)
    await typew.edit("`Muka Lu Kaya Kontol`")
    sleep(1)
    await typew.edit("`I LOVE YOU 💞`")
# Create by myself @localheart


@rzydx_cmd(pattern='semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Bernapas`")
    sleep(1)
    await typew.edit("`Dan Selalu Bersyukur`")
# Create by myself @localheart


CMD_HELP.update({
    "oi": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}rzydx`\
    \n↳ : perkenalan rzydx\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}sayang`\
    \n↳ : Gombalan maut`\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}semangat`\
    \n↳ : Jan Lupa Semangat."
})
