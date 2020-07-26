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
        "packet_loss": None,
        "recorded_at": None,
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

    def check_alive(self):
        ping_res = ping('www.starlink.com', count=3, interval=0.1, timeout=1)
        #ping_res = ping(self.data["host"], count=3, interval=0.1, timeout=1)
        self.data["is_alive"] = ping_res.is_alive
        if ping_res.is_alive:
            self.data['last_seen_alive'] = datetime.now().strftime("%H:%M:%S")
        return ping_res.is_alive
    
    def check_link_quality(self):
        """ Actually determine the quality of the link """ 
        res = ping(self.data['host'], count=10, interval=0.1, timeout=0.5)

        # packet_loss is a percent
        self.data['packet_loss'] = int(round(res.packet_loss, 2) * 100) 

        # link quality is judged to be the maximum distance from average
        # on the min or max rtt time. Basically, closer numbers to the average
        # are better, because they indicate less jitter. Units are in ms. 
        min_diff = res.avg_rtt - res.min_rtt
        max_diff = res.max_rtt - res.avg_rtt
        self.data["link_quality"] = 100 - int(round(max(min_diff, max_diff), 0))
        return self.data["link_quality"]

    def update(self):
        """ Run all of the selfchecks to update the status. """
        if self.check_alive():
            self.check_link_quality()
        else:
            self.data["link_quality"] = 0
            self.data["packet_loss"] = 100
        self.data['recorded_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
        self.history.append(self.data.copy())
        if len(self.history) > 10:
            self.history.pop(0)
            
    
   
