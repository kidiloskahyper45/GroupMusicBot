from pyrogram import filters
from pyrogram.types import Message

from MusicBot.services.callsmusic.callsmusic import client as USER


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    await USER.send_message(
        message.chat.id,
        "**Hi there, This is a music assistant service  [𝙻𝚄𝙽𝙰](@Luna_vc_bot).**\n\n ❗️ **Rules:**\n   - No chatting allowed\n   - No spam allowed \n\n 👉 **SEND GROUP INVITE LINK OR USERNAME IF USERBOT CAN'T JOIN YOUR GROUP.**\n\n **⚠️ Disclamer:** If you are sending a message here it means admin from @HappinessValley will see your message and join chat\n    - Don't add this user to secret groups.\n   - Don't Share private info here.\n\n**Feel Free to Contact Us [APARICHITHAN](https://t.me/stranger_of_telegram).**",
    )
    return
