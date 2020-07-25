#!/usr/bin/env python3

import sys
import json
from datetime import datetime
from icmplib import ping, traceroute


# Some internet-based IP we will use
remoteTarget = 'www.starlink.com'

class NetCheck(object):
    data = {
        "host": None,
        "link_quality": "Not checked yet",
        "speed_test": "Not checked yet",
        "is_alive": "unknown",
        "last_seen_alive": None,
        }

    status = 'unknown'

    # This list contains previous link_quality measurements.
    history = []
    # This is how many measurements we should remember
    history_len = 10

    net_path = None

    def __init__(self, host=remoteTarget, history_len = 10):
        self.data["host"] = host
        self.history_len = history_len

    def __repr__(self):
        return json.dumps(self.data)
                
    def __str__(self):
        str_out = "Host %s:\n" % self.data["host"]
        str_out += "  Link Quality: %s\n" % self.data["link_quality"]
        str_out += "  Speed Test Result: %s\n" % self.data["speed_Test"]
        return str_out

    def _update_quality(self, quality):
        """ quality is an integer between 0 and 100 """
        pass

    def check_alive(self):
        ping_res = ping(host, count=3, interval=0.1, timeout=1)
        self.data["is_alive"] = ping_res.is_alive
        if ping_res.is_alive:
            self.data['last_seen_alive'] = datetime.now()
    
    def check_link_quality(self):
        """ Actually determine the quality of the link """ 
        pass

    
   
