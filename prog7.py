def copy_content(filename1, filename2):
    with open(filename1, 'r') as file1, open(filename2, 'w+') as file2:
        file2.write(file1.read())
        file2.seek(0,0)
        return(file2.read())

def main():
    print(copy_content('dummy_file.txt', 'dummy_file_2.txt'))

if __name__ == '__main__':
    main()