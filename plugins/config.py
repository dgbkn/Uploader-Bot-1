import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = "5147335730:AAECZFZqCyKi3b_mxAsiVQU0sVgnu-AwAbI"
    # The Telegram API things
    APP_ID = 5459324
    API_HASH = "e41463b86cc9ef692b65489e665b0cc4"
    # Get these values from my.telegram.org
    # Banned Unwanted Members..
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "")
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
 
    # watermark file
    DEF_WATER_MARK_FILE = ""
    # your telegram id
    OWNER_ID = "1284483178"
    # Update channel for Force Subscribe
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
    # database session name, example: xurluploader
    SESSION_NAME = "TELLYuploader"
    # database uri (mongodb)
    DATABASE_URL = "mongodb+srv://devbkn:%40Anu123456@cluster0.31qt4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    
    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "0").split()))
    PRO_USERS.append(OWNER_ID)
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-100"))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096

    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    
    # dict to hold the ReQuest queue
    ADL_BOT_RQ = {}
