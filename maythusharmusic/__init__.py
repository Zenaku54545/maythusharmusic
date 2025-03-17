from maythusharmusic.core.bot import Hotty
from maythusharmusic.core.dir import dirr
from maythusharmusic.core.git import git
from maythusharmusic.core.userbot import Userbot
from maythusharmusic.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Hotty()
userbot = Userbot()
api = SafoneAPI()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

APP = "BRANDED_KUDI_BOT"  # connect music api key "Dont change it"
