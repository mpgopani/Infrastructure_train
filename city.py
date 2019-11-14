"""

        Author : MP Gopani <Mitul.Gopani@dlr.de>

        This script contains class named city, having parameters like latitude, longitude, population etc. and required
        function for infrastructure model
"""


import math
import dataframe


class City:

    def __init__(self, name):
        self.name = name  # name of the city
        self.lat = None  # latitude of the city (°)
        self.lon = None  # longitude of the city (°)
        self.population = None  # population of teh city
        self.area = None  # area of the city (km^2)
        self.radius = None  # radius of the city

    def get_area(self):
        """
            extract the area value of the given city. If area information for given city is not found then it will take
            fixed value of area which is 78.5, which yields out radius of 5 km

        :return: area of the city (km^2)
        """
        if dataframe.city_ls.loc[self.name, "Area (km^2)"] == 0:
            return 78.5  # 78.5 gives radius value of 5 km (for small cities having no data of area)
        else:
            return dataframe.city_ls.loc[self.name, "Area (km^2)"]

    def get_radius(self, area):
        """
            calculates the radius of the city from area

            :param area: area of the city (km^2)

            :return: radius of the city (km)
        """
        return math.sqrt(area / math.pi)

    def set_city_parameters(self):
        """
            set the parameters of the city class

            :return: different parameters of the city class
        """
        self.lat = dataframe.city_ls.loc[self.name, "Latitude"]
        self.lon = dataframe.city_ls.loc[self.name, "Longitude"]
        self.population = dataframe.city_ls.loc[self.name, "population"]
        self.area = self.get_area()
        self.radius = self.get_radius(self.area)
