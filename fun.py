"""

        Author : MP Gopani <Mitul.Gopani@dlr.de>

        This script contains different functions those are used in infrastructure model
"""

from random import randrange
import math
import numpy as np
import dataframe


def get_random_point(lat, lon, radius):
    """"
        calculates coordinates of random point within a given radius and coordinates of the highway nearest to this
        random point. To calculate highway coordinates nearest to the random point, same theta is used, which is used
        to calculate the random point with city radius

        :param lat : latitude of city
        :param lon : longitude of city
        :param radius: radius of the city (km)


        :return: x and y coordinates of the random point within city radius and for highway coordinates
                    lat_new : latitude of the random point
                    lon_new : longitude of the random point
                    lat_hw : highway latitude
                    lon_hw : highway longitude
    """

    RADIUS_EARTH = 6371.0088  # Radius of the earth (km)
    max_theta = 360  # Maximum value of theta
    rnd_radius = -1  # not allowed value of radius
    theta = -1  # not allowed value of radius

    lat1 = math.radians(lat)
    lon1 = math.radians(lon)

    while rnd_radius < 0 and theta < 0:
        rnd_radius = (randrange(round(radius)) - 1) + (randrange(100) / 100)  # Radius for latitude of the random point
        theta = (randrange(max_theta) - 1) + \
                (randrange(100) / 100)  # random the theta for airport on the radius circle

    # https://stackoverflow.com/questions/7222382/get-lat-long-given-current-point-distance-and-bearing
    # coordinates for random point withing city at random angle
    lat_new = math.asin(math.sin(lat1) * math.cos(rnd_radius / RADIUS_EARTH) +
                        math.cos(lat1) * math.sin(rnd_radius / RADIUS_EARTH) * math.cos(theta))

    lon_new = lon1 + math.atan2(math.sin(theta) * math.sin(rnd_radius / RADIUS_EARTH) * math.cos(lat1),
                                math.cos(rnd_radius / RADIUS_EARTH) - math.sin(lat1) * math.sin(lat_new))

    lat_new = math.degrees(lat_new)
    lon_new = math.degrees(lon_new)

    # coordinates for highway (same theta but on the circumference of teh circle)
    lat_hw = math.asin(math.sin(lat1) * math.cos(radius / RADIUS_EARTH) +
                       math.cos(lat1) * math.sin(radius / RADIUS_EARTH) * math.cos(theta))

    lon_hw = lon1 + math.atan2(math.sin(theta) * math.sin(radius / RADIUS_EARTH) * math.cos(lat1),
                               math.cos(radius / RADIUS_EARTH) - math.sin(lat1) * math.sin(lat_hw))

    lat_hw = math.degrees(lat_hw)
    lon_hw = math.degrees(lon_hw)

    return float(lat_new), float(lon_new), float(lat_hw), float(lon_hw)


# This function is pasted here from gitlab
def get_distance_from_coordinates(lat1, lon1, lat2, lon2):
    """
        Return the distance between two points on earth using the Haversive formula.

        Args:
            lat1: Latitude of point 1 in degrees
            lon1: Longitude of point 1 in degrees
            lat2: Latitude of point 2 in degrees
            lon2: Longitude of point 2 in degrees

        Returns:
            Distance in kilometers as float
        """
    # Haversine formula
    RADIUS_EARTH = 6371008.8  # Radius of the earth (m)
    dlat = np.deg2rad(lat2 - lat1)
    dlon = np.deg2rad(lon2 - lon1)
    a = np.sin(dlat / 2) ** 2 + np.cos(np.deg2rad(lat1)) * np.cos(np.deg2rad(lat2)) * np.sin(dlon / 2) ** 2
    c = 2 * np.arcsin(np.sqrt(a))
    r = RADIUS_EARTH / 1000  # Radius of earth in kilometers
    return c * r


def get_time(distance, speed):
    """
        calculates time required for given distance and speed

        :param distance: distance of the trip (km)
        :param speed: speed of the vehicle (kmph)

        :return: time of the trip (h)
    """
    return distance / speed


def get_total_time(dtv_time, wat_time, time_on_vehicle, prk_time, pta_time):
    """
        calculates access time for the airport (starting point to boarding)

        :param dtv_time: door to vehicle time (h)
        :param wat_time: waiting for vehicle time (h)
        :param time_on_vehicle: time spend on the vehicle (h)
        :param prk_time: parking time (h)
        :param pta_time: parking/station to airport time(h)

        :return: access time of the airport (h)
    """
    return dtv_time + wat_time + time_on_vehicle + prk_time + pta_time
