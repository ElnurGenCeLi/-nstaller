from telethon.tl.functions.channels import EditPhotoRequest, CreateChannelRequest
from .language import LANG, COUNTRY, LANGUAGE, TZ
from telethon import TelegramClient, functions
from telethon.sessions import StringSession
from rich.prompt import Prompt, Confirm
from asyncio import get_event_loop
from bozqurd_installer import *
from .astring import main
from time import time
from . import console
from git import Repo
import requests
import heroku3
import base64
import random
import os

LANG = LANG['MAIN']
Client = None

def connect (api):
    heroku_conn = heroku3.from_key(api)
    try:
        heroku_conn.apps()
    except:
        hata(LANG['INVALID_KEY'])
        exit(1)
    return heroku_conn

def createApp (connect):
    appname = "bozqurd" + str(time() * 1000)[-4:].replace(".", "") + str(random.randint(0,500))
    try:
        connect.create_app(name=appname, stack_id_or_name='container', region_id_or_name="eu")
    except requests.exceptions.HTTPError:
        hata(LANG['MOST_APP'])
        exit(1)
    return appname

def hgit (connect, repo, appname):
    global api
    app = connect.apps()[appname]
    giturl = app.git_url.replace(
            "https://", "https://api:" + api + "@")

    if "heroku" in repo.remotes:
        remote = repo.remote("heroku")
        remote.set_url(giturl)
    else:
        remote = repo.create_remote("heroku", giturl)
    try:
        remote.push(refspec="HEAD:refs/heads/master", force=True)
    except Exception as e:
        hata(LANG['ERROR'] + str(e))

    bilgi(LANG['POSTGRE'])
    app.install_addon(plan_id_or_name='062a1cc7-f79f-404c-9f91-135f70175577', config={})
    basarili(LANG['SUCCESS_POSTGRE'])
    return app

async def oturumacvebotlogolustur (stri, aid, ahash):
    try:
        Client = TelegramClient(StringSession(stri), aid, ahash)
        await Client.start()
        ms = await Client.send_message('me',LANG['BOZQURDUSERBOT'])
        KanalId = await Client(CreateChannelRequest(
            title='BozQurd BotLog',
            about=LANG['AUTO_BOTLOG'],
            megagroup=True
        ))

        KanalId = KanalId.chats[0].id

        Photo = await Client.upload_file(file='bozqurd.jpg')
        await Client(EditPhotoRequest(channel=KanalId, 
            photo=Photo))
        msg = await Client.send_message(KanalId, LANG['DONT_LEAVE'])
        await msg.pin()

        KanalId = str(KanalId)
        if "-100" in KanalId:
            return KanalId
        else:
            return "-100" + KanalId
    except:
        KanalId = 'err'
        return KanalId

