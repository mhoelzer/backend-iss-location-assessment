#!/usr/bin/env python

__author__ = "mhoelzer"


import requests
import time
import turtle


def print_astronauts():
    """prints astronauts info"""
    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)
    res_data = response.json()
    print("There are currently {} astronauts in space.".format(
        res_data["number"]))
    for person in res_data["people"]:
        print("{} is currently aboard the {}.".format(
            person["name"], person["craft"]))


def get_iss_coordinates():
    """finds iss coordinates (lon, lat, timestamp)"""
    url = "http://api.open-notify.org/iss-now.json"
    request = requests.get(url)
    res_data = request.json()
    latitude = res_data["iss_position"]["latitude"]
    longitude = res_data["iss_position"]["longitude"]
    timestamp = time.ctime(res_data["timestamp"])
    print("Latitude: {}".format(latitude))
    print("Longitude: {}".format(longitude))
    print("Timestamp: {}".format(timestamp))
    return (longitude, latitude, timestamp)


def setup_screen():
    """creates the map screen to put iss and indy on map"""
    screen = turtle.Screen()
    screen.setup(width=720, height=360, startx=None, starty=None)
    screen.bgpic("map.gif")
    screen.setworldcoordinates(-180, -90, 180, 90)
    return screen


def show_iss(screen, lat, lon):
    """puts iss location on map"""
    iss = turtle.Turtle()
    screen.register_shape("iss.gif")
    iss.shape("iss.gif")
    iss.setheading(90)
    iss.penup()
    iss.goto(float(lon), float(lat))  # goto expects screen coors


def get_rise_time(lat, lon):
    """finds the time"""
    url = "http://api.open-notify.org/iss-pass.json"
    payload = {"lat": lat, "lon": lon}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    res_data = response.json()
    timestamp = res_data["response"][0]["risetime"]
    return timestamp


def show_dot(lat, lon, timestamp):
    """puts indy dot on the map along with the timestamp"""
    # Assumes that screen is already setup
    indy_dot = turtle.Turtle()
    indy_dot.penup()
    indy_dot.color("yellow")
    indy_dot.goto(lon, lat)
    indy_dot.dot(5)
    indy_dot.hideturtle()
    indy_dot.write(time.ctime(timestamp))


def main():
    """creates the screen and runs all the functions"""
    # setup screen stuff
    screen = setup_screen()

    print("~~~Part A: Get Astronauts~~~")
    print_astronauts()

    print("~~~Part B: Geographic Coordinates~~~")
    longitude, latitude, timestamp = get_iss_coordinates()
    # coords get printed inside function

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
