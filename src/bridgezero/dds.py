#!/usr/bin/env python
import subprocess
import os

def run_script(script):
    result = subprocess.run(['sh', '-c', script], capture_output=True, text=True).stdout
    return result


def run():
    dirname = os.path.dirname(__file__)

    script1 = 'cd ' + dirname + '/../../bin/ && LD_LIBRARY_PATH=. ./ddcalculate '

    script2 = '"N:Q.Q8652.K9765.73 A96532.AT3.32.52 J4.974.JT8.QT864 KT87.KJ.AQ4.AKJ9" ' + \
              '"N:Q.Q8652.K9765.73 KT973.KJ.A42.K92 J4.974.JT8.QT864 A8652.AT3.Q3.AJ5" '

    script = script1 + script2

    print(script)

    print(run_script(script))
