# this script is for pythonista on iOS
# script is just to organize dicts returned from d3 when using
# disguise API on iPhone

import json
import os

jsonDir = './data'
jsonFileName = 'health_returned.json'
jFile = os.path.join(jsonDir, jsonFileName)
with open(jFile, 'r', encoding='utf-8') as jf:
    json_data = json.load(jf)


def print_dict(d, parent_key=''):
    for key, value in d.items():
        new_key = f'{parent_key}.{key}' if parent_key else key
        if isinstance(value, dict):
            print_dict(value, new_key)
        elif isinstance(value, list):
            for idx, item in enumerate(value):
                list_key = f'{new_key}[{idx}]'
                if isinstance(item, dict):
                    print_dict(item, list_key)
                else:
                    print(f'{list_key}: {item}')
        else:
            print(f'{new_key}: {value}')


status_dict = json_data['status']
result_list = json_data['result']

print('\n')

# for key, value in json_data['status'].items():
#     print(f'{key}: {value}')

print_dict(status_dict)

print('\n')

# for key, value in json_data['result'].items():
#     print(f'{key}: {value}')

for i in result_list:
    print_dict(i)
    print('\n')