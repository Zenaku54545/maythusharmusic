import os
from pyrogram import Client, filters
from pyrogram.types import ChatMemberUpdated
from logging import getLogger
from maythusharmusic import app

logger = getLogger(__name__)

# Handler for new members joining
@app.on_chat_member_updated(filters.group)
async def welcome(_, event: ChatMemberUpdated):
    if event.new_chat_member and event.new_chat_member.status == "member":
        user = event.new_chat_member.user
        chat_id = event.chat.id
        await app.send_message(chat_id, f"{user.mention} ωᴇℓᴄᴏᴍᴇ ʙᴀʙʏ 🎉")

# Start the bot
if __name__ == "__main__":
    logger.info("Bot is running...")
    app.run()
