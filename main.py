from pathlib import Path

TOTAL_LINES = 80
TOTAL_ROWS = 40
ENCODING = 'cp500'
SPACE = ' '
OUTPUT_FILE = "c:/data/text_header/sgy_file_write.sgy"
TEXT_FILE = "c:/data/text_header/text_header.txt"
DIR_PATH = "c:/data/text_header/data/"


def write_empty_text_header(file_name):
    with open(file_name, 'r+b') as f:
        for row in range(TOTAL_ROWS):
            for column in range(TOTAL_LINES):
                f.write(SPACE.encode(ENCODING))


def write_line_to_file(line_number, line, f):
    f.seek(line_number * TOTAL_LINES)
    for letter in line:
        f.write(letter.encode(ENCODING))


def write_text_header(text, output_file_name):
    with open(output_file_name, 'r+b') as f:
        for line in range(len(text)):
            write_line_to_file(line, text[line], f)


def read_text_header(file_name):
    with open(file_name, 'rb') as f:
        text_header = f.read(1)
        for row in range(TOTAL_ROWS):
            for column in range(TOTAL_ROWS):
                print(text_header.decode(ENCODING), end='')
                text_header = f.read(1)
            print()


def run():
    base_path = Path(DIR_PATH)

    with open(TEXT_FILE, 'r') as text_file:
        text = text_file.readlines()

    files_in_base_path = (entry for entry in base_path.iterdir() if entry.is_file())
    for output_file_name in files_in_base_path:
        write_empty_text_header(output_file_name)
        write_text_header(text, output_file_name)


if __name__ == '__main__':
    run()
