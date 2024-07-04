from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "13279715"
# -------------------------------------------------------------
API_HASH = "56e198053932ecf216af72a2ddffcd78"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = getenv("OWNER_ID", "6407024039")
SUPPORT_GRP = "officialbigdaddy07"
UPDATE_CHNL = "officialbigdaddy07"
OWNER_USERNAME = "ll_SANKI_XD"

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
