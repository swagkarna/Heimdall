#!/usr/bin/env python3

from requests import get


class Check:
    def __init__(self, args):
        """
        Constructor and Attributes
        """
        self._url = args.url
        self._agent = args.user_agent
        self._proxy = args.proxy

    def target(self):
        """
        Make a request to the target.
        """
        request = get(self._url, proxies=self._proxy, headers=self._agent)
