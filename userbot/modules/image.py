# Ported By VCKYOU @VckyouuBitch
# Credits © Geez-Project
# Ya gitu deh:')

from shutil import rmtree
from userbot.events import register
from userbot import CMD_HELP
from userbot.utils import googleimagesdownload


@register(outgoing=True, pattern="^.img (.*)")
async def goimg(event):
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("`Give something to search...`")
    await event.edit("`Processing Keep Patience...`")
    if ";" in query:
        try:
            lmt = int(query.split(";")[1])
            query = query.split(";")[0]
        except BaseExceptaion:
            lmt = 10
    else:
        lmt = 10
    gi = googleimagesdownload()
    args = {
        "keywords": query,
        "limit": lmt,
        "format": "jpg",
        "output_directory": "./downloads/",
    }
    pth = gi.download(args)
    ok = pth[0][query]
    await event.client.send_file(event.chat_id, ok, caption=query, album=True)
    rmtree(f"./downloads/{query}/")
    await event.delete()


CMD_HELP.update(
    {
        "img": "Cmd: `.img <search_query>`\
         \n↳ : Pencarian gambar di Google dan menunjukkan 5 list gambar."
    }
)
