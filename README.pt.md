![Static Badge](https://img.shields.io/badge/Python-3.14-blue?logo=python&logoColor=white)

<h1 align='center'>StreamPy</h1>
<p align='center'>
  <img src="./Images/Miku-Halo.webp", alt="Miku-Halo.webp">
</p>

[ENGLISH](README.md) | [PORTUGUÊS]

<h2>Funções</h2>
<li>Botões Programáveis Customizáveis</li>
<li>Execução de macros</li>
<li>Controle de mídia e volume</li>
<li>Suporte a Soundboard</li>
<li>Inicializador de aplicações</li>
<li>Automação de fluxo de trabalho</li>
<li>Comunicação ESP32 + Python</li>
<li>Leve e customizável</li>
<li>Alternativa de baixo custo a painéis de controle comerciais</li>
<hr>
<h2>Visão Geral</h2>
<p>
StreamPy e um painel de controle desktop multifunção, inspirado por dispositivos como o Stream Deck. 
Originalmente idealizado como uma DIY SoundBoard, o projeto evoluiu para uma ferramenta de automação de fluxo de trabalho/produtividade capaz de controlar outras aplicações,
executar macros, gerenciar mídias, e acionar ações customizaveis atravez de botões físicos ou atalhos do teclado.
O sistema integra hardware e software para fornercer uma solução de painel de controle baixo custo e customizável para streamers, fluxos de trabalho produtivos, aplicações multimídia etc.
</p>

<h2>Arquitetura</h2>
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

<h2>Instalação</h2>


Clone o repositorio git
```shell
git clone https://github.com/Karanzito/StreamPy
```


Crie um python3.14 virtual environment
```shell
python3.14 -m venv .venv
```


Instale as dependências com o requirements.txt
```shell
pip install -r requirementx.txt
```