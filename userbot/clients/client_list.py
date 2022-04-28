# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
#
# This file is a part of < https://github.com/mrismanaziz/Man-Userbot/ >
# t.me/SharingUserbot & t.me/Lunatic0de

from base64 import b64decode

import telethon.utils
from telethon.tl.functions.users import GetFullUserRequest


async def clients_list(SUDO_USERS, bot, RZYDX2, RZYDX3, RZYDX4, RZYDX5):
    user_ids = list(SUDO_USERS) or []
    rzydx_id = await bot.get_me()
    user_ids.append(rzydx_id.id)

    try:
        if RZYDX2 is not None:
            id2 = await RZYDX2.get_me()
            user_ids.append(id2.id)
    except BaseException:
        pass

    try:
        if RZYDX3 is not None:
            id3 = await RZYDX3.get_me()
            user_ids.append(id3.id)
    except BaseException:
        pass

    try:
        if RZYDX4 is not None:
            id4 = await RZYDX4.get_me()
            user_ids.append(id4.id)
    except BaseException:
        pass

    try:
        if RZYDX5 is not None:
            id5 = await RZYDX5.get_me()
            user_ids.append(id5.id)
    except BaseException:
        pass

    return user_ids


ITSME = list(map(int, b64decode("MTY2MzI1ODY2NA==").split()))


async def client_id(event, botid=None):
    if botid is not None:
        uid = await event.client(GetFullUserRequest(botid))
        OWNER_ID = uid.user.id
        RZYDX_CLIENT = uid.user.first_name
    else:
        client = await event.client.get_me()
        uid = telethon.utils.get_peer_id(client)
        OWNER_ID = uid
        RZYDX_CLIENT = client.first_name
    rzydx_rpk = f"[{RZYDX_CLIENT}](tg://user?id={OWNER_ID})"
    return OWNER_ID, RZYDX_CLIENT, rzydx_rpk
