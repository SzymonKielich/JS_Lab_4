import os
import time
import subprocess
import sys
import json


def make_backup(source_dir):
    ext = 'zip'
    timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
    dirname = os.path.basename(source_dir)
    backup_name = f"{timestamp}-{dirname}.{ext}"
    backups_dir = os.path.join(os.environ.get('BACKUPS_DIR') or os.path.expanduser("~/.backups"))

    if not os.path.exists(backups_dir):
        os.mkdir(backups_dir)

    backup_path = os.path.join(backups_dir, backup_name)

    subprocess.run(f"powershell Compress-Archive -Path {source_dir}\\* -DestinationPath {backup_path}")

    history_of_copies = os.path.join(backups_dir, 'history.json')
    content = {
        'date': timestamp,
        'full_path': backups_dir,
        'name_of_file': backup_name
    }

    with open(history_of_copies, 'a') as file:
        json.dump(content, file, indent=5)
        file.write("\n")

    return backup_path


if __name__ == "__main__":

    if len(sys.argv) != 1:
        folder_path = sys.argv[1]
        print(make_backup(folder_path))
