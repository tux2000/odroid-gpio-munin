#!/usr/bin/env python
from __future__ import division
import os
import sys
import time
import re

DS18B20_ID = "28-031500c850ff"
DS18B20_TEMP_RE = re.compile(r't=(?P<temperature>[+-]?\d+)', re.M)


def get_temperature_from_sensor(sensor_name):
    """
    Parse output form the sensor
    """
    sensor_file = os.path.join(
        "/sys/bus/w1/devices/",
        sensor_name,
        "w1_slave")

    timestamp = int(time.time())
    with open(sensor_file, 'r') as f:
        data = f.read()

    found = DS18B20_TEMP_RE.search(data)
    if found is None:
        return (timestamp, None)
    return (timestamp, int(found.group('temperature')) / 1000)


def print_munin_config(action):
    """
    Plugin configuration
    """
    if action == "autoconf":
        print "yes"
        return

    if action == "suggest":
        print "temperature"
        return

    if action != "config":
        return

    print 'graph_title Temperature Monitoring'
    print 'graph_args --base 1000 -l 0'
    print 'graph_vlabel Celsius'
    print 'graph_category temperature'

    print 'temperature.label Temperature (C)'
    print 'temperature.type GAUGE'
    print 'temperature.warning 20:23';
    print 'temperature.critical 18:25';


def print_temperature_for_munin(temperature):
    """
    Print sensor output
    """
    print 'temperature.value {temp}'.format(
        temp=temperature)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print_munin_config(sys.argv[1])
    else: 
        timestamp, temperature =  get_temperature_from_sensor(DS18B20_ID)
        print_temperature_for_munin(temperature)
