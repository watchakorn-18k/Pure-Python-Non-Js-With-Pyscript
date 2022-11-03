<p align="center"><img src="https://media.discordapp.net/attachments/581018943041306641/1037724522859737199/less_js.gif?width=494&height=658">
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


## components/input_app.py
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

## components/input_app.html
```html
<!DOCTYPE html>
<html lang="en">
<head id="header">
    <py-config src="../config.toml"></py-config>
    <py-env>
        - paths:
            - layouts.py
    </py-env>
    <link href="https://cdn.jsdelivr.net/npm/daisyui@2.33.0/dist/full.css" rel="stylesheet" type="text/css" />
    <link rel="stylesheet" href="../css/pyscript.css">
    <py-script src="./input_app.py"> </py-script>
</head>
<script src="../js/pyscript.js"></script>
<script src="https://cdn.tailwindcss.com"></script>
<body>
    <div class="drawer">
        <input id="my-drawer-3" type="checkbox" class="drawer-toggle" /> 
        <div class="drawer-content flex flex-col">
          <!-- Navbar -->
          <div class="w-full navbar bg-base-300">
            <div class="flex-none">
              <label for="my-drawer-3" class="btn btn-square btn-ghost">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block w-6 h-6 stroke-current"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
              </label>
            </div> 
            <div class="flex-1 px-2 mx-2"><a href="index.html" id="set_title_nav">PURE PYTHON NON JS 💪🏻</a></div>
            <div class="flex-none hidden lg:block">
              <ul class="menu menu-horizontal">
                <!-- Navbar menu content here -->
              </ul>
            </div>
          </div>
          <!-- Page content here -->
          
          <div class="grid justify-items-center ...">
            <div class="hero">
                <div class="hero-content text-center">
                  <div class="max-w-md">
                    <h1 class="text-5xl font-bold">Input App</h1>
                  </div>
                </div>
            </div>
            
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
        </div> 
        <div class="drawer-side">
          <label for="my-drawer-3" class="drawer-overlay"></label> 
          <ul class="menu p-4 overflow-y-auto w-80 bg-base-100" id="menu_all">
            <!-- Sidebar content here -->
          </ul>      
        </div>
      </div>
</body>
</html>
```

<b>Using javascript, just import pyscript with tailwindcss.<b/>
