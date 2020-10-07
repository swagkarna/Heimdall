# ⚡️ Heimdall ⚡️
[![Build Status](https://travis-ci.org/CR3DN3/Heimdall.svg?branch=master)](https://travis-ci.org/CR3DN3/Heimdall) [![License](https://img.shields.io/badge/License-MIT-critical.svg?style=flat&logo=)](https://github.com/CR3DN3/Heimdall/blob/master/LICENSE) [![Python3.8](https://img.shields.io/badge/Python-3.8-yellow.svg?style=flat&logo=python)](https://www.python.org/) [![Releases](https://img.shields.io/badge/release-v4.0--stable-green)](https://github.com/CR3DN3/Heimdall/releases/tag/v4.0-stable)


Heimdall is an open source tool designed to automate fetching from a target site's admin panel using brute force in the wordlist. Developed entirely in Python, it has simple didactic code for study, and is an ideal tool for hacking arsenal.

![HeimdallGif](https://raw.githubusercontent.com/CR3DN3/Heimdall/master/doc/images/heimdall.gif)

## Required

It is extremely important that you have the mandatory tools listed below for Heimdall to work as expected.
It is recommended that you use an operating system with a focus on Pentest.

* [`python`](https://www.python.org/): (Only version 3 of python is supported.)
* [`requests`](https://requests.readthedocs.io/) "A simple, yet elegant HTTP library."

## Installation

You can download the latest tarball by clicking [here](https://github.com/CR3DN3/Heimdall/tarball/master) or latest zipball by clicking [here](https://github.com/CR3DN3/Heimdall/zipball/master).

    $ git clone https://github.com/CR3DN3/Heimdall.git
    $ cd Heimdall && pip install -r requirements.txt

## Usage

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

## Screenshots

![Screenshot](https://raw.githubusercontent.com/CR3DN3/Heimdall/master/doc/images/screenshots/screenshot.png)

You can visit the collection of screenshots that demonstrate how it works on some platforms by clicking [here](https://github.com/CR3DN3/Heimdall/tree/master/doc/images/screenshots).

### Examples

```
./heimdall.py --url www.site_target.com --wordlist 1
./heimdall.py --url www.site_target.com --wordlist 2 --user-agent <USER-AGENT>
./heimdall.py --url www.site_target.com --wordlist extra/wordlists/custom.txt
./heimdall.py --update
```

## Translations

* [English](https://github.com/CR3DN3/Heimdall/blob/master/README.md)
* [Portuguese](https://github.com/CR3DN3/Heimdall/blob/master/doc/translations/README-pt-BR.md)

# Author
* Ygor Simões (CR3DN3) - [![GitHub](https://img.shields.io/badge/GitHub-CR3DN3-inactive.svg?style=social&logo=github)](https://github.com/CR3DN3/)
[![Facebook](https://img.shields.io/badge/Facebook-inactive.svg?style=social&logo=Facebook)](https://www.facebook.com/oldygor/)
[![Twitter](https://img.shields.io/badge/Twitter-CR3DN3-inactive.svg?style=social&logo=twitter)](https://twitter.com/CR3DN3/)
[![Instagram](https://img.shields.io/badge/Instagram-inactive.svg?style=social&logo=Instagram)](https://instagram.com/oldygor)