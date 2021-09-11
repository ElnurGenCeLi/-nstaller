from rich.live_render import LiveRender
from rich.console import Console
from rich.panel import Panel
import os, shutil
import sys


console = Console()

def hata (text):
   console.print(Panel(f'[bold red]{text}[/]',width=70),justify="center")                         
def bilgi (text):
   console.print(Panel(f'[blue]{text}[/]',width=70),justify="center")                         
def basarili (text):
   console.print(Panel(f'[bold green] {text}[/]',width=70),justify="center")                         
def onemli (text):
   console.print(Panel(f'[bold cyan]{text}[/]',width=70),justify="center")                         
def soru (soru):
   console.print(Panel(f'[bold yellow]{soru}[/]',width=70),justify="center")                         
   return console.input(f"[bold yellow]>> [/]")
def logo (dil = "None"):
   surum = str(sys.version_info[0]) + "." + str(sys.version_info[1])
   console.print(Panel(f"[bold blue]🐺𝙱𝚘𝚣𝚀𝚞𝚛𝚍 𝙸𝚗𝚜𝚝𝚊𝚕𝚕𝚎𝚛🐺[/]\n\n[bold cyan]Version: [/][i]1.0[/]\n[bold cyan]Python: [/][i]{surum}[/]\n[bold cyan]Dil: [/][i]{dil}[/]",width=80),justify="center")                         
def tamamlandi (saniye):
   console.print(Panel(f"[bold green]BozQurd Qurulumu Uğurla başa çatdı!\n[i]Botu {round(saniye)} saniyə içində qurdunuz.[/]\n\n[bold green]Bir müddət sonra hər hansı bir söhbətdə .alive yazaraq botunuzu yoxlaya bilərsiniz. Uğurlar :)[/]",width=70),justify="center")                     
                   
def rm_r(path):
    if not os.path.exists(path):
        return
    if os.path.isfile(path) or os.path.islink(path):
        os.unlink(path)
    else:
        shutil.rmtree(path)

def Sifre(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        yield S[(S[i] + S[j]) % 256]

def Sifrele(yazi, key, hexformat=False):
    key, yazi = bytearray(key), bytearray(yazi)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    keystream = Sifre(S)
    return b''.join(b"%02X" % (c ^ next(keystream)) for c in yazi) if hexformat else bytearray(c ^ next(keystream) for c in yazi)
