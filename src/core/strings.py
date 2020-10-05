#!/usr/bin/env python3

from src.config import Config
from src.core.color import Color


class Strings:
    """
    Constructor and Attributes
    """
    def __init__(self, config):
        self._config = config

    @staticmethod
    def helper():
        print("""
Usage: python3 heimdall.py [-h, --help] [-u, --url] [-w, --wordlist (1, 2, 3)]
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
        """)

    @staticmethod
    def banner():
        """
        Print the pure colored
        Heimdall banner.
        """
        Color.pl(r"""{O}_________________________________________________
                _               _       _ _ 
      /\  /\___(_)_ __ ___   __| | __ _| | |
     / /_/ / _ \ | '_ ` _ \ / _` |/ _` | | |
    / __  /  __/ | | | | | | (_| | (_| | | |
    \/ /_/ \___|_|_| |_| |_|\__,_|\__,_|_|_|{W}""")

    def banner_description(self):
        """
        Print design and
        author specifications.
        """
        print(f"""\n                  Version: {self._config['Version']}
    Author: {self._config['Author']} (Security Researcher)
        GitHub: {self._config['GitHub']}
        Twitter: {self._config['Twitter']}""")
        Color.pl("{O}_________________________________________________{W}\n")


if __name__ == '__main__':
    Configuration = Config("Ygor Simões",                  # Author
                           2.0,                            # Version
                           "https://github.com/CR3DN3",    # GitHub
                           "https://twitter.com/CR3DN3 ")  # Twitter

    configs = Configuration.get_configs()
    String = Strings(configs)
    String.banner()
    String.banner_description()
