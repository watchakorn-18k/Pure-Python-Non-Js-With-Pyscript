import js
import pyodide
import random
import asyncio
from layout import *
  
menu()
  
list_title = ["PURE PYTHON NON JS","ONLY PYTHON","LESS JS","WK18K","JUST WEB"]
name_title_random = random.choice(list_title)
getId = lambda id:js.document.getElementById(id)
set_title,set_title_nav = getId("set_title"),getId("set_title_nav")
set_title.innerHTML = set_title_nav.innerHTML = name_title_random
name_user = js.document.querySelector("input[name=name_user]")
Btn_Click = getId("submit")
card_name = getId("card-name")
user_name_title = getId("user_name_title")
client_name = getId("client-name")
progress_genarate_word = getId("progress_genarate_word")
btn_source_code = getId("btn_source_code")


async def progress_run():
    for i in range(100):
        progress_genarate_word.value += 1
        await asyncio.sleep(0)

async def welcome_user(e):
    progress_genarate_word.value = 0
    list_text = [f"Welcome to your new life {name_user.value}.",f"{name_user.value},You're always welcome here",f"{name_user.value},You're welcome to look at anything on my computer.","By the way, welcome to God's country."]
    await progress_run() if name_user.value and name_user.value != "" else None
    card_name.hidden = False if name_user.value and name_user.value != "" else True
    user_name_title.textContent = name_user.value
    client_name.textContent = random.choice(list_text)

def Golink(e):
    js.window.location = 'https://github.com/watchakorn-18k/Pure-Python-Non-Js-With-Pyscript'

Btn_Click.addEventListener("click", pyodide.ffi.create_proxy(welcome_user))
btn_source_code.addEventListener("click", pyodide.ffi.create_proxy(Golink))
name_user.addEventListener("keydown", pyodide.ffi.create_proxy(lambda e:welcome_user(e) if e.key == "Enter" else None))