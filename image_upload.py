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
    H = datetime.now().strftime('%H')
    M = datetime.now().strftime('%M')
    S = datetime.now().strftime('%S')

    return H,M,S

sec = js.document.getElementById("second")
minte = js.document.getElementById("minute")
hour = js.document.getElementById("hour")


async def run():
    while True:
        await asyncio.sleep(1)
        H,M,S = refreshTime()
        hour.style = f"--value:{H}"
        minte.style = f"--value:{M}"
        sec.style = f"--value:{S}"

pyscript.run_until_complete(run())