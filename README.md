![Static Badge](https://img.shields.io/badge/Python-3.14-blue?logo=python&logoColor=white)

<h1 align='center'>StreamPy</h1>
<p align='center'>
  <img src="./Images/Miku-Halo.webp", alt="Miku-Halo.webp">
</p>

[ENGLISH] | [PORTUGUÊS](README.pt.md)

<h2>Features</h2>
<li>Custom programmable buttons</li>
<li>Macro execution</li>
<li>Media and volume control</li>
<li>Soundboard support</li>
<li>Application launcher</li>
<li>Workflow automation</li>
<li>ESP32 + Python communication</li>
<li>Lightweight and customizable</li>
<li>Low-cost alternative to commercial control panels</li>
<hr>
<h2>Overview</h2>
<p>
StreamPy is a multifunction desktop control panel inspired by devices such as the Stream Deck.
Originally designed as a DIY soundboard, the project evolved into a programmable productivity and workflow automation tool capable of controlling applications, 
executing macros, managing media, and triggering custom actions through physical buttons or keybinds.
The system combines hardware and software integration to provide a low-cost and customizable control interface for streamers, 
productivity workflows, and multimedia application
</p>

<h2>Architecture</h2>
<h3>Hardware</h3>
<li>ESP32</li>
<h3>Front-end</h3>
<li>HTML/CSS</li>
<h3>API</h3>
<li>Flask</li>
<h3>Back-end</h3>
<li>Python3.14</li>
<li>PySerial</li>
<li>PyScript</li>
<li>sqlite3</li>


<!-- Conteudo pendente de revisão
<h2>Possible Use Cases</h2>
<li>Streaming control panel</li>
<li>Productivity shortcuts</li>
<li>OBS scene switching</li>
<li>Soundboard</li>
<li>Media controller</li>
<li>Smart desktop automation</li>
<li>Development workflow shortcuts</li> -->

<h2>Setup</h2>
<p>Clone the git reposity</p>
`git clone https://github.com/Karanzito/StreamPy`

<p>Create a python3.14 virtual environment</p>
`python3.14 -m venv .venv`

<p>Intall the requirements.txt</p>
`pip install -r requirementx.txt`