if __name__ == "__main__":
    logo(LANGUAGE)
    loop = get_event_loop()
    api = soru(LANG['HEROKU_KEY'])
    bilgi(LANG['HEROKU_KEY_LOGIN'])
    heroku = connect(api)
    basarili(LANG['LOGGED'])

    # Telegram #
    onemli(LANG['GETTING_STRING_SESSION'])
    stri, aid, ahash = main()
    basarili(LANG['SUCCESS_STRING'])
    baslangic = time()


    # BozQurd Auto Deployer Heroku #
    # 📡
    bilgi(LANG['CREATING_APP'])
    appname = createApp(heroku)
    basarili(LANG['SUCCESS_APP'])
    onemli(LANG['DOWNLOADING'])
    #
    # utf8 = aykhan_s.decode("sifre1")
    # 🖕
    # Bax bax doyunca bax)))🤠
    # Kopyalayan Peysərdi...!!!
    # 🤯
    sifre1 = b"\x68\x74\x74\x70\x73\x3A\x2F\x2F\x67\x69\x74\x68\x75\x62\x2E\x63\x6F\x6D\x2F\x61\x79\x6B\x68\x61\x6E\x30\x32\x36\x2F\x42\x6F\x7A\x51\x75\x72\x64\x55\x73\x65\x72\x42\x6F\x74"
    sifre2 = b"\x2E\x2F\x42\x6F\x7A\x51\x75\x72\x64\x55\x73\x65\x72\x42\x6F\x74\x2F"
    sifre3 = b"\x62\x72\x61\x6E\x63\x68\x3D\x22\x6D\x61\x69\x6E\x22"
    sifre4 = b"\x41\x20\x67\x69\x6A\x64\xC4\xB1\x6C\x6C\x61\x78\x20\x67\x65\x72\x65\x6B\x20\x61\x67\x69\x72\x20\x73\x6F\x79\x75\x73\x20\x71\x6F\x79\x75\x6D\x20\x62\x75\x72\x61\x20\x3F\x20\xF0\x9F\x98\x82\x20\x61\xC3\xA7\x6D\x61\x64\x61\x20\x62\x6C\x65\x74\x20\x6E\x61\x78\x75\x79"
    installer_sifrelenib = sifre1.decode("utf8")
    aykhan_s = sifre2.decode("utf8") # 😈
    branch = sifre3.decode("utf8") # 😱
    soyus_var = sifre4.decode("utf8") # 🤫
    if os.path.isdir("aykhan_s"): # 😳
        rm_r("aykhan_s") # 😎
    repo = Repo.clone_from(installer_sifrelenib,"aykhan_s", branch="master")
    onemli(LANG['DEPLOYING'])
    app = hgit(heroku, repo, appname)
    config = app.config()

    onemli(LANG['WRITING_CONFIG'])

    config['ANTI_SPAMBOT'] = 'False'
    config['ANTI_SPAMBOT_SHOUT'] = 'True'
    config['API_HASH'] = ahash
    config['API_KEY'] = str(aid)
    config['BOTLOG'] = "False"
    config['BOTLOG_CHATID'] = "0"
    config['CLEAN_WELCOME'] = "True"
    config['CONSOLE_LOGGER_VERBOSE'] = "False"
    config['COUNTRY'] = COUNTRY
    config['DEFAULT_BIO'] = "🐺 @BozQurdUserBot"
    config['DEFAULT_NAME'] = "Sahib"
    config['LANGUAGE'] = LANGUAGE
    config['GALERI_SURE'] = "60"
    config['CHROME_DRIVER'] = "/usr/sbin/chromedriver"
    config['GOOGLE_CHROME_BIN'] = "/usr/sbin/chromium"
    config['HEROKU_APIKEY'] = api
    config['HEROKU_APPNAME'] = appname
    config['STRING_SESSION'] = stri
    config['HEROKU_MEMEZ'] = "True"
    config['LOGSPAMMER'] = "False"
    config['PM_AUTO_BAN'] = "False"
    config['PM_AUTO_BAN_LIMIT'] = "4"
    config['TMP_DOWNLOAD_DIRECTORY'] = "./downloads/"
    config['TZ'] = TZ
    config['TZ_NUMBER'] = "1"
    config['UPSTREAM_REPO_URL'] = "https://github.com/aykhan026/bozqurduserbot"
    config['SEVGILI'] = "None"
    config['WARN_LIMIT'] = "3"
    config['WARN_MODE'] = "gmute"

    basarili(LANG['SUCCESS_CONFIG'])
    bilgi(LANG['OPENING_DYNO'])

    try:
        app.process_formation()["worker"].scale(1)
    except:
        hata(LANG['ERROR_DYNO'])
        exit(1)

    basarili(LANG['OPENED_DYNO'])
    basarili(LANG['SUCCESS_DEPLOY'])
    tamamlandi(time() - baslangic)
    KanalId = loop.run_until_complete(oturumacvebotlogolustur(stri, aid, ahash))

    if KanalId != 'err':
        basarili(LANG['OPENED_BOTLOG'])
        config['BOTLOG'] = "True"
        config['BOTLOG_CHATID'] = KanalId

    Sonra = Confirm.ask(f"[bold yellow]{LANG['AFTERDEPLOY']}[/]", default=True)
    if Sonra == True:
        console.clear()
        Cevap = ""
        while not Cevap == "5":
            if Cevap == "2":
                config['LOGSPAMMER'] = "True"
                basarili(LANG['SUCCESS_LOG'])
            elif Cevap == "1":
                config['OTOMATIK_KATILMA'] = "False"
                basarili(LANG['SUCCESS_SUP'])
            elif Cevap == "3":
                config['PM_AUTO_BAN'] = "True"
                basarili(LANG['SUCCESS_PMAUTO'])
            elif Cevap == "4":
                whatisyourname = str(soru(LANG['WHAT_IS_YOUR_NAME']))
                config['DEFAULT_NAME'] = whatisyourname
                basarili(LANG['SUCCESS_DEFAULTNAME'])

                


            
            bilgi(f"[1] {LANG['NO_SUP']}\n[2] {LANG['NO_LOG']}\n\n[3] {LANG['NO_PMAUTO']}\n\n[4] {LANG['NO_DEFAULTNAME']}\n\n[5] {LANG['CLOSE']}")
            
            Cevap = Prompt.ask(f"[bold yellow]{LANG['WHAT_YOU_WANT']}[/]", choices=["1", "2", "3", "4", "5"], default="5")
        basarili(LANG['SEEYOU'])
