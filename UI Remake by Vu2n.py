from bs4 import BeautifulSoup
import requests
from pathlib import Path
import colorama
from colorama import Fore
import os, time, pystyle, ctypes, fade
from pystyle import *

# Remaking a UI i saw on Discord cause it looked sexy
# Was really easy but the unicode logo and boxes are a bitch
# Probs dont need all the imports but i just copy pasted them from another file
# dont use this for a panel because its PYTHON lmao
# legit a simple base with no functionality made in 10 minutes

# Remade by Vu2n

logo = f'''
{Col.white}               ╔═╗─┐ ┬┬┌┐┌┌─┐
{Col.white}               ║ ║┌┴┬┘││││├┤ 
{Col.white}               ╚═╝┴ └─┴┘└┘└─┘ {Col.red}
         ══╦═══════════════════╦══
   ╔═══════╩═══════════════════╩═════════╗                                     
   ║ {Col.white}        Welcome To Oxine {Col.red}           ║
   ║ {Col.white}        A Shitty Resolver  {Col.red}         ║  
   ║ {Col.white}        Type Help For CMDS  {Col.red}        ║
   ╚═════════════════════════════════════╝              
'''

print(logo) 
print("")
enter = input(f"{Col.red}╔════[root{Col.white}@{Col.red}Oxine]{os.linesep}╚═══> ") # this is the cool input thing, just change the {col.} for colors

HelpC = "Help" # can probs do this alot better and easier
helpL = "help" # but i made this in 10 minutes so :)

if enter == helpL:
    # just add all your shit here for commands
else:
    if enter == HelpC:
        # just add all your shit here for commands
