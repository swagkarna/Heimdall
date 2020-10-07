# ⚡️ Heimdall ⚡️
[![Build Status](https://travis-ci.org/CR3DN3/Heimdall.svg?branch=master)](https://travis-ci.org/CR3DN3/Heimdall) [![License](https://img.shields.io/badge/License-MIT-critical.svg?style=flat&logo=)](https://github.com/CR3DN3/Heimdall/blob/master/LICENSE) [![Python3.8](https://img.shields.io/badge/Python-3.8-yellow.svg?style=flat&logo=python)](https://www.python.org/) [![Releases](https://img.shields.io/badge/release-v4.0--beta-yellow)](https://github.com/CR3DN3/Heimdall/releases/tag/v4.0-beta)

Heimdall é uma ferramenta de código aberto projetada para automatizar a busca no painel de administração de um site de destino usando força bruta na lista de palavras. Desenvolvido inteiramente em Python, possui código didático simples para estudo, e é uma ferramenta ideal para arsenal de hacking.

![HeimdallGif](https://raw.githubusercontent.com/CR3DN3/Heimdall/master/doc/images/heimdall.gif)

## Requerido

É extremamente importante que você tenha as ferramentas obrigatórias listadas abaixo para que o Heimdall funcione conforme o esperado.
É recomendável que você use um sistema operacional com foco no Pentest.

* [`python`](https://www.python.org/): (Only version 3 of python is supported.)
* [`requests`](https://requests.readthedocs.io/) "A simple, yet elegant HTTP library."

## Instalação

Você pode baixar o tarball mais recente clicando em [aqui](https://github.com/CR3DN3/Heimdall/tarball/master) ou o zipball mais recente clicando em [aqui](https://github.com/CR3DN3/Heimdall/zipball/master).

    $ git clone https://github.com/CR3DN3/Heimdall.git
    $ cd Heimdall && pip install -r requirements.txt

## Modo de uso

```
Usage: python heimdall.py [-h, --help] [-u, --url] [-w, --wordlist (1, 2, 3)]
                           [-p, --proxy <proxy>][--user-agent <custom>] [--update]

Description: Heimdall is an open source tool designed to automate fetching 
             from a target site's admin panel using brute force in the wordlist.

Optional Arguments:

   -h, --help             Show this help message and exit
   -u URL, --url URL      Target URL (http://www.site_target.com/)
   --wordlist (1, 2, 3)   Set wordlist. Default: 1 (Small) and Max: 3 (Big)
   -p, --proxy            Use a proxy to connect to the target URL
   --user-agent           Customize the User-Agent. Default: Random User-Agent
   --update               Upgrade Heimdall to its latest available version.
   
   --no-update            Disables the intention of updates
   --no-logo              Disable the initial banner
```

## Capturas de tela

![Screenshot](https://raw.githubusercontent.com/CR3DN3/Heimdall/master/doc/images/screenshots/screenshot.png)

Você pode visitar a coleção de capturas de tela que demonstram o funcionamento em algumas plataformas clicando [aqui](https://github.com/CR3DN3/Heimdall/tree/master/doc/images/screenshots).

### Exemplos

```
./heimdall.py --url www.site_target.com --wordlist 1
./heimdall.py --url www.site_target.com --wordlist 2 --user-agent <USER-AGENT>
./heimdall.py --url www.site_target.com --wordlist extra/wordlists/custom.txt
./heimdall.py --update
```

## Traduções

* [English](https://github.com/CR3DN3/Heimdall/blob/master/README.md)
* [Portuguese](https://github.com/CR3DN3/Heimdall/blob/master/doc/translations/README-pt-BR.md)

# Autor
* Ygor Simões (CR3DN3) - [![GitHub](https://img.shields.io/badge/GitHub-CR3DN3-inactive.svg?style=social&logo=github)](https://github.com/CR3DN3/)
[![Facebook](https://img.shields.io/badge/Facebook-inactive.svg?style=social&logo=Facebook)](https://www.facebook.com/oldygor/)
[![Twitter](https://img.shields.io/badge/Twitter-CR3DN3-inactive.svg?style=social&logo=twitter)](https://twitter.com/CR3DN3/)
[![Instagram](https://img.shields.io/badge/Instagram-inactive.svg?style=social&logo=Instagram)](https://instagram.com/oldygor)