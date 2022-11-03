import js
import pyodide
import random
import math
from layouts import *

header()
menu()


def setup():
    """
    setup canvas and return `canvas,` `canvas_context`, `number_of_snow_balls`
    """
    canvas = js.document.getElementById("falling-snow")
    canvas.width = js.window.innerWidth
    canvas.height = js.window.innerHeight
    canvas_context = canvas.getContext('2d')
    number_of_snowballs = 250
    return canvas, canvas_context, number_of_snowballs


def random_number(min,max):
    # random with js
    js_random = js.Math.floor(js.Math.random() * (max - min - 1)) + min
    # random with python
    py_random = random.randint(min,max)
    return py_random


def create_snowballs(canvas,number_of_snowballs):
    """
    for create snowball with get parameter `canvas`,`number_of_snowballs`
    """
    list_empty = [None] * number_of_snowballs
    def create_dict():
        return ({
            "x":random_number(0,canvas.width),
            "y":random_number(0,canvas.height),
            "opacity":random.uniform(0.3,1),
            "radius":random_number(2,4),
            "speed_x": random_number(-2,2),
            "speed_y": random.uniform(0.1,3)
            })
    # map list return x : random_number(0,canvas.width) ,y : random_number(0,canvas.height)
    map_list = list(map(lambda e:create_dict(),list_empty))
    return map_list
    
def draw_snowball(canvas_context,snowball):
    """
    draw snowball with canvas
    """
    canvas_context.beginPath()
    canvas_context.arc(snowball["x"],snowball["y"],snowball["radius"],0,math.pi * 2)
    canvas_context.fillStyle = f'rgba(255,255,255,{snowball["opacity"]})'
    canvas_context.fill()

def move_snowball(canvas,snowball):
    snowball["x"] += snowball["speed_x"]
    snowball["y"] += snowball["speed_y"]

    if snowball["x"] > canvas.width:
        snowball["x"] = 0
    elif snowball["x"] < 0:
        snowball["x"] = canvas.width
    
    if snowball["y"] > canvas.height:
        snowball["y"] = 0


def run():
    """
    run app
    """
    canvas, canvas_context, number_of_snowballs = setup()
    snowballs = create_snowballs(canvas,number_of_snowballs)


    def run_loop():
        canvas_context.clearRect(0,0,canvas.width,canvas.height)
        [draw_snowball(canvas_context,i) for i in snowballs]
        [move_snowball(canvas,i) for i in snowballs]
        
    # js.setInterval(pyodide.ffi.create_proxy(_def_), 1000, "a parameter")
    js.setInterval(pyodide.ffi.create_proxy(run_loop),50)
    

def go_to_source(e):
    js.window.location = 'falling_snow.py'

btn_source_code = js.document.getElementById("btn_source_code").addEventListener('click',pyodide.ffi.create_proxy(go_to_source))

if __name__ == "__main__":
    run()
