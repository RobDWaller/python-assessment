import copy
from .utils import print_json

'''
Prints out list with www. prepended to domain
'''
def task_two(websites):
    result = list()
    index = 0
    incorrect_elements = list()

    for website in websites:
        try:
            if website['domain'][:4] != 'www.':
                website['domain'] = 'www.' + website['domain']
        except:
            incorrect_elements.append(index)
            print('Website has invalid key.')
            continue
            
        index += 1

    for i in reversed(incorrect_elements):
        del websites[i]

    print_json(websites)
