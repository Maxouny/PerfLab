import json

def recursive_items(dictionary):
    for key, value in dictionary.items():
        if type(value) is dict:
            yield (key, dictionary)
            yield from recursive_items(value)
        elif type(value) is list:
            for item in value:
               yield from recursive_items(item)
        else:
            yield (key, dictionary)

with open('tests.json', 'r') as f_tests, open('values.json', 'r') as f_values:
    tests = json.load(f_tests)
    values = json.load(f_values)

dict_values = {}
for item in values['values']:
    dict_values[item['id']] = item['value']

for key, dict_tests in recursive_items(tests):
    if key == 'id' and dict_tests.get('value') != None:
        id_value = dict_tests[key]  
        dict_tests['value'] = dict_values[id_value]

with open('report.json', 'w') as f_report:
    json.dump(tests, f_report)