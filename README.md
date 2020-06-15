# ⚡️ Heimdall ⚡️
[![License](https://img.shields.io/badge/License-MIT-critical.svg?style=flat-square)](https://github.com/CR3DN3/Heimdall/blob/master/LICENSE) [![Python3.8](https://img.shields.io/badge/Python-3.8-yellow.svg?style=flat-square&logo=python)](https://www.python.org/)

[![GitHub](https://img.shields.io/badge/GitHub-CR3DN3-inactive.svg?style=social&logo=github)](https://github.com/CR3DN3/)
[![Facebook](https://img.shields.io/badge/Facebook-inactive.svg?style=social&logo=Facebook)](https://www.facebook.com/oldygor/)
[![Twitter](https://img.shields.io/badge/Twitter-CR3DN3-inactive.svg?style=social&logo=twitter)](https://twitter.com/CR3DN3/)
[![Instagram](https://img.shields.io/badge/Instagram-inactive.svg?style=social&logo=Instagram)](https://instagram.com/oldygor)
![Screenshot](https://raw.githubusercontent.com/CR3DN3/Heimdall/master/doc/images/heimdall.gif)

## What this is?

Heimdall is an open source tool designed to automate fetching from a target site's admin panel using brute force in the wordlist. Developed entirely in Python, it has simple didactic code for study, and is an ideal tool for hacking arsenal.

## Screenshot

![Screenshot](https://raw.githubusercontent.com/CR3DN3/Heimdall/master/doc/images/screenshot.png)

## Tested on

* macOS Catalina
* Manjaro
* Kali Linux

## Installation

You can download the latest tarball by clicking [here](https://github.com/CR3DN3/Heimdall/tarball/master) or latest zipball by clicking [here](https://github.com/CR3DN3/Heimdall/zipball/master).

    $ git clone --depth 1 https://github.com/CR3DN3/Heimdall.git
    $ cd Heimdall && pip3 install -r requirements.txt

## Usage

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

### Examples

```
./heimdall.py --url www.target.com --wordlist 1
./heimdall.py --url www.target.com --wordlist 2 --user-agent <USER-AGENT>
./heimdall.py --url www.target.com --wordlist extra/wordlists/custom.txt
./heimdall.py --update
```

## Translations

* [English](https://github.com/CR3DN3/Heimdall/blob/master/README.md)
* [Portuguese](https://github.com/CR3DN3/Heimdall/blob/master/doc/translations/README-pt-BR.md)