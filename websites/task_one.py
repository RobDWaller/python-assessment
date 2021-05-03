from .utils import print_json

'''
Prints out all the sites that have values greater or equal to four
'''
def task_one(websites):
    result = list()

    for website in websites:
        try:
            if website['value'] >= 4:
                result.append(website)
        except:
            print('Website does not have value key.')
            continue

    print_json(result)

    return result
