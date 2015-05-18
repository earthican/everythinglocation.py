# -*- coding: utf-8 -*-

"""
everythinglocation.base
~~~~~~~~~~~~~~~
This module implements the class that makes calls to the everythinglocation API.

:copyright: (c) 2015 by Justin Cano
:license: MIT, see LICENSE for more details
"""
import json, requests, os

from .response import ELResponse

class APIKeyError(Exception):
    pass

class EverythingLocation(object):
    headers = {
        'content-length': '50',
        'keep-alive': 'timeout=1, max=100',
        'connection': 'Keep-Alive',
        'cache-control': 'max-age=0, no-store, no-cache',
        'content-type': 'application/json; charset=utf-8'
    }
    BASE_PATH = ''
    URLS = {
        'version': 'version'
    }

    def __init__(self):
        self.base_uri = 'https://saas.loqate.com/rest'
        path = self._get_path('version')
        self.version = ELResponse(self._GET(path)).version

    def verify(self, params):
        params['p'] = 'v'
        return ELResponse(self._GET(params=params))

    def _get_path(self, key):
        return self.BASE_PATH + self.URLS[key]

    def _get_complete_url(self, path):
        return os.path.join(self.base_uri, path)

    def _get_params(self, params):
        from . import API_KEY
        if not API_KEY:
            raise APIKeyError

        api_dict = {'lqtkey': API_KEY}
        if params:
            params.update(api_dict)
        else:
            params = api_dict
        return params

    def _request(self, method, path, params=None):
        url = self._get_complete_url(path)
        params = self._get_params(params)

        response = requests.request(
            method, url, params=params)

        response.raise_for_status()
        response.encoding = 'utf-8'
        return response.json()

    def _GET(self, path='', params=None):
        return self._request('GET', path, params=params)

    def _POST(self, path, params=None, payload=None):
        return self._request('POST', path, params=params, payload=payload)

    def _DELETE(self, path, params=None, payload=None):
        return self._request('DELETE', path, params=params, payload=payload)
