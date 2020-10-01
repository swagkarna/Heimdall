#!/usr/bin/env python3

from random import choice

def Random():

    UAChrome = open('extra/user-agents/Chrome.txt', 'r')
    Chrome = UAChrome.readlines()
    UAChrome.close()

    UAEdge = open('extra/user-agents/Edge.txt', 'r')
    Edge = UAEdge.readlines()
    UAEdge.close()

    UAFirefox = open('extra/user-agents/Firefox.txt', 'r')
    Firefox = UAFirefox.readlines()
    UAFirefox.close()

    UAOpera = open('extra/user-agents/Firefox.txt', 'r')
    Opera = UAOpera.readlines()
    UAOpera.close()

    UASafari = open('extra/user-agents/Firefox.txt', 'r')
    Safari = UASafari.readlines()
    UASafari.close()

    UserAgent = Chrome + Edge + Firefox + Opera + Safari
    RandomUserAgent = choice(UserAgent).rstrip('\n')

    return RandomUserAgent
