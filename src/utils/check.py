#!/usr/bin/env python3

from requests import get
from src.core.color import Color


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
        Handling and preparing the args.url.
        """
        try:
            request = get(self._url, proxies=self._proxy, headers=self._agent)
            Color.pl("{+} Tagert On: {G}%s{W}" % self._url)
        except Exception as ex:
            Color.pl("{!} [%s]" % request.status_code)
            Color.pl("{!} %s" % ex)
            Color.pl("{!} Please verify your target.")
