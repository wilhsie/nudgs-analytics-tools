#!/usr/bin/env

"""

    Hello and welcome to the mixed_reality_json_parser.py tool >^ o ^<
    
    Input:
        JSON containing player data created by Mixed Reality
    Output:
        Player name / id
        List of (player action, client time)


"""

import sys
import json

fd = open(sys.argv[1])

# TODO: Handle case where line != type(JSON) i.e. line = # version:1

list_of_player_data = []

for line in fd:
    json_dump = json.dumps(line)
    json_load = json.loads(json_dump)
    json_reload = json.loads(json_load)
    if(json_reload['type'] == "action"):
        list_of_player_data.append([json_reload['data']['details'], json_reload['data']['client_time']])

print list_of_player_data
