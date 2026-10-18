from os import getenv


def env_int(name, default=None):
    value = getenv(name)
    if value is None or value.strip() == "":
        if default is None:
            raise RuntimeError(f"Missing required environment variable: {name}")
        return int(default)
    return int(value.strip())


def env_int_list(name, default=""):
    value = getenv(name, default).replace(",", " ")
    return [int(x) for x in value.split() if x.strip()]


API_ID = env_int("API_ID")
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
if not API_HASH:
    raise RuntimeError("Missing required environment variable: API_HASH")
if not BOT_TOKEN:
    raise RuntimeError("Missing required environment variable: BOT_TOKEN")

OWNER_ID = env_int_list("OWNER_ID")
MONGO_DB = getenv("MONGO_DB", "")
if not MONGO_DB:
    raise RuntimeError("Missing required environment variable: MONGO_DB")

LOG_GROUP = env_int("LOG_GROUP", 0)
CHANNEL_ID = env_int("CHANNEL_ID", 0)
FREEMIUM_LIMIT = env_int("FREEMIUM_LIMIT", 50)
PREMIUM_LIMIT = env_int("PREMIUM_LIMIT", 1000)
WEBSITE_URL = getenv("WEBSITE_URL", "")
AD_API = getenv("AD_API", "")
STRING = getenv("STRING", "")
DEFAULT_SESSION = getenv("DEFAULT_SESSION", getenv("DEFAUL_SESSION", "")) or None

# Optional cookies. Keep them in hosting environment variables, never in source code.
YT_COOKIES = getenv("YT_COOKIES", "")
INSTA_COOKIES = getenv("INSTA_COOKIES", "")
