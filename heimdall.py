#!/usr/bin/env python3

import argparse

from src.config import Config
from src.core.color import Color
from src.core.strings import Strings
from src.finder import Finder

from src.utils.update import Update
from src.utils.check import Check
from src.utils.setter import Setter

"""
Resolves some Heimdall 
settings for better operation.
"""
Configuration = Config("Ygor Simões",                  # Author
                       "v4.1-stable",                  # Version
                       "https://github.com/CR3DN3",    # GitHub
                       "https://twitter.com/CR3DN3 ")  # Twitter

configs = Configuration.get_configs()
updates = Configuration.updates()

"""
Try to import libraries.
"""
try:
    from requests import get
except ModuleNotFoundError as ex:
    Color.pl("{!} %s Please install requirements: {R}pip3 install -r requirements.txt{W}" % ex)

"""
Capture all passed 
command line arguments.
"""
parser = argparse.ArgumentParser(add_help=False)

parser.add_argument("-h", "--help",
                    action="store_true",
                    help="Show this help message and exit")

parser.add_argument("-u", "--url",
                    action="store",
                    type=str,
                    default=False,
                    help="Target URL (http://www.site_target.com/)")

parser.add_argument("-w", "--wordlist",
                    action="store",
                    type=str,
                    default="1",
                    help="Set wordlist. Default: 1 (Small) and Max: 3 (Big)")

parser.add_argument("-p", "--proxy",
                    action="store",
                    type=str,
                    default=None,
                    help="Use a proxy to connect to the target URL")

parser.add_argument("--user-agent",
                    action="store",
                    type=str,
                    default=None,
                    help="Customize the User-Agent. Default: Random User-Agent")

parser.add_argument("--update",
                    action="store_true",
                    default=False,
                    help="Upgrade Heimdall to its latest available version")

parser.add_argument("--no-update",
                    action="store_true",
                    default=False,
                    help="Disables the intention of updates")

parser.add_argument("--no-logo",
                    action="store_true",
                    default=False,
                    help="Disable the initial banner")

if __name__ == '__main__':
    """
    Stores all command line arguments 
    passed in the variable.
    """
    args = parser.parse_args()

    """
    Get the Heimdall settings, updates and 
    pass it on to the Strings class.
    """
    String = Strings(configs)

    """
    Print the banner along with 
    Heimdall specifications.
    """
    if not args.no_logo:
        String.banner()
        String.banner_description()

    """
    Check for available updates.
    """
    updates_automatic = updates['updates_automatic']
    if args.no_update:
        updates_automatic = False
    if updates_automatic or args.update:
        Updates = Update(configs, updates)
        if Updates.verify():
            Updates.upgrade()
            exit()

    """
    Activates the "helper()" method if no 
    targets are passed in the arguments.
    """
    if not args.url:
        String.helper()
        exit()
    else:
        """
        Format the target URL accordingly.
        """
        args.url = Configuration.target(args.url)

        """
        Instance the "Request" class.
        Generates a random User-Agent.
        """
        Set = Setter(args)
        args.user_agent = Set.user_agent()

        """
        Formats the selected proxy.
        """
        if args.proxy is not None:
            args.proxy = Set.proxy()

        """
        Instance the "Check" class.
        Checks whether the target is online.
        """
        Checkup = Check(args)
        try:
            Checkup.target()
            Color.pl("{+} Target On: {G}%s{W}" % args.url)
        except Exception as ex:
            Color.pl("{!} Error: %s" % ex)
            Color.pl("{!} Please verify your target.")
            exit()

        """
        Stores the selected word list in the variable.
        """
        args.wordlist = Set.wordlist()

        """
        Instance the "Finder" class.
        Heimdall, find!
        """
        ExploitFinder = Finder(args)
        try:
            ExploitFinder.dashboard()
        except KeyboardInterrupt as ex:
            Color.pl("\n{!} CTRL + C has pressed. %s" % ex)
    Color.pl("{+} Finished!    :)")
