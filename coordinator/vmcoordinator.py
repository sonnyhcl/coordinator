# -*- coding: UTF-8 -*-
__author__ = 'sonnyhcl'

"""
Vessel/Manager Coordinator
"""
import json
import string
import time

import requests
from requests.auth import HTTPBasicAuth

from coordinator.utils import *


def VMCoordinator(msg):
    """
    :param msg:
    :return:
    """
    msgType = msg.get("msgType")
    if msgType == "Msg_StartMana":
        msg.pop("msgType", None)
        sendMessageToStartProcessInstance(msgType, json.dumps(msg))
