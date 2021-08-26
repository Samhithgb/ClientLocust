import urllib.request
import shutil
import os
import time
import sys
import datetime
import invokust
from locust import HttpUser, between, task

URL = 'http://192.168.110.123:5000/'
DOWNLOAD_PERIOD = 100


class WebsiteUser(HttpUser):
    wait_time = between(1, 3)

    @task()
    def get_home_page(self):
        '''
        Gets /
        '''
        self.client.get("/")


def run_download(url, end_date):
    settings = invokust.create_settings(
        classes=[WebsiteUser],
        host=url,
        num_users=1000,
        spawn_rate=2,
        run_time='3m'
    )

    while True:

        if time.time() > end_date:
            break

        loadtest = invokust.LocustLoadTest(settings)
        loadtest.run()

        time.sleep(DOWNLOAD_PERIOD)


if __name__ == '__main__':
    year = int(sys.argv[1])
    month = int(sys.argv[2])
    day = int(sys.argv[3])

    date = datetime.datetime(year=year, month=month, day=day).timestamp()

    run_download(URL, date)
