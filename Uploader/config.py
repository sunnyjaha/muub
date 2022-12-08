import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):
    # get a token from https://chatbase.com
    CHAT_BASE_TOKEN = os.environ.get("CHAT_BASE_TOKEN", "")
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5691637076:AAHd_g65IUAhs2OW8N3vvKAWuw3P1ZMeAHc")
    # The Telegram API things
    API_ID = int(os.environ.get("API_ID", "15939361"))
    API_HASH = os.environ.get("API_HASH", "f8beb0bd0054a717d84fbe9be12a23ea")
    # Get these values from my.telegram.org
    # Array to store users who are authorized to use the bot

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    # Update channel for Force Subscribe
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "-1001744824600")
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 4194304000
    TG_MAX_FILE_SIZE = 4194304000
    FREE_USER_MAX_FILE_SIZE = 4194304000

    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "")
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    # https://t.me/hevcbay/951
    OUO_IO_API_KEY = ""
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprcess
    PROCESS_MAX_TIMEOUT = 300
    # watermark file
    DEF_WATER_MARK_FILE = ""
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://mdisk:mdisk@cluster0.fdrl77f.mongodb.net/?retryWrites=true&w=majority")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Uploader-Bot")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001527701055"))
    LOGGER = logging
    OWNER_ID = int(os.environ.get("OWNER_ID", "5543917190"))
    # Update channel for Force Subscribe
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001744824600")
    TG_MIN_FILE_SIZE = 2097152000
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "UrlUploaderAmrobot")
    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "5543917190 5627748290").split()))
    PRO_USERS.append(OWNER_ID)
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
    BYPASS = os.environ.get("BYPASS", "True")
    ADL_BOT_RQ = {}
    AUTH_USERS = list(set(int(x) for x in os.environ.get("AUTH_USERS", "5627748290 5543917190").split()))
    AUTH_USERS.append(OWNER_ID)
