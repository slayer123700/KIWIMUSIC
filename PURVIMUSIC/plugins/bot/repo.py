from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from PURVIMUSIC import app
from config import BOT_USERNAME
from PURVIMUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
✪ ᴡᴇʟᴄᴏᴍᴇ ғᴏʀ ᴄʜᴜᴅᴀɪ ☠️😂 ✪
 
 ➲ ᴛᴇʀɪ ᴍᴀᴀᴀᴀ ᴋɪ ᴄʜᴜᴛ ᴍᴀɪ ʀᴇᴘᴏ ᴅᴀᴀʟᴅᴜᴜ ᴋɪᴅ 😂 ✰
 
 ➲ ʀᴀɴᴅɪɪ ᴋʜᴜᴅᴋᴀ ʀᴇᴘᴏ ʙɴᴀᴀ 😾💪✰
 
 ➲ ᴛᴇʀɪ ʙᴇʜᴀɴ ᴋɪ ᴄʜᴜᴛ ᴍᴀɪ ᴘʏᴛʜᴏɴ ᴅᴀᴀʟᴅᴜ 🥱✰
 
 ➲ᴜɴʟɪᴍɪᴛᴇᴅ ᴄʜᴜᴅᴀɪɪɪ  ✰
 
 ➲  24x7 ᴛᴍʀʜɪ ᴏʀ ᴛᴍʀʜɪ ᴋʜᴀɴᴅᴀɴ ᴋɪ ᴄʜᴜᴅᴀɪ 😋 ✰
 
 ► ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ sᴇɴᴅ ɴᴜᴅᴇs ᴏғ ᴜʀ ᴍᴏᴛʜᴇʀ
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
             buttons = [
        [ 
          InlineKeyboardButton("𝗔𝗗𝗗 𝗠𝗘", url=f"https://t.me/Ridi_music_bot?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗛𝗘𝗟𝗣", url="https://t.me/thala_elclassico_07"),
          InlineKeyboardButton("𝗢𝗪𝗡𝗘𝗥", url="https://t.me/ll_destroyerr_ll"),
        ]]

            reply_markup = InlineKeyboardMarkup(buttons)
       
    await msg.reply_photo(
        photo="https://telegra.ph/file/17365df54ea493b54f62b.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )


# --------------

@app.on_message(filters.command("repo", prefixes="."))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https//xxx.ᴄᴏᴍ 😂😋💋")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[ɢᴀᴀɴᴅᴜᴜ] | [𝖦𝖱𝖮𝖴𝖯](https://t.me/thala_elclassico_07)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")


