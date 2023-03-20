#!/usr/bin/env python
import subprocess
import os

from bridgezero import constants


def run_script(script: str):
    return subprocess.run(['sh', '-c', script], capture_output=True, text=True).stdout

def dds_parse_result(line: str):
    tricks = {'N': {}, 'E': {}, 'S': {}, 'W': {}}
    arr = line.split(',')
    iter = 0
    for player_name in constants.PLAYERS_NAMES:
        for bid_color in constants.BIDS_COLORS:
            tricks[player_name][bid_color] = arr[iter]
            iter += 1

    return tricks


def run_dds(deals):
    dirname = os.path.dirname(__file__)
    script = 'cd ' + dirname + '/../../bin/ && LD_LIBRARY_PATH=. ./ddcalculate '

    params = ''
    for deal in deals:
        params = ' "' + deal.get_as_PBN() + '"'
#    params = '"N:Q.Q8652.K9765.73 A96532.AT3.32.52 J4.974.JT8.QT864 KT87.KJ.AQ4.AKJ9" '

    result = run_script(script + params)
    lines = result.split('\n')

    dd_results = []
    for line in lines:
        if not line:
            continue
        dd_results.append(dds_parse_result(line))

    return dd_results
