#!/usr/bin/env python

__author__ = "mhoelzer"


import requests
import time
import turtle


def print_astronauts():
    """"""
    url = "http://api.open-notify.org/astros.json"
    request = requests.get(url)
    req_data = request.json()
    print("There are currently {} astronauts in space.".format(
        req_data["number"]))
    for person in req_data["people"]:
        print("{} is currently aboard the {}.".format(
            person["name"], person["craft"]))


# def geographic_coordinates():
def get_iss_coordinates():
    url = "http://api.open-notify.org/iss-now.json"
    request = requests.get(url)
    req_data = request.json()
    longitude = req_data["iss_position"]["longitude"]
    latitude = req_data["iss_position"]["latitude"]
    timestamp = time.ctime(req_data["timestamp"])
    print("Longitude: {}".format(longitude))
    print("Latitude: {}".format(latitude))
    print("Timestamp: {}".format(timestamp))
    return (longitude, latitude, timestamp)


def setup_screen():
    # lon, lat, timestamp = geographic_coordinates()
    screen = turtle.Screen()
    screen.setup(width=720, height=360, startx=None, starty=None)
    screen.bgpic("map.gif")
    screen.setworldcoordinates(-180, -90, 180, 90)
    return screen


def show_iss(screen, lat, lon):
    iss = turtle.Turtle()
    screen.register_shape("iss.gif")
    iss.shape("iss.gif")
    iss.setheading(90)
    iss.penup()
    iss.goto(float(lon), float(lat)) # goto expects screen coor


def get_rise_time(lat, lon):
    url = "http://api.open-notify.org/iss-pass.json"
    payload = {"lat": lat, "lon": lon}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    req_data = response.json()
    # print(req_data)
    timestamp = req_data["response"][0]["risetime"]
    return timestamp


def show_dot(lat, lon, timestamp):
    # Assumes that screen is already setup
    indy_dot = turtle.Turtle()
    indy_dot.penup()
    indy_dot.color("yellow")
    indy_dot.goto(lon, lat)
    indy_dot.dot(5)
    # indy_dot.shape("circle")
    indy_dot.hideturtle()
    indy_dot.write(time.ctime(timestamp))


def main():
    # setup screen stuff
    screen = setup_screen()

    print("~~~Part A: Get Astronauts~~~")
    print_astronauts()
    # print(astro_data)

    print("~~~Part B: Geographic Coordinates~~~")
    longitude, latitude, timestamp = get_iss_coordinates()
    # print coords

    print("~~~Part C: ISS Coordinates~~~")
    show_iss(screen, latitude, longitude)
    print("See popup")

    print("~~~Part D: Indianapolis Coordinates~~~")
    indy_lat = 39.7684
    indy_long = -86.1581
    risetime = get_rise_time(indy_lat, indy_long)
    show_dot(indy_lat, indy_long, risetime)
    # show indy risetime

    # CLEANUP SCREEN STUFF
    print("Click on map to exit")
    screen.exitonclick()


if __name__ == '__main__':
    main()
