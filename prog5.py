def file_reader(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.readlines()
            return contents
    except IOError as error:
        return str(error)

if __name__ == '__main__':
    print(file_reader('dummy_file.txt'))

#OUTPUT:
#['Hey,\n', '    If you are reading this means your code has been excecuted successfully.\n', 'Thanks.']