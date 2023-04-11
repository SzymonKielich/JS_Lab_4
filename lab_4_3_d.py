import json
import os
import subprocess
import sys
from collections import Counter

def lab_4_3_d():
    folder_path = sys.argv[1]
    file_stats_list = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if (filename.endswith('.txt')):
            process = subprocess.Popen(['python', 'lab_4_3.py', file_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True, universal_newlines=True)
            file_result, stnrd = process.communicate(input='os.path.join(folder_path, filename)')
            json_stat = json.loads(file_result)
            file_stats_list.append(json_stat)
    total_characters = 0
    total_words = 0
    total_lines = 0

    char_counts = Counter()
    word_counts = Counter()
    for file_stat in file_stats_list:
        total_characters += file_stat['total_chars']
        total_words += file_stat['words_counter']
        total_lines += file_stat['lines_counter']
        char_counts.update(file_stat['most_used_char']['character'])
        word_counts.update(file_stat['most_used_word']['word'])
    print(f'\nFiles read: {len(file_stats_list)}, \nTotal number of characters: {total_characters}, '
          f'\nTotal number of words: {total_words}, \nTotal number of lines: {total_lines},'
          f'\nMost common char: {char_counts.most_common(1)[0][0]}, \n Most common word: {word_counts.most_common(1)[0][0]}')


if __name__ == '__main__':
    if len(sys.argv) != 1:
        lab_4_3_d()

