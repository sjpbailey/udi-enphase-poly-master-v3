#!/usr/bin/env python3
"""
Polyglot v3 node server Enphase
Copyright (C) 2021 Steven Bailey

MIT License
"""
import udi_interface
import sys
from nodes import EnphaseController

LOGGER = udi_interface.LOGGER

if __name__ == "__main__":
    try:
        polyglot = udi_interface.Interface([])
        polyglot.start()

        # Create the controller node
        EnphaseController(polyglot, 'controller', 'controller', 'Enphase')

        # Just sit and wait for events
        polyglot.runForever()
    except (KeyboardInterrupt, SystemExit):
        sys.exit(0)
