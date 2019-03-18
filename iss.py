#!/usr/bin/env python

__author__ = "mhoelzer"


import requests
import time
import turtle


def get_astronauts():
    url = "http://api.open-notify.org/astros.json"
    request = requests.get(url)
    req_data = request.json()
    print("There are currently {} astronauts in space.".format(
        req_data["number"]))
    for person in req_data["people"]:
        print("{} is currently aboard the {}.".format(
            person["name"], person["craft"]))


def geographic_coordinates():
    url = "http://api.open-notify.org/iss-now.json"
    request = requests.get(url)
    req_data = request.json()
    longitude = req_data["iss_position"]["longitude"]
    latitude = req_data["iss_position"]["latitude"]
    timestamp = time.ctime(req_data["timestamp"])
    print("Longitude: {}".format(longitude))
    print("Latitude: {}".format(latitude))
    print("Timestamp: {}".format(timestamp))
    return req_data


def iss_coordinates():
    req_data = geographic_coordinates()
    longitude = req_data["iss_position"]["longitude"]
    latitude = req_data["iss_position"]["latitude"]

    screen = turtle.Screen()
    screen.setup(width=720, height=360, startx=None, starty=None)
    screen.bgpic("map.gif")
    screen.setworldcoordinates(-180, -90, 180, 90)

    iss_screen = turtle.Turtle()
    screen.register_shape("iss.gif")
    iss_screen.shape("iss.gif")
    # iss_screen.setheading(180)
    iss_screen.penup()
    # print(longitude, latitude)
    iss_screen.goto(float(longitude), float(latitude))
    screen.exitonclick()


def main():
    print("~~~Part A: Get Astronauts~~~")
    get_astronauts()
    print("~~~Part B: Geographic Coordinates~~~")
    geographic_coordinates()
    print("~~~Part C: ISS Coordinates~~~")
    iss_coordinates()


if __name__ == '__main__':
    main()
