from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from PURVIMUSIC import app
from config import BOT_USERNAME
from PURVIMUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
♡ 𝘞𝘌𝘓𝘊𝘖𝘔𝘌 𝘔𝘈𝘋𝘈𝘙𝘊𝘏𝘖𝘋𝘋 ♡
 
➥𝘙𝘈𝘕𝘋𝘐 𝘒𝘌 𝘉𝘊𝘏𝘌𝘌 ☠︎︎
 
➥ 𝘛𝘌𝘙𝘐 𝘔𝘈𝘈𝘈 𝘒𝘐 𝘊𝘏𝘜𝘛 𝘒𝘐𝘋 ⍥⃝
 
➥ 𝘎𝘈𝘕𝘋 𝘋𝘌 𝘛𝘉 𝘙𝘌𝘗𝘖 𝘋𝘜𝘕𝘎𝘈 ꈍᴗꈍ
 
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("ＡＤＤ ＭＥ ＢＡＢＹ", url=f"https://t.me/Ridi_music_bot?startgroup=true")
        ],
        [
          InlineKeyboardButton("ＧＲＯＵＰ", url="https://t.me/thala_elclassico_07"),
          InlineKeyboardButton("ＤＥＳＴＲＯＹＥＲ", url="https://t.me/ll_destroyerr_ll"),
          ],
               [
                InlineKeyboardButton("ＡＶＥＮＧＥＲＳ ＮＥＴＷＯＲＫ", url=f"https://t.me/Avengers_net_work"),
],
[
InlineKeyboardButton("ＲＩＤＩ ＭＵＳＩＣ ＢＯＴ", url=f"https://t.me/Ridi_music_bot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/3093023b954815189d472.jpg",
        caption=start_txt,
        reply_markup=reply_markup
 )
