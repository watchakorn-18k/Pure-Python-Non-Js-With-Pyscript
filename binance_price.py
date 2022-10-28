import pyodide
from pyodide.http import pyfetch
import js
import asyncio
from layout import *

menu()

url = "https://binance43.p.rapidapi.com/ticker/24hr"

headers = {
	"X-RapidAPI-Key": "c37160bd91msh3cb69439624aab0p1381b5jsn98d893dea099",
	"X-RapidAPI-Host": "binance43.p.rapidapi.com"
}



response = await pyfetch(url=url,method="GET",headers=headers)

data = await response.json()
data_all = data.copy()
data_all = data_all[:100]

name = js.document.getElementById("name")
card = js.document.getElementById("card_all")
for i in data_all:
    if float(i['lastPrice']) > 0 :
        card.innerHTML += f"""
        <div class="stat" >
            <div class="stat-title">{i["symbol"]}</div>
            <div class="stat-value">{i['lastPrice']}</div>
            <div class="stat-desc">{i["priceChangePercent"]}% price change, in percentage</div>
        </div>
        """


