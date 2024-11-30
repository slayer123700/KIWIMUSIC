import random
from pyrogram import Client, filters
from PURVIMUSIC import app
from pyrogram.types import Message
from pyrogram.enums import ChatAction
from pymongo import MongoClient
from config import BOT_USERNAME

MONGO_DB_URI = "mongodb+srv://teamdaxx123:teamdaxx123@cluster0.ysbpgcp.mongodb.net/?retryWrites=true&w=majority"
# MongoDB Initialization
mongo_client = MongoClient(MONGO_DB_URI)
chatbot_db = mongo_client["VickDb"]["Vick"]  # Disabled chatbot chats
word_db = mongo_client["Word"]["WordDb"]     # Word-response pairs

# Helper function to check if a user is an admin
async def is_admin(chat_id, user_id):
    member = await app.get_chat_member(chat_id, user_id)
    return member.status in ("administrator", "creator")

# Command to disable the chatbot
@app.on_message(filters.command(["chatbot off", f"chatbot@{BOT_USERNAME} off"], prefixes=["/"]) & ~filters.private)
async def chatbot_off(client, message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    if not await is_admin(chat_id, user_id):
        return await message.reply_text("You are not an admin!")

    if not chatbot_db.find_one({"chat_id": chat_id}):
        chatbot_db.insert_one({"chat_id": chat_id})
        await message.reply_text("Chatbot Disabled!")
    else:
        await message.reply_text("Chatbot is already disabled.")

# Command to enable the chatbot
@app.on_message(filters.command(["chatbot on", f"chatbot@{BOT_USERNAME} on"], prefixes=["/"]) & ~filters.private)
async def chatbot_on(client, message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    if not await is_admin(chat_id, user_id):
        return await message.reply_text("You are not an admin!")

    if chatbot_db.find_one({"chat_id": chat_id}):
        chatbot_db.delete_one({"chat_id": chat_id})
        await message.reply_text("Chatbot Enabled!")
    else:
        await message.reply_text("Chatbot is already enabled.")

# Command to display chatbot usage
@app.on_message(filters.command(["chatbot", f"chatbot@{BOT_USERNAME}"], prefixes=["/"]) & ~filters.private)
async def chatbot_usage(client, message: Message):
    await message.reply_text("**Usage:**\n`/chatbot [on/off]`\nChatbot commands only work in groups.")

# Chatbot responder for group chats
@app.on_message((filters.text | filters.sticker) & ~filters.private & ~filters.bot)
async def chatbot_responder(client: Client, message: Message):
    chat_id = message.chat.id

    if chatbot_db.find_one({"chat_id": chat_id}):
        return

    await app.send_chat_action(chat_id, ChatAction.TYPING)

    if not message.reply_to_message:
        responses = list(word_db.find({"word": message.text}))
        if responses:
            response = random.choice(responses)
            if response["check"] == "sticker":
                await message.reply_sticker(response["text"])
            else:
                await message.reply_text(response["text"])
    else:
        reply = message.reply_to_message
        if reply.from_user.id == (await app.get_me()).id:
            responses = list(word_db.find({"word": message.text}))
            if responses:
                response = random.choice(responses)
                if response["check"] == "sticker":
                    await message.reply_sticker(response["text"])
                else:
                    await message.reply_text(response["text"])
        else:
            if message.text:
                word_db.insert_one({"word": reply.text, "text": message.text, "check": "text"})
            elif message.sticker:
                word_db.insert_one({"word": reply.text, "text": message.sticker.file_id, "check": "sticker"})

# Chatbot responder for private chats
@app.on_message((filters.text | filters.sticker) & filters.private & ~filters.bot)
async def chatbot_private(client: Client, message: Message):
    await app.send_chat_action(message.chat.id, ChatAction.TYPING)

    if not message.reply_to_message:
        responses = list(word_db.find({"word": message.text}))
        if responses:
            response = random.choice(responses)
            if response["check"] == "sticker":
                await message.reply_sticker(response["text"])
            else:
                await message.reply_text(response["text"])
    else:
        reply = message.reply_to_message
        if reply.from_user.id == (await app.get_me()).id:
            responses = list(word_db.find({"word": message.text}))
            if responses:
                response = random.choice(responses)
                if response["check"] == "sticker":
                    await message.reply_sticker(response["text"])
                else:
                    await message.reply_text(response["text"])
        else:
            if message.text:
                word_db.insert_one({"word": reply.text, "text": message.text, "check": "text"})
            elif message.sticker:
                word_db.insert_one({"word": reply.text, "text": message.sticker.file_id, "check": "sticker"})
