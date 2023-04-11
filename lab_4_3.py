import os
import sys
from collections import Counter
import json


def lab_4_3():
    file_path = sys.argv[1]
    file_reader = open(file_path, 'r')
    characters_counter = 0
    words_counter = 0
    lines_counter = 0

    for line in file_reader:
        line = line.strip(os.linesep)
        words_counter += len(line.split())
        characters_counter += len(line)
        lines_counter += 1

    file_reader.seek(0)
    full_text = file_reader.read()
    most_used_chars_dict = Counter(full_text)

    most_used_words_dict = Counter(full_text.split())

    results = {
        'file_path': file_path,
        'total_chars': characters_counter,
        'words_counter': words_counter,
        'lines_counter': lines_counter,
        'most_used_char': {
            'character': most_used_chars_dict.most_common(1)[0][0],
            'count': most_used_chars_dict.most_common(1)[0][1]
        },
        'most_used_word': {
            'word': most_used_words_dict.most_common(1)[0][0],
            'count': most_used_words_dict.most_common(1)[0][1],
        }
    }

    print(json.dumps(results, indent=4))


if __name__ == '__main__':

    if len(sys.argv) != 1:
        lab_4_3()
