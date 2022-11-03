import js
import pyodide


menu_all = js.document.getElementById("menu_all")
def menu():
    menu_all.innerHTML += "<li class='menu-title'><span>Example List</span></li>"
    menu_all.innerHTML += "<li><a href='input_app.html'>Input App</a></li>"
    menu_all.innerHTML += "<li><a href='clock.html'>Clock</a></li>"
    menu_all.innerHTML += "<li><a href='binance_price.html'>Binance Price</a></li>"
    menu_all.innerHTML += "<li><a href='ascii.html'>ASCII</a></li>"
    menu_all.innerHTML += "<li><a href='falling_snow.html'>Falling Snow</a></li>"


def header():
    js.document.getElementById("header").innerHTML += """
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title id="set_title">PURE PYTHON NON JS</title>
    <link rel="shortcut icon" href="../icon.png" type="image/x-icon">
    """