from . import logo, console, bilgi, hata, soru
from rich.prompt import Prompt
from rich.panel import Panel
from time import sleep
from json import loads

def importlang ():
    console.clear()
    logo()
    bilgi("[blue]\n\n[1] Azərbaycanca\n[2] Türkçə\n[3] English[/]")
    Dil = Prompt.ask("[bold yellow]Bir dil seçin / Please select a language[/]", choices=["1", "2", "3"], default="1")

    if Dil == "1":
            COUNTRY = "Azerbaijan"
            LANGUAGE = "AZ"
            TZ = "Asia/Baku"
    elif Dil == "2":
        COUNTRY = "Turkey"
        LANGUAGE = "TR"
        TZ = "Europe/Istanbul"
    elif Dil == "3":
            COUNTRY = "United Kingdom"
            LANGUAGE = "EN"
            TZ = "Europe/London"

    return COUNTRY, LANGUAGE, TZ

COUNTRY, LANGUAGE, TZ = importlang()
LANG = loads(open(f"./bozqurd_installer/language/{LANGUAGE}.bozqurdjson", "r").read())["STRINGS"]
