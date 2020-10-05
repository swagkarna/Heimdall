#!/usr/bin/env python3

import os
from random import choice

from src.config import Config
from src.core.color import Color


class Setter:
    def __init__(self, args):
        self._proxy = args.proxy
        self._user_agent = args.user_agent
        self._wordlist = args.wordlist

    def proxy(self):
        """
        Formats the selected proxy accordingly.
        """
        if self._proxy is not None:
            if self._proxy[:7] == "http://":
                self._proxy = {'http://': self._proxy}
                Color.pl("{+} Proxy: %s" % self._proxy['http://'])
            elif self._proxy[:8] == "https://":
                self._proxy = {'https://': self._proxy}
                Color.pl("{+} Proxy: %s" % self._proxy['https://'])
            elif self._proxy[:3] == "ftp":
                self._proxy = {'ftp': self._proxy}
                Color.pl("{+} Proxy: %s" % self._proxy['ftp'])
            else:
                self._proxy = ""
            return self._proxy

    def user_agent(self):
        """
        Method that reads text files containing thousands of User-Agents
        using the "random" library to generate just one random User-Agent.
        """
        if self._user_agent is not None:
            return self._user_agent
        else:
            user_agent_chrome_text = open(os.path.realpath("extra/user-agents/Chrome.txt"), 'r')
            chrome = user_agent_chrome_text.readlines()
            user_agent_chrome_text.close()

            user_agent_edge_text = open(os.path.realpath("extra/user-agents/Edge.txt"), 'r')
            edge = user_agent_edge_text.readlines()
            user_agent_edge_text.close()

            user_agent_firefox_text = open(os.path.realpath("extra/user-agents/Firefox.txt"), 'r')
            firefox = user_agent_firefox_text.readlines()
            user_agent_firefox_text.close()

            user_agent_opera_text = open(os.path.realpath("extra/user-agents/Opera.txt"), 'r')
            opera = user_agent_opera_text.readlines()
            user_agent_opera_text.close()

            user_agent_safari_text = open(os.path.realpath("extra/user-agents/Safari.txt"), 'r')
            safari = user_agent_safari_text.readlines()
            user_agent_safari_text.close()

            user_agents = chrome + edge + firefox + opera + safari
            random_agent = choice(user_agents).rstrip('\n')

            random_agent = {'User-Agent': random_agent}

        """
        Returns the random User-Agent.
        """
        return random_agent

    def wordlist(self):
        """
        Opens the text files containing the wordlist.
        """
        if self._wordlist == "1":
            wordlist_text = open(os.path.realpath("extra/wordlists/small.txt"), 'r')
            Color.pl("{+} Wordlist Small: 'extra/wordlists/small.txt'")
        elif self._wordlist == "2":
            wordlist_text = open(os.path.realpath("extra/wordlists/medium.txt"), 'r')
            Color.pl("{+} Wordlist Medium: 'extra/wordlists/medium.txt'")
        elif self._wordlist == "3":
            wordlist_text = open(os.path.realpath("extra/wordlists/big.txt"), 'r')
            Color.pl("{+} Wordlist Big: 'extra/wordlists/big.txt'")
        else:
            Color.pl("{+} Wordlist Alternative: %s" % self.wordlist())
            wordlist_text = open(self._wordlist, 'r')

        wordlist = wordlist_text.readlines()
        wordlist_text.close()

        """
        Returns the selected wordlist.
        """
        return wordlist


if __name__ == '__main__':
    Configuration = Config("Ygor Simões",                  # Author
                           2.0,                            # Version
                           "https://github.com/CR3DN3",    # GitHub
                           "https://twitter.com/CR3DN3")  # Twitter
