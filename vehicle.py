"""

        Author : MP Gopani <Mitul.Gopani@dlr.de>

        This script contains class named vehicle, having parameters like city speed, highway speed, time etc. and
        required function for infrastructure model

"""

import dataframe
import var_city
import fun


class Vehicle:

    def __init__(self):
        self.vehicle_type = None  # type of the vehicle
        self.city_spd = None  # vehicle speed inside the origin city (kmph)
        self.destination_city_spd = None  # vehicle speed inside the destination city (kmph)
        self.str_distance = None  # starting point to railway station distance
        self.dtv_time = None  # door to vehicle time (h)
        self.wat_time = None  # waiting time (h) (eg for bus, taxi, tram etc)
        self.str_time = None  # starting point to railway station time in the vehicle (h)
        self.prk_time = None  # parking time (h) (eg for private car)
        self.ptr_time = None  # parking or vehicle stop to railway station time (h)
        self.ad_wat_time = None  # additional waiting time at railway station (h)
        self.access_time = None  # access time for the airport (h)
        self.rte_distance = None  # railway station to end point distance for egress time (km)
        self.rte_time = None  # airport to end point time for egress model (h)
        self.egress_time = None  # egress time of the airport (h)

    def get_city_speed(self, mode_of_transport, population):
        """
            extract speed information of the vehicle inside the city depending on city population

            :param mode_of_transport: Mode of transport
            :param population: population of the city

            :return: speed of given mode of transport
        """

        if mode_of_transport == "car/taxi (kmph)":
            if population < 250000:
                return dataframe.vehicle_spd.iloc[0, 1]
            elif 250000 < population < 500000:
                return dataframe.vehicle_spd.iloc[0, 2]
            elif 500000 < population < 10000000:
                return dataframe.vehicle_spd.iloc[0, 3]
            elif 10000000 < population < 25000000:
                return dataframe.vehicle_spd.iloc[0, 4]
            else:
                return dataframe.vehicle_spd.iloc[0, 5]

        elif mode_of_transport == "public transport (kmph)":
            if population < 250000:
                return dataframe.vehicle_spd.iloc[1, 1]
            elif 250000 < population < 500000:
                return dataframe.vehicle_spd.iloc[1, 2]
            elif 500000 < population < 10000000:
                return dataframe.vehicle_spd.iloc[1, 3]
            elif 10000000 < population < 25000000:
                return dataframe.vehicle_spd.iloc[1, 4]
            else:
                return dataframe.vehicle_spd.iloc[1, 5]

        elif mode_of_transport == "bus (kmph)":
            if population < 250000:
                return dataframe.vehicle_spd.iloc[2, 1]
            elif 250000 < population < 500000:
                return dataframe.vehicle_spd.iloc[2, 2]
            elif 500000 < population < 10000000:
                return dataframe.vehicle_spd.iloc[2, 3]
            elif 10000000 < population < 25000000:
                return dataframe.vehicle_spd.iloc[2, 4]
            else:
                return dataframe.vehicle_spd.iloc[2, 5]

        elif mode_of_transport == "bicycle (kmph)":
            if population < 250000:
                return dataframe.vehicle_spd.iloc[3, 1]
            elif 250000 < population < 500000:
                return dataframe.vehicle_spd.iloc[3, 2]
            elif 500000 < population < 10000000:
                return dataframe.vehicle_spd.iloc[3, 3]
            elif 10000000 < population < 25000000:
                return dataframe.vehicle_spd.iloc[3, 4]
            else:
                return dataframe.vehicle_spd.iloc[3, 5]

        elif mode_of_transport == "walk (kmph)":
            if population < 250000:
                return dataframe.vehicle_spd.iloc[4, 1]
            elif 250000 < population < 500000:
                return dataframe.vehicle_spd.iloc[4, 2]
            elif 500000 < population < 10000000:
                return dataframe.vehicle_spd.iloc[4, 3]
            elif 10000000 < population < 25000000:
                return dataframe.vehicle_spd.iloc[4, 4]
            else:
                return dataframe.vehicle_spd.iloc[4, 5]

    def set_str_distance(self):
        """
            calculates city to airport distance

            :return: sets cta_distance (km)
        """
        self.str_distance = fun.get_distance_from_coordinates(var_city.start_lat, var_city.start_lon,
                                                              var_city.origin.lat, var_city.origin.lon)

    def set_rte_distance(self):
        """
            calculates airport to city distance for egress part of the model

            :return: sets atc_distance (km)
        """
        self.rte_distance = fun.get_distance_from_coordinates(var_city.destination.lat, var_city.destination.lon,
                                                              var_city.end_lat, var_city.end_lon)

    def set_access_time(self, city_spd):
        """
            calculates and sets the access time for airport (starting point to boarding)

            :param city_spd: vehicle speed in the origin city (kmph)

            :return: sets the access_time (h)
        """
        self.set_str_distance()
        self.str_time = fun.get_time(self.str_distance, city_spd)
        self.access_time = (self.dtv_time + self.wat_time + self.str_time + self.prk_time + self.ptr_time +
                            self.ad_wat_time)

    def set_egress_time(self, city_spd):
        """
            calculates and sets the egress time for airport (landing to home)

            :param city_spd : vehicle speed inside the destination city (kmph)

            :return: sets the egress_time (h)
        """
        self.set_rte_distance()
        self.rte_time = fun.get_time(self.rte_distance, city_spd)
        self.egress_time = self.ptr_time + self.wat_time + self.rte_time + self.prk_time + self.dtv_time
