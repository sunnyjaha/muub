from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
ð Há´Ê {} â¡

I á´á´ á´á´Êá´É¢Êá´á´ á´á´sá´ á´á´á´¡á´ÊÒá´Ê á´ÊÊ á´á´Êá´á´á´á´Ê Êá´á´

Usá´ Êá´Êá´ Êá´á´á´á´É´ á´á´ á´É´á´á´¡ Êá´á´¡ á´á´ á´sá´ á´á´

ððððððððð ÊÊ : [ðð-ð¡ðððð£ð¢ ê²](https://t.me/AmRobots_Bots)
"""
    HELP_TEXT = """
ÊÉªÉ´á´ á´á´ á´á´á´Éªá´ á´Ê ÒÉªÊá´

â  sá´É´á´ á´ ÊÉªÉ´á´ Òá´Ê á´á´Êá´á´á´ á´á´ á´á´Êá´É¢Êá´á´ ÒÉªÊá´ á´Ê á´á´á´Éªá´.

sá´á´ á´Êá´á´ÊÉ´á´ÉªÊ

â  sá´É´á´ á´ á´Êá´á´á´ á´á´ á´á´á´á´ Éªá´ á´s á´á´Êá´á´É´á´É´á´ á´Êá´á´ÊÉ´á´ÉªÊ.

á´á´Êá´á´ÉªÉ´É¢ á´Êá´á´ÊÉ´á´ÉªÊ

â  sá´É´á´ /delthumb á´á´ á´á´Êá´á´á´ á´Êá´á´ÊÉ´á´ÉªÊ.

sá´á´á´ÉªÉ´É¢s

â  á´á´É´ÒÉªÉ¢á´Êá´ á´Ê sá´á´á´ÉªÉ´É¢s á´á´ á´Êá´É´É¢á´ á´á´Êá´á´á´ á´á´á´á´

sÊá´á´¡ á´Êá´á´ÊÉ´á´ÉªÊ

â  sá´É´á´ /showthumb á´á´ á´ Éªá´á´¡ á´á´sá´á´á´ á´Êá´á´ÊÉ´á´ÉªÊ.

ððððððððð ÊÊ : [ðð-ð¡ðððð£ð¢ ê²](https://t.me/AmRobots_Bots)
 
"""
    ABOUT_TEXT = """
**MÊ É´á´á´á´** : [á´á´Êá´á´á´á´Ê Êá´á´](http://t.me/UrlUploaderAmrobot)

**CÊá´É´É´á´Ê** : [ðð-ð¡ðððð£ð¢](https://t.me/AmRobots_Bots)

**Vá´Êê±Éªá´É´** : [2.0 Êá´á´á´](https://t.me/AmRobots_Bots)

**Sá´á´Êá´á´** : [á´ÊÉªá´á´ Êá´Êá´](https://t.me/AM_ROBOTS)

**Sá´Êá´ á´Ê** : [ðð-ð¡ðððð£ð¢ ê²](https://youtube.com/@AMROBOTS)

**Lá´É´É¢á´á´É¢á´ :** [PÊá´Êá´É´ 3.10.2](https://www.python.org/)

**FÊá´á´á´á´¡á´Êá´ :** [á´ÊÊá´É¢á´á´ 2.0.30](https://docs.pyrogram.org/)

**Dá´á´ á´Êá´á´á´Ê :** [ðð-ð¡ðððð£ð¢ ê²](https://t.me/AM_ROBOTS)

**ððððððððð ÊÊ** : [ðð-ð¡ðððð£ð¢ ê²](https://t.me/AmRobots_Bots)

"""


    PROGRESS = """
ð° Sá´á´á´á´ : {3}/s\n\n
ð Dá´É´á´ : {1}\n\n
ð¥ Tá´á´á´Ê sÉªá´¢á´  : {2}\n\n
â³ TÉªá´á´ Êá´Òá´ : {4}\n\n
"""
    ID_TEXT = """
ð Your Telegram ID ð¢ð¬ :- <code>{}</code> \ð\ðððððððððð ð±ð¢ : @AmRobots_Bots
"""

    INFO_TEXT = """

 ð¤¹ First Name : <b>{}</b>

 ð´ââï¸ Second Name : <b>{}</b>

 ð§ð»âð Username : <b>@{}</b>

 ð Telegram Id : <code>{}</code>

 ð Profile Link : <b>{}</b>

 ð¡ Dc : <b>{}</b>

 ð Language : <b>{}</b>

 ð² Status : <b>{}</b>
"""

    PLANS = """ð¸ â¹50/Month or 1$/Month for Premium User 
No download Limits & No Time Limits.

Buy Subscription from @AM_ROBOTS.

ðððð ðððð bot like ðððð? ð³ð¼ - @AM_ROBOTS

You can donate any amount to keep this service alive & free - @AmRobots_About

"""

    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('ðï¸ sá´á´á´ÉªÉ´É¢s', callback_data='OpenSettings')
        ],[
        InlineKeyboardButton('â Êá´Êá´', callback_data='help'),
        InlineKeyboardButton('ð¨âð á´Êá´á´á´', callback_data='about')
        ],[
        InlineKeyboardButton('â¨ï¸ á´Êá´sá´', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('ð¡ Êá´á´á´', callback_data='home'),
        InlineKeyboardButton('ð¨âð á´Êá´á´á´', callback_data='about')
        ],[
        InlineKeyboardButton('â¨ï¸ á´Êá´sá´', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('ð¡ Êá´á´á´', callback_data='home'),
        InlineKeyboardButton('â Êá´Êá´', callback_data='help')
        ],[
        InlineKeyboardButton('â¨ï¸ á´Êá´sá´', callback_data='close')
        ]]
    )
    BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('â¨ï¸ á´Êá´sá´', callback_data='close')
        ]]
    )
    TEXT = "sá´É´á´ á´á´ á´É´Ê á´á´sá´á´á´ á´Êá´á´ÊÉ´á´ÉªÊ á´á´ sá´á´ Éªá´ \ð\ðððððððððð ð±ð¢ : @AmRobots_Bots"
    IFLONG_FILE_NAME = " Only 64 characters can be named .  \ð\ðððððððððð ð±ð¢ : @AmRobots_Bots"
    RENAME_403_ERR = "Sorry. You are not permitted to rename this file."
    ABS_TEXT = " Please don't be selfish."
    UPGRADE_TEXT = "<b>No preminum plans available in this bot </b>  /help for Details"
    FORMAT_SELECTION = "Ná´á´¡ Sá´Êá´á´á´ TÊá´ Dá´sÉªÊá´á´ Fá´Êá´á´á´ á´Ê FÉªÊá´ ðï¸ SÉªá´¢á´ á´á´ Uá´Êá´á´á´"
    SET_CUSTOM_USERNAME_PASSWORD = """"""
    NOYES_URL = "@robot URL detected. Please send me a fast URL so that I can upload to Telegram, without me slowing down for other users. \ð\ðððððððððð ð±ð¢ : @AmRobots_Bots"
    DOWNLOAD_FILE = "ð¥ Downloading  File "
    UPLOAD_FILE = " UploadinG ð¤ \n\n To  transfer.sh \ð\ð ððððððððð ð±ð¢ : @AmRobots_Bots"
    ANNO_UPLOAD = " UploadinGð¤ \n\n To  anonfiles.com \ð\ð ððððððððð ð±ð¢ : @AmRobots_Bots"
    BAY_UPLOAD = " UploadinGð¤ \n\n To  bayfiles.com \ð\ð ððððððððð ð±ð¢ : @AmRobots_Bots"
    GO_FILE_UPLOAD = " ð¤UploadinGð¤ \n\n To  gofile.io "
    DOWNLOAD_START = "á´ÊÊÉªÉ´É¢ á´á´ á´á´á´¡É´Êá´á´á´ â ððððððððð ð±ð¢ : @AmRobots_Bots\n\nð®ð¸ <i>{} ð®ð¸</i>"
    UPLOAD_START = "ð¤ Uá´Êá´á´á´ÉªÉ´É¢ PÊá´á´sá´ Wá´Éªá´ ððððððððð ð±ð¢ : @AmRobots_Bots"
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 2GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG = " JOIN : https://t.me/AmRobots_Bots\nFor the List of Telegram Bots"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Dá´á´¡É´Êá´á´á´á´á´ ÉªÉ´ {} sá´á´á´É´á´s.\n\nTÊá´É´á´s Fá´Ê UsÉªÉ´É¢ Má´\n\nUá´Êá´á´á´á´á´ ÉªÉ´ {} sá´á´á´É´á´s"
    NOT_AUTH_USER_TEXT = "Please /upgrade your subscription."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Detected File Size: {}. Free Users can only upload: {}\nPlease /upgrade your subscription.\nIf you think this is a bug, please contact <a href='https://telegram.dog/AM_ROBOTS'>@AM_ROBOTS</a>"
    SAVED_CUSTOM_THUMB_NAIL = "Cá´sá´á´á´ á´ Éªá´á´á´ / ÒÉªÊá´ á´Êá´á´ÊÉ´á´ÉªÊ sá´á´ á´á´. TÊÉªs Éªá´á´É¢á´ á´¡ÉªÊÊ Êá´ á´sá´á´ ÉªÉ´ á´Êá´ á´ Éªá´á´á´ / ÒÉªÊá´."
    DEL_ETED_CUSTOM_THUMB_NAIL = "â Cá´sá´á´á´ á´Êá´á´ÊÉ´á´ÉªÊ á´Êá´á´Êá´á´ sá´á´á´á´sÒá´ÊÊÊ"
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "â Media cleared succesfully."
    SAVED_RECVD_DOC_FILE = "Document Downloaded Successfully."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_CUSTOM_THUMB_NAIL_FOUND = "Ná´ á´á´sá´á´á´ á´Êá´á´ÊÉ´á´ÉªÊ Òá´á´É´á´"
    NO_VOID_FORMAT_FOUND = "ERROR... <code>{}</code>"
    FILE_NOT_FOUND = "Error, File not Found!!"
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    SOMETHING_WRONG = "<code>Something Wrong. Try again.</code>"
    REPLY_TO_DOC_GET_LINK = "Reply to a Telegram media to get High Speed Direct Download Link"
    REPLY_TO_DOC_FOR_C2V = "Reply to a Telegram media to convert"
    REPLY_TO_DOC_FOR_SCSS = "Reply to a Telegram media to get screenshots"
    REPLY_TO_DOC_FOR_RENAME_FILE = "Reply to a Telegram media to /ren with custom thumbnail support"
    AFTER_GET_LINK = " <b>File Name :</b> <code>{}</code>\n<b>File Size :</b> {}\n\n<b>â¡Linkâ¡ :</b> <code>{}</code>\n\nJoin : @@AmRobots_Bots"
    AFTER_GET_DL_LINK = " <b>File Name :</b> <code>{}</code>\n<b>File Size :</b> {}\n\n<b>â¡Linkâ¡ :</b> <code>{}</code>\n\nValid for <b>14</b> days.\nJoin : @AmRobots_Bots"
    #AFTER_GET_DL_LINK = " {} valid for 30 or more days.\n\n Join : https://t.me/AmRobots_Bots \n For the list of Telegram bots. "
    AFTER_GET_GOFILE_LINK = " <b>File Name :</b> <code>{}</code>\n<b>File Size :</b> {}\n<b>File MD5 Checksum :</b> <code>{}</code>\n\n<b>â¡Linkâ¡ :</b> <code>{}</code>\n\n Valid untill 10 days of inactivity\nJoin : @AmRobots_Bots"
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """Syntax: /trim HH:MM:SS for screenshot of that specific time."""
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "First send /downloadmedia to any media so that it can be downloaded to my local. \nSend /storageinfo to know the media, that is currently downloaded."
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "Video Duration: {}\nSend /clearffmpegmedia to delete this media, from my storage.\nSend /trim HH:MM:SS [HH:MM:SS] to cu[l]t a small photo / video, from the above media."
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "A saved media already exists. Please send /storageinfo to know the current media details."
    USER_DELETED_FROM_DB = "User <a href='tg://user?id={}'>{}</a> deleted from DataBase."
    REPLY_TO_DOC_OR_LINK_FOR_RARX_SRT = "Reply to a Telegram media (MKV), to extract embedded streams"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
    INVALID_UPLOAD_BOT_URL_FORMAT = "URL format is incorrect. make sure your url starts with either http:// or https://. You can set custom file name using the format link | file_name.extension"
    ABUSIVE_USERS = "You are not allowed to use this bot. If you think this is a mistake, please check /me to remove this restriction."
    FF_MPEG_RO_BOT_AD_VER_TISE_MENT = "Join : https://t.me/sources_cods \n For the list of Telegram bots. "
    EXTRACT_ZIP_INTRO_ONE = "Send a compressed file first, Then reply /unzip command to the file."
    EXTRACT_ZIP_INTRO_THREE = "Analyzing received file. â ï¸ This might take some time. Please be patient. "
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    EXTRACT_ZIP_ERRS_OCCURED = "Sorry. Errors occurred while processing compressed file. Please check everything again twice, and if the issue persists, report this to <a href='https://t.me/AmRobots_Support'>@AmRobots_Support</a>"
    EXTRACT_ZIP_STEP_TWO = """Select file_name to upload from the below options.
You can use /rename command after receiving file to rename it with custom thumbnail support."""
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    FREE_USER_LIMIT_Q_SZE = """Cannot Process Free users only 1 request per 5 min\n
Upgrade your /plans to Remove Time Gaps and For link Processing ððððððððð ð±ð¢ : @AmRobots_Bots"""
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Send me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    FORCE_SUBSCRIBE_TEXT = "<code>Sorry Dear You Must Join My Updates Channel for using me ðð....</code>"
    BANNED_USER_TEXT = "<code>You are Banned!</code> \ð\ðððððððððð ð±ð¢ : @AmRobots_Bots"
    CHECK_LINK = "PÊá´á´á´ssÉªÉ´É¢ Êá´á´Ê ÊÉªÉ´á´ â \ð\ðððððððððð ð±ð¢ : @AmRobots_Bots"

    ADD_CAPTION_HELP = """Select an uploaded file/video or forward me <b>Any Telegram File</b> and just write the text you want to be on the file <b>as a reply to the file</b> and the text you wrote will be attached as the caption! ð¤©
    
Ex: <a href='https://telegra.ph/file/68259e3c723b935e22e69.jpg'>See This!</a> ð"""
