import json
from haralyzer import HarParser, HarPage
with open('10.2.9.136.har', 'r') as f:
    har_parser = HarParser(json.loads(f.read()))

data = har_parser.har_data
# print(type(data), data.keys())

# print(har_parser.har_data["entries"][10].keys())
# print(len(har_parser.har_data["entries"][10]['_webSocketMessages']))
entries = []
dict_data = {}
for entry in har_parser.har_data["entries"][10]['_webSocketMessages']:    
    if entry['data'].startswith("{"):
        data = json.loads(entry['data'])
        if data['type'] == 3:
            # print(data)
            entry['data'] = data
            entries.append(entry)
dict_data['WS'] = entries
with open('data.json', 'w') as fp:
    json.dump(dict_data, fp)