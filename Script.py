class script(object):
    
    START_TXT = """<b>ʜᴇʏ {}, <i>{}</i>
    
<blockquote>ɪ ᴀᴍ ᴘᴏᴡᴇʀғᴜʟ ᴀᴜᴛᴏ ғɪʟᴛᴇʀ ᴡɪᴛʜ ʟɪɴᴋ sʜᴏʀᴛᴇɴᴇʀ ʙᴏᴛ. ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴀꜱ ᴀᴜᴛᴏ ғɪʟᴛᴇʀ ᴡɪᴛʜ ʟɪɴᴋ sʜᴏʀᴛᴇɴᴇʀ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ... ɪᴛ'ꜱ ᴇᴀꜱʏ ᴛᴏ ᴜꜱᴇ ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴀꜱ ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ɪ ᴡɪʟʟ ᴘʀᴏᴠɪᴅᴇ ᴛʜᴇʀᴇ ᴍᴏᴠɪᴇꜱ ᴡɪᴛʜ ʏᴏᴜʀ ʟɪɴᴋ ꜱʜᴏʀᴛᴇɴᴇʀ... ♻️</blockquote></b>"""

    MY_ABOUT_TXT = """⪼ ꜱᴇʀᴠᴇʀ: <a href=https://www.koyeb.com>ᴋᴏʏᴇʙ</a>
⪼ ᴅᴀᴛᴀʙᴀꜱᴇ: <a href=https://www.mongodb.com>ᴍᴏɴɢᴏᴅʙ</a>
⪼ ʟᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>ᴘʏᴛʜᴏɴ</a>
⪼ ʟɪʙʀᴀʀʏ: <a href=https://pyrogram.org>ᴘʏʀᴏɢʀᴀᴍ</a>"""

    MY_OWNER_TXT = """★ Name: Bloody Sweet
⪼ Username: @KR_Movie2"""

    STATUS_TXT = """<b>╭━━━━━━━━━━❰sᴛᴀᴛᴜs ʙᴀʀ❱══❍⊱❁۪۪
 ⪼ 📁 ᴛᴏᴛᴀʟ ꜰɪʟᴇs: <code>{}</code>
 ⪼ 👥 ᴛᴏᴛᴀʟ ᴜsᴇʀs: <code>{}</code>
 ⪼ 🧧 ᴘʀᴇᴍɪᴜᴍ ᴜsᴇʀs: <code>{}<code>
 ⪼ ♻️ ᴛᴏᴛᴀʟ ᴄʜᴀᴛs: <code>{}</code>
 ⪼ ✨ ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ: <code>{}</code>
 ⪼ 🆓 ꜰʀᴇᴇ sᴛᴏʀᴀɢᴇ: <code>{}</code></b>"""

    NEW_GROUP_TXT = """#NewGroup
›Title - {}
›ID - <code>{}</code>
›Username - {}
›Total - <code>{}</code>"""

    NEW_USER_TXT = """#NewUser
›Name: {}
›ID: <code>{}</code>"""

    NOT_FILE_TXT = """👋 Hello {},

<blockquote>ɪ ᴄᴀɴ'ᴛ ꜰɪɴᴅ ᴛʜᴇ <b>{}</b> ɪɴ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ!</blockquote>

👉 ꜱᴇᴀʀᴄʜ ᴏɴ ɢᴏᴏɢʟᴇ ᴀɴᴅ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ꜱᴩᴇʟʟɪɴɢ.
👉 ᴩʟᴇᴀꜱᴇ ʀᴇᴀᴅ ᴛʜᴇ ɪɴꜱᴛʀᴜᴄᴛɪᴏɴꜱ ᴛᴏ ɢᴇᴛ ʙᴇᴛᴛᴇʀ ʀᴇꜱᴜʟᴛꜱ.
👉 ᴄʜᴇᴄᴋ ᴛʜᴇ ᴍᴏᴠɪᴇ ʀᴇʟᴇᴀꜱᴇ ᴅᴀᴛᴇ.
👉ʀᴇᴩᴏʀᴛ @Blody_sweet_bot ɪꜰ ʏᴏᴜ ᴅᴏɴ'ᴛ ꜰɪɴᴅ."""
    
    EARN_TXT = """<b>ʜᴏᴡ ᴛᴏ ᴇᴀʀɴ ꜰʀᴏᴍ ᴛʜɪs ʙᴏᴛ

➥ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴇᴀʀɴ ᴍᴏɴᴇʏ ʙʏ ᴜsɪɴɢ ᴛʜɪꜱ ʙᴏᴛ.

» sᴛᴇᴘ 1:- ғɪʀsᴛ ʏᴏᴜ ʜᴀᴠᴇ ᴛᴏ ᴀᴅᴅ ᴛʜɪs ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ᴀᴅᴍɪɴ ᴘᴇʀᴍɪssɪᴏɴ.

» sᴛᴇᴘ 2:- ᴍᴀᴋᴇ ᴀᴄᴄᴏᴜɴᴛ ᴏɴ <a href=https://mdiskshortner.link/ref/104594076436939082113>ᴍᴅɪꜱᴋꜱʜᴏʀᴛɴᴇʀ.ɴᴇᴛ</a> [ ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴜsᴇ ᴏᴛʜᴇʀ sʜᴏʀᴛɴᴇʀ ᴡᴇʙsɪᴛᴇ ]

» sᴛᴇᴘ 3:- ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴇʟᴏᴡ ɢɪᴠᴇɴ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ sʜᴏʀᴛɴᴇʀ ᴡɪᴛʜ ᴛʜɪs ʙᴏᴛ.

➥ ᴛʜɪꜱ ʙᴏᴛ ɪs ꜰʀᴇᴇ ꜰᴏʀ ᴀʟʟ, ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘs ғᴏʀ ꜰʀᴇᴇ ᴏꜰ ᴄᴏꜱᴛ.</b>"""

    HOW_TXT = """<b>ʜᴏᴡ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ᴏᴡɴ sʜᴏʀᴛɴᴇʀ ‼️

➥ ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ᴏᴡɴ sʜᴏʀᴛɴᴇʀ ᴛʜᴇɴ ᴊᴜsᴛ sᴇɴᴅ ᴛʜᴇ ɢɪᴠᴇɴ ᴅᴇᴛᴀɪʟs ɪɴ ᴄᴏʀʀᴇᴄᴛ ꜰᴏʀᴍᴀᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ

➥ ғᴏʀᴍᴀᴛ ↓↓↓

<code>/set_shortlink sʜᴏʀᴛɴᴇʀ sɪᴛᴇ sʜᴏʀᴛɴᴇʀ ᴀᴘɪ</code>

➥ ᴇxᴀᴍᴘʟᴇ ↓↓↓

<code>/set_shortlink ᴍᴅɪꜱᴋꜱʜᴏʀᴛɴᴇʀ.net 1cf9ae3a85f3180eb45564a2a47e03f074b47a6a</code>

➥ ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴄʜᴇᴄᴋ ᴡʜɪᴄʜ sʜᴏʀᴛᴇɴᴇʀ ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛʜᴇɴ sᴇɴᴅ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴛʜᴇ ɢʀᴏᴜᴘ /get_shortlink

📝 ɴᴏᴛᴇ:- ʏᴏᴜ sʜᴏᴜʟᴅ ɴᴏᴛ ʙᴇ ᴀɴ ᴀɴᴏɴʏᴍᴏᴜs ᴀᴅᴍɪɴ ɪɴ ɢʀᴏᴜᴘ. sᴇɴᴅ ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜᴏᴜᴛ ʙᴇɪɴɢ ᴀɴ ᴀɴᴏɴʏᴍᴜs ᴀᴅᴍɪɴ.</b>"""



    
    IMDB_TEMPLATE = """✅ I Found: <code>{query}</code>

🏷 ᴛɪᴛʟᴇ: <a href={url}>{title}</a>
🎭 ɢᴇɴʀᴇꜱ: {genres}
📆 ʏᴇᴀʀ: <a href={url}/releaseinfo>{year}</a>
🎙️ ʟᴀɴɢᴜᴀɢᴇ: {languages}
📀 ʀᴜɴᴛɪᴍᴇ: {runtime} Minutes

🗣 ʀᴇǫᴜᴇꜱᴛᴇᴅ ʙʏ: {message.from_user.mention}
©️ ᴘᴏᴡᴇʀᴇᴅ ʙʏ: <b>{message.chat.title}</b>"""

    FILE_CAPTION = """<b>[{file_name}](https://t.me/+NABTLpcBvvU3MGY9)\n\n<b>•────•────────•────•\n📌 ʀᴇǫᴜᴇsᴛ ɢʀᴏᴜᴘ : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/+NABTLpcBvvU3MGY9)\n🎬 ᴍᴏᴠɪᴇs ᴄʜᴀɴɴᴇʟ : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/Kr_Movie2)\n•────•────────•────•\n\n©️ ᴘᴏᴡᴇʀᴇᴅ ʙʏ : [ʙʟᴏᴏᴅʏ ꜱᴡᴇᴇᴛ](https://t.me/TG_BOTS_UPDATE)</b>"</b>

🚫 ᴘʟᴇᴀsᴇ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ᴄʟᴏsᴇ ʙᴜᴛᴛᴏɴ ɪꜰ ʏᴏᴜ ʜᴀᴠᴇ sᴇᴇɴ ᴛʜᴇ ᴍᴏᴠɪᴇ 🚫"""

    WELCOME_TEXT = """👋 Hello {mention}, Welcome to {title} group! 💞"""

    HELP_TXT = """<b>Note - <spoiler>Try each command without any argument to see more details 😹</spoiler></b>"""
    
    ADMIN_COMMAND_TXT = """<b>Here is bot admin commands 👇

/index_channels - to check how many index channel id added
/stats - to get bot status
/delete - to delete files using query
/delete_all - to delete all indexed file
/broadcast - to send message to all bot users
/grp_broadcast - to send message to all groups
/pin_broadcast - to send message as pin to all bot users.
/pin_grp_broadcast - to send message as pin to all groups.
/restart - to restart bot
/leave - to leave your bot from particular group
/unban_grp - to enable group
/ban_grp - to disable group
/ban_user - to ban a users from bot
/unban_user - to unban a users from bot
/users - to get all users details
/chats - to get all groups
/invite_link - to generate invite link
/set_pm_search - to do pm search on/off
/index - to index bot accessible channels</b>
/add_premium - to add user in premium
/remove_premium - to remove user from premium"""
    
    USER_COMMAND_TXT = """<b>Here is bot user commands 👇

/start - to check bot alive or not
/settings - to change group settings as your wish
/set_template - to set custom imdb template
/set_caption - to set custom bot files caption
/set_shortlink - group admin can set custom shortlink
/get_custom_settings - to get your group settings details
/set_welcome - to set custom new joined users welcome message for group
/set_tutorial - to set custom tutorial link in result page button
/id - to check group or channel id
/set_fsub - to set force subscribe channels
/remove_fsub - to remove all force subscribe channel
/openai - Find solution to any question with ChatGPT
/myplan - to check your plan details
/plans - to get plan details</b>"""
    
    SOURCE_TXT = """<b><blockquote>ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ</blockquote></b>"""

    PREMIUM_PLAN_TEXT = """<b><i><u>- ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs - </u>

- 1 ᴡᴇᴇᴋ - 10ʀs 
- 1 ᴍᴏɴᴛʜs - 40ʀs
- 3 ᴍᴏɴᴛʜs - 100ʀs (19% ᴏғғ)
- 6 ᴍᴏɴᴛʜs - 210ʀs (42% ᴏғғ)

<u>🎁 ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇs 🎁</u>

○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪғʏ
○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋ
○ ᴅɪʀᴇᴄᴛ ғɪʟᴇs   
○ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ 
○ ʜɪɢʜ-sᴘᴇᴇᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ                           
○ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs & sᴇʀɪᴇs                                                                         
○ ꜰᴜʟʟ ᴀᴅᴍɪɴ sᴜᴘᴘᴏʀᴛ                              
○ ʀᴇǫᴜᴇsᴛ ᴡɪʟʟ ʙᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ 1ʜ ɪꜰ ᴀᴠᴀɪʟᴀʙʟᴇ   

✨ ᴘᴀʏᴍᴇɴᴛ ɪᴅ - <code>{}</code>

ᴄʟɪᴄᴋ ᴛᴏ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ /myplan

💢 ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ

‼️ ᴀғᴛᴇʀ sᴇɴᴅɪɴɢ ᴀ sᴄʀᴇᴇɴsʜᴏᴛ ᴘʟᴇᴀsᴇ ɢɪᴠᴇ ᴜs sᴏᴍᴇ ᴛɪᴍᴇ ᴛᴏ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴛʜᴇ ᴘʀᴇᴍɪᴜᴍ ʟɪsᴛ</i></b>"""


