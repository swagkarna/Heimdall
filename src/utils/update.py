#!/usr/bin/env python3

import os

from requests import get

from src.config import Config
from src.core.color import Color


class Update:
    """
    Constructor and Attributes
    """
    def __init__(self, configs, updates):
        self._configs = configs
        self._updates = updates

    def verify(self):
        """
        Checks for updates to
        update versions.
        """
        request = get(self._updates['api_repositorie']).json()
        if request[0]['name'] != self._configs['Version']:
            Color.pl("{+} New version avaliabe: {G}%s{W}" % request[0]['name'])
            option = input(Color.s("{+} Do you want to upgrade to the latest version? [Y/n] "))
            if option == "Y" or option == "y" or option == "":
                return True
            elif option == "N" or option == "n":
                Color.pl("{!} Update aborted.\n")
                return False
            else:
                Color.pl("{!} Command not found!\n")
        return False

    def upgrade(self):
        """
        Updates Heimdall to the
        most current version available.
        """
        try:
            Color.pl("{+} Updating...")
            os.system(f"git pull {self._updates['repositorie']}")
            Color.pl("{+} Heimdall was successfully updated.")
        except Exception as ex:
            Color.pl("{!} Could not update.")
            Color.pl("{!} %s" % ex)


if __name__ == '__main__':
    Configuration = Config("Ygor Simões",                  # Author
                           2.0,                            # Version
                           "https://github.com/CR3DN3",    # GitHub
                           "https://twitter.com/CR3DN3 ")  # Twitter
