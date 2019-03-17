#!/usr/bin/env python

__author__ = "mhoelzer"


import argparse
import sys
import requests


def get_astronauts():
    url = "http://api.open-notify.org/astros.json"
    request = requests.get(url)
    return request.json()


def create_parser():
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text.")
    parser.add_argument(
        "-a", "--astronauts", help="search for an astronaut")
    return parser


def main():
    parser = create_parser()
    namespace = parser.parse_args()
    if not namespace:
        parser.print_usage()
        sys.exit(1)
    if namespace.astronauts:
        # print("{} is currently aboard the {}.".format(name, craft))
        # print("There are currently {} astronauts in space.".format(number))
        pass


if __name__ == '__main__':
    main()
