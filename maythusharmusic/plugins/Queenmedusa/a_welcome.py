from pyrogram import Client, filters
from pyrogram.types import Message

# Telegram API credentials
API_ID = "29758428"
API_HASH = "51f9369e03f78674ca21aee8dfd1c842"
BOT_TOKEN = "7792923188:AAGyBuTG16P0290DbKwPtq86g11Vx8qikwQ"

# Create bot client
bot = Client("welcome_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.new_chat_members)
async def welcome(client: Client, message: Message):
    """Handle new members joining the group."""
    for user in message.new_chat_members:
        mention = user.mention(style="md")  # Mention user with Markdown style
        welcome_text = f"🎉 Welcome {mention} to our group! Enjoy your stay! 😊"
        
        await message.reply_text(welcome_text, parse_mode="markdown")

# Start the bot
print("Bot is running...")
bot.run()
