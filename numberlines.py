import sys
import os

def number(line_number, input):
    return '{:>4} {}'.format(line_number, input)

files = sys.argv[1:]
for file in files:
    try:
        with open(file, encoding='utf-8') as input_file:
            print('Processing {}'.format(file))
            input_file_parts = os.path.splitext(file)
            output_filename = ''.join((input_file_parts[0], '_numbered',
                                       input_file_parts[1]))
            with open(output_filename, mode='w', encoding='utf-8') as output_file:
                line_number = 0
                for line in input_file:
                    line_number += 1
                    output_file.write('{:>4} {}'.format(line_number, line))
    except FileNotFoundError:
        continue
    except IsADirectoryError:
        continue
    except UnicodeDecodeError:
        continue
