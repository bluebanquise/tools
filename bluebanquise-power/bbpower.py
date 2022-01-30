#!/usr/bin/env python3

# ██████╗ ██╗     ██╗   ██╗███████╗██████╗  █████╗ ███╗   ██╗ ██████╗ ██╗   ██╗██╗███████╗███████╗
# ██╔══██╗██║     ██║   ██║██╔════╝██╔══██╗██╔══██╗████╗  ██║██╔═══██╗██║   ██║██║██╔════╝██╔════╝
# ██████╔╝██║     ██║   ██║█████╗  ██████╔╝███████║██╔██╗ ██║██║   ██║██║   ██║██║███████╗█████╗
# ██╔══██╗██║     ██║   ██║██╔══╝  ██╔══██╗██╔══██║██║╚██╗██║██║▄▄ ██║██║   ██║██║╚════██║██╔══╝
# ██████╔╝███████╗╚██████╔╝███████╗██████╔╝██║  ██║██║ ╚████║╚██████╔╝╚██████╔╝██║███████║███████╗
# ╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝╚══════╝
#
# BlueBanquise Power
# Manage equipment's power
# 2022 - Benoît Leveugle <benoit.leveugle@sphenisc.com>
# https://github.com/bluebanquise/bluebanquise - MIT license

import os
import importlib.util
import time
from argparse import ArgumentParser
import yaml
from ClusterShell.NodeSet import NodeSet
import logging

# Colors, from https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def load_file(filename):
    logging.info(bcolors.OKBLUE+'Loading '+filename+bcolors.ENDC)

    with open(filename, 'r') as f:
        # Select YAML loader (needs PyYAML 5.1+ to be safe)
        if int(yaml.__version__.split('.')[0]) > 5 or (int(yaml.__version__.split('.')[0]) == 5 and int(yaml.__version__.split('.')[1]) >= 1):
            return yaml.load(f, Loader=yaml.FullLoader)
        return yaml.load(f)

if __name__ == '__main__':

    print('\nStarting BlueBanquise Power\n')

    #bbpower_configuration = load_file('/etc/bbpower/config.yml')
    bbpower_configuration = load_file('config.yml')
    bbpower_nodes_data = load_file('nodes.yml')
    plugins_path = bbpower_configuration['plugins_path']

    print(bcolors.OKBLUE+'[INFO] Loading plugins'+bcolors.ENDC)
    plugins = {}
    for f in os.listdir(plugins_path+'/'):
        if os.path.isfile(plugins_path+'/'+f) and f.endswith('.py') and f != 'main.py' and f[:-3] in bbpower_configuration['plugins_list']:
            modname = f[:-3]  # remove '.py' extension
            spec = importlib.util.spec_from_file_location(modname, plugins_path+'/'+f)
            plugins[modname] = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(plugins[modname])

    print(bcolors.OKBLUE+'  Found:'+bcolors.ENDC)
    for plugin in plugins:
        print(bcolors.OKBLUE+'    - '+plugin+bcolors.ENDC)

    # Get arguments passed to bootset
    parser = ArgumentParser()
    parser.add_argument("-n", "--nodes", dest="nodes",
                        help="Target node(s). Use nodeset format for ranges.", metavar="NODE")
    parser.add_argument("-a", "--action", dest="action",
                        help="Action to be done: off, on, cycle, reset, etc.", metavar="ACTION")
    parser.add_argument("-db", "--delay-between", dest="delay_between",
                        help="Add a delay between each nodes action. In seconds.", metavar="DELAY_BETWEEN", default=0)
    passed_arguments = parser.parse_args()

    for node in NodeSet(passed_arguments.nodes):
        plugins[bbpower_nodes_data[node]['power_protocol']].power(node,bbpower_nodes_data[node]['protocol_arguments'],passed_arguments)
        time.sleep(int(passed_arguments.delay_between))