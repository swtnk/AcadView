def copy_content(filename1, filename2):
    with open(filename1, 'r') as file1, open(filename2, 'r') as file2:
        data_file1, data_file2 = file1.readlines(), file2.readlines()
        line_in_file1, line_in_file2 = len(data_file1), len(data_file2)
        for i in range(max(line_in_file1, line_in_file2)):
            try:
                print(data_file1[i])
            except IndexError as error:
                pass
            try:
                print(data_file2[i])
            except IndexError as error:
                pass

def main():
    copy_content('dummy_file.txt', 'dummy_file_2.txt')

if __name__ == '__main__':
    main()