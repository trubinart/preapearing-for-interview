import os

def get_file_name(file):
    path = os.path.abspath(file)
    print (path.split('/')[-1].split('.')[0])

if __name__ == '__main__':
    get_file_name('task_1.py')

