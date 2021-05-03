import sys
import websites
from websites.resources.data import WEBSITES


def main():
    global WEBSITES

    task = int(sys.argv[1])

    result = 0

    if task == 1:
        result = websites.task_one(WEBSITES)
    elif task == 2:
        WEBSITES = websites.task_two(WEBSITES)
    elif task == 3:
        WEBSITES = websites.task_three(WEBSITES)    
    elif task == 4:
        result = websites.task_four(WEBSITES)
    else:
        print('Invalid number. Please try numbers one through four.')
        return 1


if __name__ == '__main__':
    main()
    