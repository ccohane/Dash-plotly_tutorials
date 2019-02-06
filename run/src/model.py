#!usr/lib/bin/activate

#Model to handle backend logic

import pandas as pd
import json, jsonify, requests, pprint

url = "https://api.overwatchleague.com/stats/matches/10528/maps/1"

response=json.loads(requests.get(url).text)
players = response['teams'][0]['players']
#for x in players:
#    pprint.pprint(x)

df= pd.read_json(response)

