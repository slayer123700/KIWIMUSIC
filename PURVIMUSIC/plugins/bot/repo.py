
Navigation Menu

Code
Pull requests
Actions
BreadcrumbsPURVI_MUSIC/PURVIMUSIC/plugins/bot
/repo.py
Latest commit
Adithakur008
Adithakur008
last month
History
89 lines (67 loc) · 3.24 KB
File metadata and controls

Code

Blame
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from PURVIMUSIC import app
from config import BOT_USERNAME
from PURVIMUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
✪ ᴡᴇʟᴄᴏᴍᴇ ʀᴀɴᴅɪ ᴋᴇ ʙᴄʜᴇ ✪
 
 ➲ ʀᴇᴘᴏ ᴋᴇ ʟɪʏᴇ ʙᴀᴀᴘ ʙᴏʟ 🤣
 
 ➲ ɢᴀɴᴅ ᴅᴇ ʀᴇᴘᴏ ᴅᴇᴅᴜɴɢᴀ 😘
 
 ➲ ʜᴛᴛ ᴛᴇʀɪ ᴍᴀᴀ ᴋɪ ᴄʜᴜᴛ 😍
 
 ➲ ɢᴀɴᴅ ʟᴇᴋᴇ ᴀᴘɴɪ ʙʜᴀᴀɢ ᴊᴀ 😁
 
 ➲ 24*7 ᴄʜᴏᴅᴜɴɢᴀᴀ ʙʜᴀᴀɢ ᴊᴀᴀ 😮‍💨✰
 
 ► ᴍᴜᴍᴍʏ ᴋᴇ ɴᴜᴅᴇs ʙʜᴊ ᴘʜʟᴇ 🌚
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("🌷ＡＤＤ ＭＥ🌷", url=f"https://t.me/Ridi_music_bot?startgroup=true")
        ],
        [
          InlineKeyboardButton("🪐ＧＲＯＵＰ🪐", url="https://t.me/thala_elclassico_07"),
          InlineKeyboardButton("⚡ＤＡＤＤＹ⚡", url="https://t.me/ll_destroyerrll"),
          ],
               [
                InlineKeyboardButton("𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓"),

],
[
              InlineKeyboardButton("𝐒𝐔𝐀𝐑𝐑𝐑"),
              InlineKeyboardButton("︎𝐑𝐀𝐍𝐃𝐈𝐈𝐈"),
              ],
              [
              InlineKeyboardButton("𝐆𝐀𝐍𝐃 𝐃𝐄"),
InlineKeyboardButton("𝐋𝐀𝐔𝐑𝐄𝐄𝐄𝐄 "),
],
[
InlineKeyboardButton("𝐁𝐄𝐇𝐀𝐍 𝐊𝐄 𝐋𝐔𝐍𝐃"),
InlineKeyboardButton("𝐋𝐔𝐍𝐃 𝐋𝐄𝐋𝐄"),
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/3093023b954815189d472.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
   
# --------------


@app.on_message(filters.command("repo", prefixes="."))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("KHUD KA MAAALIK HU KHUD HU LAUREE 🤣")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[REPO LINK](@ll_destroyerr_ll ᴋᴏ ʙᴀᴀᴘ ʙᴏʟ ᴘʜʟᴇ 🌚| [𝖦𝖱𝖮𝖴𝖯](https://t.me/thala_elclassico_07)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")
