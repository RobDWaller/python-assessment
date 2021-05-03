import copy
from .utils import print_json

'''
Prints out websites list with fixed data
'''
def task_three(websites):
    index = 0
    incorrect_elements = list()

    for website in websites:
        try:
            if 'https://' in website['url'] and website['secure'] == False:
                website['secure'] = True
            elif 'http://' in website['url'] and website['secure'] == True:
                website['secure'] = False
        except:
            incorrect_elements.append(index)
            print('Website has invalid key(s).')
            continue

        index += 1


    for i in reversed(incorrect_elements):
        del websites[i]

    print_json(websites)

    return websites
