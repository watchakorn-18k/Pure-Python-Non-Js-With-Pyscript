import os
import js
from datetime import datetime
import pyodide
import random
import asyncio
from layout import *
  
menu()

timeDisplay = js.document.getElementById("time");

def refreshTime() -> str:
    D = datetime.now().strftime('%d')
    H = datetime.now().strftime('%H')
    M = datetime.now().strftime('%M')
    S = datetime.now().strftime('%S')

    return H,M,S,D

sec = js.document.getElementById("second")
minte = js.document.getElementById("minute")
hour = js.document.getElementById("hour")
day = js.document.getElementById("day")


async def run():
    while True:
        await asyncio.sleep(1)
        H,M,S,D = refreshTime()
        print(D)
        day.style = f"--value:{D}"
        hour.style = f"--value:{H}"
        minte.style = f"--value:{M}"
        sec.style = f"--value:{S}"

pyscript.run_until_complete(run())