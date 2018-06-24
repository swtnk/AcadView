import re
def word_freq_counter(filename):
    with open(filename, 'r') as file:
        content_array = re.split(r'\.|\n|\t|\,|\ ', file.read())
        return {x : content_array.count(x) for x in set(content_array)}
def main():
    print(word_freq_counter('dummy_file.txt'))

if __name__ == '__main__':
    main()

#OUTPUT:
#{'': 7, 'this': 1, 'are': 1, 'excecuted': 1, 'has': 1, 'successfully': 1, 'Thanks': 1, 'reading': 1, 'your': 1, 'code': 1, 'been': 1, 'means': 1, 'you': 1, 'If': 1, 'Hey': 1}