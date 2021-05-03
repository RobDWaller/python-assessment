'''
Prints the total value of all sites
'''
def task_four(websites):
    total = 0

    for website in websites:
        try:
            total += website['value']
        except:
            print('Website does not have "value" key or invalid value type.')
            continue

    print(total)

    return total
