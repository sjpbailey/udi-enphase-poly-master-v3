"""
Polyglot v3 node server
Copyright (C) 2021 Steven Bailey
MIT License
"""
import udi_interface
from datetime import datetime, timedelta
import json
import urllib3
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
        self.siteInfo(self)
        self.http = urllib3.PoolManager()

    def siteInfo(self, command):
        URL_SITE = 'https://api.enphaseenergy.com/api/v2/systems/'+self.system_id + '/summary'
        params = (('key', self.key), ('user_id', self.user_id))
        try:
            r = requests.get(URL_SITE, params=params)
            #print('\n Summary \n' + response)
            Response = json.loads(r.text)
            LOGGER.info(Response["current_power"])
            # Currently produced kW
            self.setDriver('GV1', float(Response["current_power"]/1000))
            LOGGER.info(Response["current_power"])
            # Todays Current kWh
            self.setDriver('GV2', float(Response["energy_today"]/1000))
            LOGGER.info(Response["current_power"])
            self.setDriver('GV3', float(
                Response["energy_lifetime"]/1000))  # Lifetime kWh
            LOGGER.info(Response["status"])
            normal1 = Response["status"]
            if normal1 == 'normal':
                self.setDriver('GV4', 1)
            else:
                self.setDriver('GV4', 0)
            if r.status_code == 200:
                self.setDriver('ST', 1)
            else:
                self.setDriver('ST', 0)
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
        {'driver': 'GV1', 'value': 0, 'uom': 30},  # Current kW
        {'driver': 'GV2', 'value': 0, 'uom': 33},  # Todays kWh
        {'driver': 'GV3', 'value': 0, 'uom': 33},  # Life Time kWh
        {'driver': 'GV4', 'value': 0, 'uom': 25},

    ]

    id = 'site'

    commands = {
        'SITEINFO': siteInfo

    }
