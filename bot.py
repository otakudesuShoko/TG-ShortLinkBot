# © All rights reserved by Mrvishal2k2
# Kangers dont f*ckin kang this !!!
# Should have to give credits 😏 else f***off 
# This is only for personal use Dont use this for ur bot channel business 😂
# Thanks to Mahesh Malekar for his Gplinks Bot !!

from os import environ
# Moved Back to asyncio-dev branch of pyrogram
from pyrogram import Client, Filters, InlineKeyboardButton, InlineKeyboardMarkup
import pyshorteners

API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')
API_KEY = environ.get('API_KEY')

bot = Client('Shortlink bot',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=50,
             sleep_threshold=10)


@bot.on_message(Filters.command('start') & Filters.private)
async def start(bot, update):
    await update.reply(
         "https://telegra.ph/file/9679efa9a400052f2835e.jpg",
        f"**Hi {update.chat.first_name}!**\n"
        "**Saya Bot Pemendek Tautan Tanpa Iklan!!**\n"
        "**Silakan gunakan /help untuk cara penggunaan 💡**\n\n"
        "**Bot Developed & Maintained by** [i'm](https://t.me/Hyoneechan)\n\n"
        "Channel Hiburan [Memes](https://t.ms/MemesRpi)")
      
@bot.on_message(Filters.regex(r'https?://[^\s]+') & Filters.private)
async def link_handler(bot, update):
    link = update.matches[0].group(0)
    if API_KEY:
      try:
        s = pyshorteners.Shortener(api_key=API_KEY) 
        shortened_url = s.cuttly.short(link)
        button = [[InlineKeyboardButton("Link 🔗", url=shortened_url)]]
        markup = InlineKeyboardMarkup(button)
        await update.reply_text(text=f'Here is your shortlink \n`{shortened_url}`', reply_markup=markup, quote=True)
        
      except Exception as e:
        await update.reply(f'Error: {e}', quote=True)
    else:
      try:
        s = pyshorteners.Shortener() 
        shortened_url = s.dagd.short(link)
        button = [[InlineKeyboardButton("Link 🔗", url=shortened_url)]]
        markup = InlineKeyboardMarkup(button)
        await update.reply_text(text=f'Here is your shortlink \n`{shortened_url}`', reply_markup=markup, quote=True)
        
      except Exception as e:
        await update.reply(f'Error: {e}', quote=True)

      

bot.run()
