#!/usr/bin/env

"""

    Hello and welcome to the mixed_reality_json_parser.py tool >^ o ^<
    
    Input:
        JSON containing player data created by Mixed Reality
    Output:
        Player name / id
        List of (player action, client time)


    byteify function:
    http://stackoverflow.com/questions/956867/how-to-get-string-objects-instead-of-unicode-ones-from-json-in-python

"""

import sys
import json

# TODO: Handle case where line != type(JSON) i.e. line = # version:1
# TODO: Grab player name and score

def main():
    list_of_player_data = []
    fd = open(sys.argv[1])

    for line in fd:
        json_dump = json.dumps(line)
	json_load = json.loads(line)

	if(json_load['type'] == "action"):
            player_action = byteify(json_load['data']['details']['key'])
            client_time = byteify(json_load['data']['client_time'])
            list_of_player_data.append([player_action, client_time])

    print list_of_player_data



###  Helper functions

def byteify(input):
    if isinstance(input, dict):
        return {byteify(key):byteify(value) for key,value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input


if __name__ == '__main__':
    main()

