![Static Badge](https://img.shields.io/badge/Python-3.14-blue?logo=python&logoColor=white)

<h1 align='center'>StreamPy</h1>
<p align='center'>
  <img src="./Images/Miku-Halo.webp", alt="Miku-Halo.webp">
</p>

[ENGLISH](README.md) | [PORTUGUÊS]

<h2>Funções</h2>
<li>Boões Programaveis Customizáveis</li>
<li>Execução de macros</li>
<li>Controle de mídia e volume</li>
<li>Suporte a Soundboard</li>
<li>Inicializador de aplicações</li>
<li>Automação de fluxo de trabalho</li>
<li>Comunicação ESP32 + Python</li>
<li>Leve e customizável</li>
<li>Alternativa de baixo custo a paineis de controle comerciais</li>
<hr>
<h2>Visão Geral</h2>
<p>
StreamPy e um painel de controle desktop multifunção, inspirado por dispositivos como o Stream Deck. 
Originalmente idealizado como uma DIY SoundBoard, o projeto evoluiu para uma ferramenta de automação de fluxo de trabalho/produtividade capaz de controlar outras aplicações,
executar macros, gerenciar mídias, e acionar ações customizaveis atravez de botões físicos ou atalhos do teclado.
O sistema integra hardware e software para fornercer uma solução de painel de controle baixo custo e customizável para streamers, fluxos de trabalho produtivos, aplicações multimedia etc.
</p>

<!-- Trecho sujeito a mudanças -->
<h2>Arquitetura</h2>
<h3>Back-end</h3>
<li>Python3.14</li>
<li>ESP32-C3</li>
<li>PySerial</li>
<li>Pygame-mixer</li>
<li>json</li>
<h3>Front-end</h3>
<li>customtkinter</li>

<h2>Instalação</h2>
<p>Clone o repositorio git</p>
`git clone https://github.com/Karanzito/StreamPy`

<p>Crie um python3.14 virtual environment</p>
`python3.14 -m venv .venv`

<p>Instale o requirements.txt</p>
`pip install -r requirementx.txt`

<p>Caso necessario, instale pipfreeze.txt para replicar as minhas configurações exatas</p>
`pip install -r pipfreeze.txt`