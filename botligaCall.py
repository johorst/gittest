import json
import urllib
import os

# command zusammenbauen: machtid und result (3. Stelle am Ausgabe Neuron) token s.u.
mycmd = 'curl -X POST --data "match_id=14181&result=2:1&token=ofdcjlljsn6bv8r3lm1aoib2" http://botliga.de/api/guess'
#    Execute the command (a string) in a subshell.
os.system(mycmd)

