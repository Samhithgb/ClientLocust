import urllib.request
import shutil
import os
import time
import sys
import datetime

URL = 'http://127.0.0.1:5000/download'
FILE_NAME = 'downloadedfile'
DOWNLOAD_PERIOD = 100


def run_download(url, file_name, end_date):
    while True:

        if time.time() > end_date:
            print("Reached end date. Quitting")
            break

        if os.path.exists(FILE_NAME):
            os.remove(FILE_NAME)
        else:
            print("The file does not exist")

        with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)

        time.sleep(DOWNLOAD_PERIOD)


if __name__ == '__main__':
    year = int(sys.argv[1])
    month = int(sys.argv[2])
    day = int(sys.argv[3])

    date = datetime.datetime(year=year, month=month, day=day).timestamp()

    run_download(URL, FILE_NAME, date)
