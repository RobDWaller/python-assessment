from .utils import print_json
from .resources.data import WEBSITES

'''
Prints out websites list with fixed data
'''
def task_three():
    result = list()

    for website in WEBSITES:
        try:
            if 'https://' in website['url'] and website['secure'] == False:
                website['secure'] = True
            elif 'http://' in website['url'] and website['secure'] == True:
                website['secure'] = False
            
            result.append(website)
        except:
            print('Website has invalid key(s).')
            continue

    print_json(result)

    return result
