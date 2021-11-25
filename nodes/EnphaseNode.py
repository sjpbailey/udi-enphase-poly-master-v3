
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
            self.setDriver('GV1', float(Response["current_power"]/1000))
            LOGGER.info(Response["current_kWh"]/1000)
            self.setDriver('GV2', float(Response["energy_today"]/1000))
            LOGGER.info(Response["energy_lifetime"]/1000)
            self.setDriver('GV3', float(Response["energy_lifetime"]/1000))
            LOGGER.info(Response["status"])
            self.setDriver('GV4', str(Response["status"]))

            if r.status_code == 200:
                self.setDriver('ST', 1)
            else:
                self.setDriver('ST', 0)
        except requests.exceptions.RequestException as e:
            LOGGER.error("Error: " + str(e))

    def siteHist(self, command):
        presentday = datetime.now()
        yesterday = presentday - timedelta(1)
        start_date = yesterday.strftime('%Y-%m-%d')
        end_date = presentday.strftime('%Y-%m-%d')
        LOGGER.info(start_date)
        LOGGER.info(end_date)
        URL_HIST = 'https://api.enphaseenergy.com/api/v2/systems/2527105/energy_lifetime?start_date=' + \
            start_date+'&end_date='+end_date
        params = (('key', self.key), ('user_id', self.user_id))

        try:
            r = requests.get(URL_HIST, params=params)
            #print('\n Summary \n' + response)
            Response = json.loads(r.text)

            LOGGER.info(Response)
            self.setDriver('GV5', float(Response/1000))

            # LOGGER.info(Response["current_power"])
            #self.setDriver('GV2', float(Response["energy_today"]/1000))
            # LOGGER.info(Response["current_power"])
            #self.setDriver('GV3', float(Response["energy_lifetime"]/1000))
            # LOGGER.info(Response["status"])
            #self.setDriver('GV4', str(Response["status"]))

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
        {'driver': 'GV1', 'value': 0, 'uom': 56},
        {'driver': 'GV2', 'value': 0, 'uom': 56},
        {'driver': 'GV3', 'value': 0, 'uom': 56},
        {'driver': 'GV4', 'value': 0, 'uom': 25},
        {'driver': 'GV5', 'value': 0, 'uom': 56},

    ]

    id = 'site'

    commands = {
        'SITEINFO': siteInfo

    }
