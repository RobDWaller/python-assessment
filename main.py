import sys
import websites
from websites.resources.data import WEBSITES



def main():
    global WEBSITES

    task = int(sys.argv[1])

    if task == 1:
        WEBSITES = websites.task_one()
    elif task == 2:
        WEBSITES = websites.task_two()
    elif task == 3:
        WEBSITES = websites.task_three()    
    elif task == 4:
        websites.task_four()
    else:
        print('Invalid number. Please try numbers one through four.')
        return 1


if __name__ == '__main__':
    main()
    