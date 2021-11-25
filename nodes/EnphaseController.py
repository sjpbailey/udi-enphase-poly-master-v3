import requests
from requests.auth import HTTPBasicAuth
import json
import logging
import udi_interface

from nodes import EnphaseNode

LOGGER = udi_interface.LOGGER
LOG_HANDLER = udi_interface.LOG_HANDLER
Custom = udi_interface.Custom
ISY = udi_interface.ISY

# IF you want a different log format than the current default
LOG_HANDLER.set_log_format(
    '%(asctime)s %(threadName)-10s %(name)-18s %(levelname)-8s %(module)s:%(funcName)s: %(message)s')


class Controller(udi_interface.Node):
    def __init__(self, polyglot, primary, address, name):
        super(Controller, self).__init__(
            polyglot, primary, address, name)
        self.poly = polyglot
        self.name = 'Enphase Site Controller'
        self.hb = 0
        self.Parameters = Custom(polyglot, 'customparams')
        self.Notices = Custom(polyglot, 'notices')
        self.TypedParameters = Custom(polyglot, 'customtypedparams')
        self.TypedData = Custom(polyglot, 'customtypeddata')
        self.poly.subscribe(self.poly.START, self.start, address)
        self.poly.subscribe(self.poly.LOGLEVEL, self.handleLevelChange)
        self.poly.subscribe(self.poly.CUSTOMPARAMS, self.parameterHandler)
        self.poly.ready()
        self.poly.addNode(self)

    def start(self):
        self.poly.updateProfile()
        self.poly.setCustomParamsDoc()
        self.discover()

    # key '33443540a4c162ed92df1c878e87867b'),
    # user_id '4d6a55794e7a55354d413d3d0a'),
    # system_id '2527105'

    def get_request(self, url):
        params = (
            ('key', self.key),
            ('user_id', self.user_id),
            ('system_id', self.system_id),
        )

        try:
            r = requests.get(
                'https://api.enphaseenergy.com/api/v2/systems/'+self.system_id+'/systems',  params=params)

            #print('\n Summary \n' + response)
            Response = json.loads(r.text)

            LOGGER.info('\n System ID \n', Response["systems"][0]["system_id"])

            # url, auth=HTTPBasicAuth)
            # if r.status_code == requests.codes.ok:
            #    if self.debug_enable == 'True' or self.debug_enable == 'true':
            #        LOGGER.info(r.content)

            #    return r.content
            # else:
            #    LOGGER.error("get_request:  " + r.content)
            #    return None

        except requests.exceptions.RequestException as e:
            LOGGER.error("Error: " + str(e))

    def parameterHandler(self, params):
        self.Parameters.load(params)
        LOGGER.debug('Loading parameters now')
        self.check_params()

    def handleLevelChange(self, level):
        LOGGER.info('New log level: {}'.format(level))

    def query(self, command=None):
        nodes = self.poly.getNodes()
        for node in nodes:
            nodes[node].reportDrivers()

    def discover(self, *args, **kwargs):
        node = EnphaseNode.SiteNode(self.poly, self.address,
                                    'site', 'loads', self.key, self.user_id, self.system_id)
        self.poly.addNode(node)

    def delete(self):
        LOGGER.info('deleted.')

    def stop(self):
        LOGGER.debug('NodeServer stopped.')

    def set_module_logs(self, level):
        logging.getLogger('urllib3').setLevel(level)

    def check_params(self):
        self.Notices.clear()
        default_key = "YourApiKey"
        default_user_id = "YourUser_id"
        default_system_id = "YourSystem_id"

        self.key = self.Parameters.key
        if self.key is None:
            self.key = default_key
            LOGGER.error(
                'check_params: key not defined in customParams, please add it.  Using {}'.format(default_key))
            self.key = default_key, self.user = self.Parameters.user

        self.user_id = self.Parameters.user_id
        if self.user_id is None:
            self.user_id = default_user_id
            LOGGER.error('check_params: user_id not defined in customParams, please add it.  Using {}'.format(
                default_user_id))
            self.user_id = default_user_id

        self.system_id = self.Parameters.system_id
        if self.system_id is None:
            self.system_id = default_system_id
            LOGGER.error('check_params: system_id not defined in customParams, please add it.  Using {}'.format(
                default_system_id))
            self.system_id = default_system_id

        # Add a notice if they need to change the user/user_id from the default.
        if self.key == default_key or self.user_id == default_user_id or self.system_id == default_system_id:
            self.Notices['auth'] = 'Please set proper email and user_id in configuration page'
            self.setDriver('ST', 0)
        else:
            self.setDriver('ST', 1)

    def remove_notices_all(self, command):
        LOGGER.info('remove_notices_all: notices={}'.format(self.Notices))
        # Remove all existing notices
        self.Notices.clear()

    id = 'ctl'

    commands = {
        'QUERY': query,
        'REMOVE_NOTICES_ALL': remove_notices_all,
    }

    drivers = [
        {'driver': 'ST', 'value': 1, 'uom': 2},

    ]
