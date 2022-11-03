import js
import pyodide
from layouts import *

header()
menu()
convert2char = js.document.getElementById('convert-ascii')

result_show = js.document.getElementById('result-char')





def go_to_source(e):
    js.window.location = 'ascii.py'

def convert_to_char(e):
    try:
        int_number = int(convert2char.value)
        result_show.innerHTML = f"{chr(int_number)}"
    except:
        char_ascii = convert2char.value
        result_show.innerHTML = f"{ord(char_ascii)}" if len(char_ascii) == 1 else "Please enter number or character" if len(char_ascii) == 0 else "Only one character can be entered as an ASCII number."


btn_source_code = js.document.getElementById("btn_source_code").addEventListener('click',pyodide.ffi.create_proxy(go_to_source))
convert2char.addEventListener('keyup',pyodide.ffi.create_proxy(convert_to_char))
