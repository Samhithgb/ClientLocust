import urllib.request
import shutil
import os
import time

URL = 'http://127.0.0.1:5000/'
FILE_NAME = 'downloadedfile'
DOWNLOAD_PERIOD = 100


def run_download(url, file_name):
    while True:
        if os.path.exists(FILE_NAME):
            os.remove(FILE_NAME)
        else:
            print("The file does not exist")

        with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)

        time.sleep(DOWNLOAD_PERIOD)


if __name__ == '__main__':
    run_download(URL, FILE_NAME)
