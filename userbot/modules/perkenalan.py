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


@rzydx_cmd(pattern='maull(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`πππ ππππππ ππππ πππππππ`")
    sleep(3)
    await typew.edit("`ππππ πππ πππππ, πππππ ππππππ`")
    sleep(1)
    await typew.edit("`πππππ πππππ ππ πππππππ π`")
# Create by myself @localheart


@rzydx_cmd(pattern='sayang(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Cuma Mau Bilang`")
    sleep(3)
    await typew.edit("`Muka Lu Kaya Kontol`")
    sleep(1)
    await typew.edit("`I LOVE YOU π`")
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
    "oi": f"πΎπ€π’π’ππ£π: `{cmd}rzydx`\
    \nβ³ : perkenalan rzydx\
    \n\nπΎπ€π’π’ππ£π: `{cmd}sayang`\
    \nβ³ : Gombalan maut`\
    \n\nπΎπ€π’π’ππ£π: `{cmd}semangat`\
    \nβ³ : Jan Lupa Semangat."
})
