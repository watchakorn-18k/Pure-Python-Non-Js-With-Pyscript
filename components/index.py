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
