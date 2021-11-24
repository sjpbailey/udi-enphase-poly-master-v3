
import udi_interface
import sys
import time
import json
import urllib3
import asyncio
import logging

import requests
from requests.auth import HTTPBasicAuth  # HTTP

LOGGER = udi_interface.LOGGER


class SiteNode(udi_interface.Node):
    def __init__(self, polyglot, primary, address, name, key, user_id, system_id):
        super(SiteNode, self).__init__(polyglot, primary, address, name)
        self.poly = polyglot
        self.lpfx = '%s:%s' % (address, name)
        self.poly.subscribe(self.poly.START, self.start, address)
        self.poly.subscribe(self.poly.POLL, self.poll)
        self.key = key
        self.user_id = user_id
        self.system_id = system_id

    def start(self):
        self.goNow(self)
        self.http = urllib3.PoolManager()

    def siteInfo(self, command):
        params = (
            ('key' == self.key),  # '33443540a4c162ed92df1c878e87867b'),
            ('user_id' == self.user_id)  # , '4d6a55794e7a55354d413d3d0a'),
            ('system_id' == self.system_id)  # , '2527105'
        )

        try:
            r = requests.get(
                'https://api.enphaseenergy.com/api/v2/systems/system_id/summary',  params=params)

            #print('\n Summary \n' + response)
            Response = json.loads(r.text)

            LOGGER.info(Response["current_power"])
            self.setDriver('GV1', float(Response["current_power"]/1000))
            LOGGER.info(Response["current_power"])
            self.setDriver('GV2', float(Response["energy_today"]/1000))
            LOGGER.info(Response["current_power"])
            self.setDriver('GV3', float(Response["energy_lifetime"]/1000))
            LOGGER.info(Response["status"])
            self.setDriver('GV4', str(Response["status"]))

            # url, auth=HTTPBasicAuth)
            if r.status_code == requests.codes.ok:
                if self.debug_enable == 'True' or self.debug_enable == 'true':
                    LOGGER.info(r.content)

                return r.content
            else:
                LOGGER.error("get_request:  " + r.content)
                return None

        except requests.exceptions.RequestException as e:
            LOGGER.error("Error: " + str(e))

    def poll(self, polltype):
        if 'shortPoll' in polltype:
            LOGGER.debug('shortPoll (node)')
            self.reportDrivers()
        else:
            self.siteInfo(self)
            LOGGER.debug('longPoll (node)')

    def query(self, command=None):
        self.reportDrivers()

    drivers = [
        {'driver': 'ST', 'value': 0, 'uom': 2},
        {'driver': 'GV1', 'value': 0, 'uom': 56},
        {'driver': 'GV2', 'value': 0, 'uom': 25},
        {'driver': 'GV3', 'value': 0, 'uom': 56},
        {'driver': 'GV4', 'value': 0, 'uom': 25},

    ]

    id = 'site'

    commands = {
        'SITEINFO': siteInfo

    }
