import os
import json
import pprint
config = json.loads(open('obj.json').read())
first = config[0]['friends'][1]['name']

pprint.pprint(first)