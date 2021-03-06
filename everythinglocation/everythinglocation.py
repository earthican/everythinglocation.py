# -*- coding: utf-8 -*-

"""
everythinglocation.everythinglocation
~~~~~~~~~~~~~~~
This module implements the class that makes calls to the everythinglocation API.

:copyright: (c) 2015 by Justin Cano
:license: MIT, see LICENSE for more details
"""
import requests

from .base import Loqate
from .response import ELResponse

class EverythingLocation(Loqate):
    BASE_PATH = 'rest'
    RESOURCES = {
        'version': 'version',
        'authorize': 'authorize.php'
    }

    def __init__(self):
        super(EverythingLocation, self).__init__()
        self.response = self._process(params={}, resource='version') #ELResponse(self._GET(resource='version'))
        self.version = self.response.version

    def verify(self, params, geocode=False):
        params['p'] = 'v'
        if geocode:
            params['p'] += '+g'
        return self._process(params)

    def search(self, params, geocode=False):
        params['p'] = 's'
        if geocode:
            params['p'] += '+g'
        return self._process(params)

    def authorize(self, auth):
        return self._process(auth, resource='authorize')

    def _process(self, params, resource=None):
        return ELResponse(self._GET(params=params, resource=resource))
