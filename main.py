import sys
import json
from websites.resources.data import WEBSITES


'''
Prints list in JSON format
'''
def print_json(result: list()):
    json_formatted_str = json.dumps(result, indent=2)

    print(json_formatted_str)


'''
Prints out all the sites that have values greater or equal to four
'''
def task_one():
    result = list()

    for website in WEBSITES:
        if website['value'] >= 4:
            result.append(website)

    print_json(result)

'''
Prints out list with www. prepended to domain
'''
def task_two():
    result = list()

    for website in WEBSITES:
        if website['domain'][:4] != 'www.':
            website['domain'] = 'www.' + website['domain']
        
        result.append(website)

    print_json(result)


'''
Prints out websites list with fixed data
'''
def task_three():
    result = list()

    for website in WEBSITES:
        if 'https://' in website['url'] and website['secure'] == False:
            website['secure'] = True
        elif 'http://' in website['url'] and website['secure'] == True:
            website['secure'] = False
        
        result.append(website)

    print_json(result)


'''
Prints the total value of all sites
'''
def task_four():
    total = 0

    for website in WEBSITES:
        total += website['value']

    print(total)


def main():
    task = int(sys.argv[1])

    if task == 1:
        task_one()
    elif task == 2:
        task_two()
    elif task == 3:
        task_three()
    elif task == 4:
        task_four()
    else:
        print('Invalid number. Please try numbers one through four.')
        return 1


if __name__ == '__main__':
    main()
    