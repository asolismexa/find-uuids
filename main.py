import os
import re
import csv
from glob import glob

root_dir = r"C:\Users\Desarrollo\Downloads\comp"
extension = '*.sat'
uuids_file = 'uuids.csv'


def main():
    uuids = []
    for dirpath, dirnames, files in os.walk(root_dir):
        for file in glob(os.path.join(dirpath, extension)):
            # Read the file
            with open(file, 'r') as f:
                text = f.read()

                # Use a regular expression to match the UUID
                match = re.search(r'UUID=([A-Fa-f0-9-]+)', text)

                if match:
                    uuid = match.group(1)
                    uuids.append(uuid)
                else:
                    print("UUID not found.")

    with open(uuids_file, 'w', newline='') as csvfile:
        for uuid in uuids:
            writer = csv.writer(csvfile)
            writer.writerow([uuid])


if __name__ == '__main__':
    main()
