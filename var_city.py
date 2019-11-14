"""

        Author : MP Gopani <Mitul.Gopani@dlr.de>

        This script contains all the variables of city and airport, those are used in the model of infrastructure
"""

import input
import fun
from city import City

origin = City(input.origin_city)
destination = City(input.destination_city)

origin.set_city_parameters()
destination.set_city_parameters()
start_lat, start_lon, hw_lat, hw_lon = fun.get_random_point(origin.lat, origin.lon, origin.radius)
end_lat, end_lon, destination_hw_lat, destination_hw_lon = fun.get_random_point(destination.lat, destination.lon,
                                                                                destination.radius)


