import random
from pyrogram import filters
from pymongo import MongoClient
from PURVIMUSIC import app

# MongoDB Connection
from config import MONGO_URL

mongo_client = MongoClient(MONGO_URL)
chatbot_db = mongo_client["VickDb"]["Vick"]  # Collection to store disabled chatbot chats
word_db = mongo_client["Word"]["WordDb"]     # Collection to store word-response pairs

# Command to Disable Chatbot
@app.on_message(filters.command(["chatbot off"]) & ~filters.private)
async def chatbot_off(client, message):
    if not await is_admin(message):
        return await message.reply_text("You are not admin.")
    
    chat_id = message.chat.id
    if not chatbot_db.find_one({"chat_id": chat_id}):
        chatbot_db.insert_one({"chat_id": chat_id})
        await message.reply_text("Chatbot Disabled!")
    else:
        await message.reply_text("Chatbot is already disabled.")

# Command to Enable Chatbot
@app.on_message(filters.command(["chatbot on"]) & ~filters.private)
async def chatbot_on(client, message):
    if not await is_admin(message):
        return await message.reply_text("You are not admin.")
    
    chat_id = message.chat.id
    if chatbot_db.find_one({"chat_id": chat_id}):
        chatbot_db.delete_one({"chat_id": chat_id})
        await message.reply_text("Chatbot Enabled!")
    else:
        await message.reply_text("Chatbot is already enabled.")

# Chatbot Response Handler
@app.on_message((filters.text | filters.sticker) & ~filters.private & ~filters.bot)
async def chatbot_response(client, message):
    chat_id = message.chat.id
    if chatbot_db.find_one({"chat_id": chat_id}):
        return  # If chatbot is disabled, do nothing

    if message.reply_to_message:
        await handle_reply(message)
    else:
        await handle_message(message)

# Helper Function: Check Admin Status
async def is_admin(message):
    user = message.from_user.id
    chat_id = message.chat.id
    member = await app.get_chat_member(chat_id, user)
    return member.status in ["administrator", "creator"]

# Helper Function: Handle Normal Messages
async def handle_message(message):
    text = message.text
    possible_responses = [item["text"] for item in word_db.find({"word": text})]
    if possible_responses:
        response = random.choice(possible_responses)
        is_sticker = word_db.find_one({"text": response})["check"] == "sticker"
        if is_sticker:
            await message.reply_sticker(response)
        else:
            await message.reply_text(response)

# Helper Function: Handle Replies
async def handle_reply(message):
    reply_text = message.reply_to_message.text
    if message.text:
        word_db.insert_one({"word": reply_text, "text": message.text, "check": "none"})
    elif message.sticker:
        word_db.insert_one({"word": reply_text, "text": message.sticker.file_id, "check": "sticker"})
