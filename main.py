TOTAL_LINES = 80
TOTAL_ROWS = 40
ENCODING = 'cp500'
SPACE = ' '


def write_empty_text_header():
    with open("c:/data/text_header/sgy_file_write.sgy", 'r+b') as f:
        for row in range(TOTAL_ROWS):
            for column in range(TOTAL_LINES):
                f.write(SPACE.encode(ENCODING))


def write_line_to_file(line_number, line, f):
    f.seek(line_number * TOTAL_LINES)
    for letter in line:
        f.write(letter.encode(ENCODING))


def write_text_header():
    with open("c:/data/text_header/text_header.txt", 'r') as text_file:
        text = text_file.readlines()

    with open("c:/data/text_header/sgy_file_write.sgy", 'r+b') as f:
        for line in range(len(text)):
            write_line_to_file(line, text[line], f)


def read_text_header():
    with open("c:/data/text_header/sgy_file_read.sgy", 'rb') as f:
        text_header = f.read(1)
        for row in range(TOTAL_ROWS):
            for column in range(TOTAL_ROWS):
                print(text_header.decode(ENCODING), end='')
                text_header = f.read(1)
            print()


if __name__ == '__main__':
    write_empty_text_header()
    write_text_header()
