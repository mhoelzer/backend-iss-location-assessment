#!/usr/bin/env python

__author__ = "mhoelzer"


import requests


def get_astronauts():
    url = "http://api.open-notify.org/astros.json"
    request = requests.get(url)
    req_data = request.json()
    print("There are currently {} astronauts in space.".format(
        req_data["number"]))
    for person in req_data["people"]:
        print("{} is currently aboard the {}.".format(
            person["name"], person["craft"]))


def main():
    get_astronauts()


if __name__ == '__main__':
    main()
