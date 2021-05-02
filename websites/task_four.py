from .resources.data import WEBSITES

'''
Prints the total value of all sites
'''
def task_four():
    total = 0

    for website in WEBSITES:
        try:
            total += website['value']
        except:
            print('Website does not have "value" key or invalid value type.')
            continue

    print(total)

    return total
