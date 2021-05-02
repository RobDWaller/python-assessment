from .utils import print_json
from .resources.data import WEBSITES

'''
Prints out all the sites that have values greater or equal to four
'''
def task_one():
    result = list()

    for website in WEBSITES:
        try:
            if website['value'] >= 4:
                result.append(website)
        except:
            print('Website does not have value key.')
            continue

    print_json(result)

    return result
