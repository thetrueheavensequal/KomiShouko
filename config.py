import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
class Config(object):
    log = True
    APP_ID = getenv("API_ID", "21927988")
    API_HASH = getenv("API_HASH", "e18f720acdff1e5b0ec80616aecd8a5a")
    TOKEN = getenv("TOKEN", "5932946559:AAER2ptdYl_5tQOM9ff0rOK0cAthvG4RC_M")
    OWNER_ID = getenv("OWNER_ID", "2064735436")
    ASSISTANT_ID = getenv("ASSISTANT_ID", "5743885958")
    STRING_SESSION = getenv("STRING_SESSION", "1BVtsOIUBu0PNRMZXjhxr88j3FHyty78hCA2l7Kw3RWEY1B17z3mmH0jpaULuHqbVLSzE8LNyiYoj2DQ8J6O8dUj1dU-lILLQVhtBSr_VOmdppX9e2Ai3JDucwtSU8X60bOkQdXJwMnJSHSjFcmWh120iqifJwYJzN4Xk0feSAgEzmHvAzaT4z38u8T14mq8mzNQPvPrn6XAHRPqE11d5MWuwn-8Jxdr0wH3AEo8UhNj_OW4sm0IKT_R8SYcJFWVmP4Qq0L8DiJGLpKIkupr6jfuBh4OJNHDdCUVeiBeEAMKmKNU-HLClq1bY4f7kmiNd3QddO7po7eCDEugLUzIEby380AFWtM4=") #telethon
    OWNER_USERNAME = getenv("OWNER_USERNAME", "plumblossomsword")
    DB_URI = getenv("DATABASE_URL", "postgres://Komi:#Strongpass0@postgres-117945-0.cloudclusters.net:11931/telegram")
    DB_URI = DB_URI.replace("postgres", "postgresql")
    MESSAGE_DUMP = getenv("MESSAGE_DUMP", "-1001838981105")
    GBAN_LOGS = getenv("GBAN_LOGS", "-1001838981105")
    SYS_ADMIN = getenv("SYS_ADMIN", "2064735436")
    DEV_USERS = getenv("DEV_USERS", "2064735436")
    LOAD = getenv("LOAD")
    WEBHOOK = False
    SPB_MODE = True
    DROP_UPDATES = False
    DEBUG = False
    URL = None
    INFOPIC = True
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    BAN_STICKER = getenv("BAN_STICKER", "CAACAgUAAx0CakC87QACK3lkIYLpM3hLni092TT6A8J8mEu3PAACtwgAAlIl0VT9IuTRAoPKPi8E")
    ALLOW_EXCL = True
    CUSTOM_CMD = False
    CHANNEL = getenv("CHANNEL", "WalhallaBots")
    SUPPORT = getenv("SUPPORT", "theoneandonlymurim")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/26b93e0b47b609d0759c8.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://graph.org/file/24d9f01abdfc05a006d98.jpg")
    CASH_API_KEY = getenv("CASH_API_KEY", "6HZ09C7DZYKWBCCE")
    TIME_API_KEY = getenv("TIME_API_KEY", "4ID9HHBVU5L8")
    WALL_API = getenv("WALL_API", "")
    spamwatch_api = getenv("spamwatch_api", "zKSTO8g_x3qmaMrU_tiTRXibTb532qbmTKXYW3RdyW8Pq0qk1oEtqddo7HqxRp~1")
    SPAMMERS = getenv("SPAMMERS", "")
    LASTFM_API_KEY = getenv("LASTFM_API_KEY", "0d539c421f45b82acb2576954de8a74a")
    CF_API_KEY = getenv("CF_API_KEY", "")
    BOT_API_URL = getenv("BOT_API_URL", "https://api.telegram.org/bot")
    BOT_API_FILE_URL = getenv("BOT_API_FILE_URL", "https://api.telegram.org/file/bot")
    SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6124970729 5743885958 1967847517").split()))
    ZAID_USER = list(map(int, getenv("DEV_USERS", "2064735436").split()))
    NO_LOAD = list(map(int, getenv("NO_LOAD", "").split()))
