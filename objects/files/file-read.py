import os


def run():
    file_path = '{}/objects/files/file-read.txt'.format(os.getcwd())
    counter = 0

    with open(file_path, 'r') as f:
        for line in f:
            counter += line.count('Lorem')

    print('Lorem se encuentra {} veces'.format(counter))

if __name__ == '__main__':
    run()
