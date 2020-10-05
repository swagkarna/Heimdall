#!/usr/bin/env python3

import os


class Config:
    """
    Constructor and Attributes
    """
    def __init__(self, author, version, github, twitter):
        self._author = author
        self._version = version
        self._github = github
        self._twitter = twitter

    def get_configs(self):
        """
        Returns the settings
        in an object structure.
        """
        configs = {
            "Author": self._author,
            "Version": self._version,
            "GitHub": self._github,
            "Twitter": self._twitter
        }
        return configs

    def updates(self):
        """
        Defines configuration variables
        for the Update class.
        """
        updates = {
            "api_repositorie": "https://api.github.com/repos/CR3DN3/Heimdall/releases",
            "repositorie": self._github + "/Heimdall",
            "updates_automatic": False
        }
        return updates

    @staticmethod
    def target(url):
        """
        Format the target URL accordingly.
        """
        if url[:7] != "http://" and url[:8] != "https://":
            url = "http://" + url
        if url[-1] != "/":
            url = url + "/"
        return url

    @staticmethod
    def target_simple(url):
        """
        Format the target URL as simple.
        """
        if url[:7] == "http://":
            url = url.replace("http://", "")
        elif url[:8] == "https://":
            url = url.replace("https://", "")
        if url[-1] == "/":
            url = url.replace("/", "")
        return url

    # Getters
    @property
    def author(self):
        return self._author

    @property
    def version(self):
        return self._version

    @property
    def os(self):
        return self.os

    @property
    def github(self):
        return self.github

    @property
    def twitter(self):
        return self._twitter


if __name__ == '__main__':
    Configuration = Config("Ygor Simões",  # Author
                           2.0,  # Version
                           "https://github.com/CR3DN3",  # GitHub
                           "https://twitter.com/CR3DN3")  # Twitter

    config = Configuration.get_configs()
    print(config)
