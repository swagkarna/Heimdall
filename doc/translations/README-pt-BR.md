# ⚡️ Heimdall ⚡️
[![License](https://img.shields.io/badge/Licença-MIT-critical.svg?style=flat-square)](https://github.com/CR3DN3/Heimdall/blob/master/LICENSE) [![Python3.x](https://img.shields.io/badge/Python-3.8-yellow.svg?style=flat-square&logo=python)](https://www.python.org/)

[![GitHub](https://img.shields.io/badge/GitHub-CR3DN3-inactive.svg?style=social&logo=github)](https://github.com/CR3DN3/)
[![Facebook](https://img.shields.io/badge/Facebook-inactive.svg?style=social&logo=Facebook)](https://www.facebook.com/oldygor/)
[![Twitter](https://img.shields.io/badge/Twitter-CR3DN3-inactive.svg?style=social&logo=twitter)](https://twitter.com/CR3DN3/)
[![Instagram](https://img.shields.io/badge/Instagram-inactive.svg?style=social&logo=Instagram)](https://instagram.com/oldygor)
![Screenshot](https://raw.githubusercontent.com/CR3DN3/Heimdall/master/doc/images/heimdall.gif)

## O que é isso?

O Heimdall é uma ferramenta de código aberto projetada para automatizar a busca do painel de administração de um site alvo usando força bruta na lista de palavras. Desenvolvida totalmente em Python, possui um código didático e simples para estudos, além de ser uma ferramenta ideal para o arsenal de hacker.

## Capturas de Telas

![Screenshot](https://raw.githubusercontent.com/CR3DN3/Heimdall/master/doc/images/screenshot.png)

## Testado no

* macOS Catalina
* Manjaro
* Kali Linux

## Instalação

Você pode baixar o tarball mais recente clicando [aqui](https://github.com/CR3DN3/Heimdall/tarball/master) ou zipball mais recente, clicando [aqui](https://github.com/CR3DN3/Heimdall/zipball/master).

    $ git clone --depth 1 https://github.com/CR3DN3/Heimdall.git
    $ cd Heimdall && pip3 install -r requirements.txt

## Uso

```
Usage: ./heimdall.py [-h, --help] [-u, --url] [-w, --wordlist (1, 2, 3)]
                     [--user-agent <custom>] [--update]

Description: Heimdall is an open source tool designed to automate fetching 
             from a target site's admin panel using brute force in the wordlist.

Optional Arguments:

   -h, --help             Show this help message and exit
   -u URL, --url URL      Target URL (http://www.site.com/)
   --wordlist (1, 2, 3)   Set wordlist. Default: 1 (Small) and Max: 3 (Big)
   -p, --proxy            Use a proxy to connect to the target URL
   --user-agent           Customize the User-Agent. Default: Random User-Agent
   --update               Upgrade Heimdall to its latest available version.
```

### Exemplos

```
./heimdall.py --url www.target.com --wordlist 1
./heimdall.py --url www.target.com --wordlist 2 --user-agent <USER-AGENT>
./heimdall.py --url www.target.com --wordlist extra/wordlists/custom.txt
./heimdall.py --update
```

## Traduções

* [English](https://github.com/CR3DN3/Heimdall/blob/master/README.md)
* [Portuguese](https://github.com/CR3DN3/Heimdall/blob/master/doc/translations/README-pt-BR.md)
