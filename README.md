<p align="center"><img src="https://media.discordapp.net/attachments/581018943041306641/1037724522859737199/less_js.gif" width=50%>
</p>

# Pure Python Non Js With Pyscript
We make an effort to build an app website without JS, to say the least. But actually we just change the format to use. The modules available in pyodide are based on JS commands on python.

<b>Using javascript, just import [pyscript](https://pyscript.net/) and [tailwindcss](https://tailwindcss.com/) and [daisyui](https://daisyui.com/)<b/>


# Install
```
git clone https://github.com/watchakorn-18k/Pure-Python-Non-Js-With-Pyscript

cd Pure-Python-Non-Js-With-Pyscript
```

# Example 
File `index.html`
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
    <py-script src="./index.py"> </py-script>
</head>
<script src="../js/pyscript.js"></script>
<script src="https://cdn.tailwindcss.com"></script>
<body>
  <div id="main" class="drawer">
    <div class="drawer-side" id="start-slide">
      <label for="my-drawer-3" class="drawer-overlay"></label> 
      <ul class="menu p-4 overflow-y-auto w-80 bg-base-100" id="menu_all">
        <!-- Sidebar content here -->
      </ul>
    </div>
  </div>
</body>
</html>
```

File `index.py`
```python
import js
from layouts import *

header()
menu()

js.document.getElementById('start-slide').insertAdjacentHTML('beforebegin',"""
  <input id="my-drawer-3" type="checkbox" class="drawer-toggle" /> 
  <div class="drawer-content flex flex-col">
    <!-- Navbar -->
    <div class="w-full navbar bg-base-300">
      <div class="flex-none">
        <label for="my-drawer-3" class="btn btn-square btn-ghost">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block w-6 h-6 stroke-current"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
        </label>
      </div> 
      <div class="flex-1 px-2 mx-2"><a href="index.html">PURE PYTHON NON JS 💪🏻</a></div>
      <div class="flex-none hidden lg:block">
        <ul class="menu menu-horizontal">
          <!-- Navbar menu content here -->
        </ul>
      </div>
    </div>
    <!-- Page content here -->
    <div class="hero">
      <div class="hero-content text-center">
        <div class="max-w-md">
          <div class="avatar online">
              <div class="w-24 rounded-full">
                <img src="https://avatars.githubusercontent.com/u/74919942?v=4" />
              </div>
            </div>
          <h1 class="text-5xl font-bold">Hello there</h1>
          <p class="py-6">My name is WK-18k and here is an example building a web app that doesn't use JS but is powered by Pyscript.</p>
          <button class="btn btn-primary"><a href="https://github.com/watchakorn-18k/Pure-Python-Non-Js-With-Pyscript">Source Code</a></button>
          <br>
        </div>
      </div>
  </div>
  </div> 
""")

```

File `layouts.py`
```python
import js
import pyodide


menu_all = js.document.getElementById("menu_all")
def menu():
    menu_all.innerHTML += "<li class='menu-title'><span>Example List</span></li>"
    menu_all.innerHTML += "<li><a href='input_app.html'>Input App</a></li>"
    menu_all.innerHTML += "<li><a href='clock.html'>Clock</a></li>"
    menu_all.innerHTML += "<li><a href='binance_price.html'>Binance Price</a></li>"
    menu_all.innerHTML += "<li><a href='ascii.html'>ASCII</a></li>"


def header():
    js.document.getElementById("header").innerHTML += """
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title id="set_title">PURE PYTHON NON JS</title>
    <link rel="shortcut icon" href="../icon.png" type="image/x-icon">
    """
```


# Run
- Open File `index.html` or [Open Link](https://watchakorn-18k.github.io/Pure-Python-Non-Js-With-Pyscript/)

# Tree File
```
│   config.toml
│   icon.png
│   index.html
│   README.md
│   
├───.vscode
│       settings.json
│       
├───components
│       ascii.html
│       ascii.py
│       binance_price.html
│       binance_price.py
│       clock.html
│       clock.py
│       index.html
│       index.py
│       input_app.html
│       input_app.py
│       layouts.py
│
├───css
│       pyscript.css
│
└───js
        pyscript.js

```

# Example List
<p align="center"><img src="https://media.discordapp.net/attachments/581018943041306641/1037749656018489354/image.png" width=40%></p>

[Input App](https://watchakorn-18k.github.io/Pure-Python-Non-Js-With-Pyscript/components/input_app.html) : Example of creating a form to receive data from the client

<p align="center"><img src="https://media.discordapp.net/attachments/581018943041306641/1037750924371836958/less_js.gif" width=40%></p>

[Clock](https://watchakorn-18k.github.io/Pure-Python-Non-Js-With-Pyscript/components/clock.html) : An example of making a real-time display clock

<p align="center"><img src="https://media.discordapp.net/attachments/581018943041306641/1037751514673991680/less_js.gif" width=40%></p>

[Binance Price](https://watchakorn-18k.github.io/Pure-Python-Non-Js-With-Pyscript/components/binance_price.html) : This is an example of retrieving data with an API without using JavaScript.

<p align="center"><img src="https://media.discordapp.net/attachments/581018943041306641/1037752869597753455/less_js.gif" width=40%></p>

[ASCII](https://watchakorn-18k.github.io/Pure-Python-Non-Js-With-Pyscript/components/ascii.html) : An example of an ASCII transformation that uses Python's built-in function `chr()` with `ord()` to demonstrate Python's capabilities.

<p align="center"><img src="https://media.discordapp.net/attachments/581018943041306641/1037809745500831824/less_js.gif?width=350&height=658" width=40%></p>

[Falling Snow](https://watchakorn-18k.github.io/Pure-Python-Non-Js-With-Pyscript/components/falling_snow.html) : An example of creating snow falling from the sky using basic python, either map() or using dict instead of array in JS by reference from [PasaComputer - Falling Snow | JavaScript 21 Days Challenge EP. 1 | สอน JavaScript เรียนรู้จากการลงมือทำ](https://youtu.be/oKY8tJLA5nU)


# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate.



