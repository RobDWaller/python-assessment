import json

'''
Prints list in JSON format
'''
def print_json(result: list()):
    json_formatted_str = json.dumps(result, indent=2)

    print(json_formatted_str)
