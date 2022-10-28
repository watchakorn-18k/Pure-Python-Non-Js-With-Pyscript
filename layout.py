import js
import pyodide


menu_all = js.document.getElementById("menu_all")
def menu():
    menu_all.innerHTML += "<li class='menu-title'><span>Example List</span></li>"
    menu_all.innerHTML += "<li><a href='input_app.html'>Input App</a></li>"
    menu_all.innerHTML += "<li><a href='clock.html'>Clock</a></li>"
    menu_all.innerHTML += "<li><a href='binance_price.html'>Binance Price</a></li>"