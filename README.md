<p align="center"><img src="https://media.discordapp.net/attachments/585069498986397707/1034910530336460910/rtset.gif">
</p>

# Pure Python Non Js With Pyscript
Just use HTML + Pyscript + .PY

# Install
```
git clone https://github.com/watchakorn-18k/Pure-Python-Non-Js-With-Pyscript

cd Pure-Python-Non-Js-With-Pyscript
```



# Run
- Open File `index.html` or [Open Link](https://watchakorn-18k.github.io/Pure-Python-Non-Js-With-Pyscript/)


# main.py
```py
import js
import pyodide
import random
import asyncio
  
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
    js.window.location = 'main.py'

Btn_Click.addEventListener("click", pyodide.ffi.create_proxy(welcome_user))
btn_source_code.addEventListener("click", pyodide.ffi.create_proxy(Golink))
name_user.addEventListener("keydown", pyodide.ffi.create_proxy(lambda e:welcome_user(e) if e.key == "Enter" else None))
```

# index.html
```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title id="set_title">PURE PYTHON NON JS</title>
    <link rel="stylesheet" href="css/pyscript.css">
    <link href="https://cdn.jsdelivr.net/npm/daisyui@2.33.0/dist/full.css" rel="stylesheet" type="text/css" />
    <link rel="shortcut icon" href="icon.png" type="image/x-icon">


    <py-config src="./config.toml"></py-config>
</head>

<body>
    <div class="navbar bg-base-100">
  <div class="flex-1">
    <a class="btn btn-ghost normal-case text-xl" id="set_title_nav">PURE PYTHON NON JS</a>
  </div>
  <!-- <div class="navbar-end">
    <a class="btn">English</a>
  </div> -->
</div>
    <py-script src="./main.py"> </py-script>
    <div class="grid justify-items-center ...">
        <div class="form-control w-full max-w-xs">
            <label class="label">
                <span class="label-text">What is your name?</span>
                <span class="label-text-alt">Can <kbd class="kbd kbd-sm">Enter</kbd> to Submit</span>
            </label>
            <input type="text" placeholder="Enter your name" name="name_user"
                class="input input-bordered w-full max-w-xs" />
            <br>
            <button class="btn btn-outline btn-success" id="submit">Submit</button>
            <br>
            <progress class="progress progress-success" value="0" max="100" id="progress_genarate_word"></progress>
        </div>
        <br>
        <div class="card w-96 bg-primary shadow-xl" id="card-name" hidden>
            <div class="card-body items-center text-center">
                <h2 class="card-title">Welcome <p id="user_name_title"></p></h2>
                <p id="client-name"></p>
            </div>
        </div>
        <br>
        <button class="btn btn-xs sm:btn-sm md:btn-md lg:btn-lg" id="btn_source_code">SOURCE CODE</button>
    </div>
    
</body>

<script src="js/pyscript.js"></script>
<script src="https://cdn.tailwindcss.com"></script>

</html>
```

<b>Using javascript, just import pyscript with tailwindcss.<b/>
