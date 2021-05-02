from .utils import print_json
from .resources.data import WEBSITES

'''
Prints out list with www. prepended to domain
'''
def task_two():


    result = list()

    for website in WEBSITES:
        try:
            if website['domain'][:4] != 'www.':
                website['domain'] = 'www.' + website['domain']
            
            result.append(website)
        except:
            print('Website has invalid key.')
            continue

    print_json(result)

    return result
