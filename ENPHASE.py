#!/usr/bin/env python
from nodes import EnphaseController
import udi_interface
import sys

LOGGER = udi_interface.LOGGER

""" Grab My Controller Node (optional) """

if __name__ == "__main__":
    try:

        polyglot = udi_interface.Interface([EnphaseController])

        polyglot.start()

        control = EnphaseController(
            polyglot, 'controller', 'controller', 'PythonTemplate')

        polyglot.runForever()
    except (KeyboardInterrupt, SystemExit):
        LOGGER.warning("Received interrupt or exit...")

        polyglot.stop()
    except Exception as err:
        LOGGER.error('Excption: {0}'.format(err), exc_info=True)
    sys.exit(0)
