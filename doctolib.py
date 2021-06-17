import json
import os
import platform
import requests

from datetime import datetime
from headers import doctolib as doctolib_headers
from time import sleep


class Doctolib:

    TODAY = datetime.today().date()
    AVAILABLE = False

    def __init__(self, praxis, api, link, poll, retry):
        self.PRAXIS = praxis
        self.API_URL = api.format(self.TODAY)
        self.APPOINTMENT_URL = link
        self.TIMER = poll
        self.RETRY_COUNT = retry

    def get_avail_appointments(self):
        self.AVAILABLE = False
        results = requests.request(
            headers=doctolib_headers,
            url=self.API_URL,
            method="GET"
        )
        resp_data = json.loads(results.text)
        try:
            if "message" in resp_data:
                print(datetime.now().replace(microsecond=0).time(), " : ", self.PRAXIS, " : ", resp_data["message"])
            else:
                self.AVAILABLE = True
                print(datetime.now().replace(microsecond=0).time(), " : ", self.PRAXIS, " : ", resp_data["availabilities"])
        except Exception as e:
            print(resp_data)
            raise e

    def open_link(self):
        if self.AVAILABLE:
            if platform.system() == "Windows":
                command = "cmd /k start"
            elif platform.system() == "Darwin":
                command = "open"
            else:
                command = ""
            os.system("{} {}".format(command, self.APPOINTMENT_URL))
            sleep(30)  # This will put the execution on hold for 30 seconds after opening the browser
            self.AVAILABLE = False

    def main(self):
        for i in range(self.RETRY_COUNT):
            self.get_avail_appointments()
            self.open_link()
            sleep(self.TIMER)
