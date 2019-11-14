"""

        Author : MP Gopani <Mitul.Gopani@dlr.de>

        This script contains all the variables of vehicle class, those are used in the model of infrastructure
"""

import var_city
from vehicle import Vehicle

car = Vehicle()
taxi = Vehicle()
bus = Vehicle()
pt = Vehicle()  # public transport other than bus
bicycle = Vehicle()
walk = Vehicle()

car.name = "Car"
taxi.name = "Taxi"
bus.name = "Bus"
pt.name = "Public Transport"
bicycle.name = "Bicycle"
walk.name = "Walk"

car.city_spd = car.get_city_speed("car/taxi (kmph)", var_city.origin.population)
taxi.city_spd = taxi.get_city_speed("car/taxi (kmph)", var_city.origin.population)
bus.city_spd = bus.get_city_speed("bus (kmph)", var_city.origin.population)
pt.city_spd = pt.get_city_speed("public transport (kmph)", var_city.origin.population)
bicycle.city_spd = bicycle.get_city_speed("bicycle (kmph)", var_city.origin.population)
walk.city_spd = walk.get_city_speed("walk (kmph)", var_city.origin.population)

car.destination_city_spd = car.get_city_speed("car/taxi (kmph)", var_city.destination.population)
taxi.destination_city_spd = taxi.get_city_speed("car/taxi (kmph)", var_city.destination.population)
bus.destination_city_spd = bus.get_city_speed("bus (kmph)", var_city.destination.population)
pt.destination_city_spd = pt.get_city_speed("public transport (kmph)", var_city.destination.population)
bicycle.destination_city_spd = bicycle.get_city_speed("bicycle (kmph)", var_city.destination.population)
walk.destination_city_spd = walk.get_city_speed("walk (kmph)", var_city.destination.population)

car.dtv_time = 2 / 60  # 3 minutes converted into hours "ASSUMPTION"
taxi.dtv_time = 3 / 60  # 5 minutes converted into hours "ASSUMPTION"
bus.dtv_time = 5 / 60  # 7 minutes converted into hours "ASSUMPTION"
pt.dtv_time = 5 / 60  # 15 minutes converted into hours "ASSUMPTION"
bicycle.dtv_time = 2 / 60  # 2 minutes converted into hours "ASSUMPTION"
walk.dtv_time = 0

car.wat_time = 0
taxi.wat_time = 3 / 60  # "ASSUMPTION"
bus.wat_time = 3 / 60  # "ASSUMPTION"
pt.wat_time = 3 / 60  # "ASSUMPTION"
bicycle.wat_time = 0
walk.wat_time = 0

car.prk_time = 5 / 60  # "ASSUMPTION"
taxi.prk_time = 0
bus.prk_time = 0
pt.prk_time = 0
bicycle.prk_time = 3 / 30  # "ASSUMPTION"
walk.prk_time = 0

car.ptr_time = 5 / 60  # "ASSUMPTION"
taxi.ptr_time = 2 / 60  # "ASSUMPTION"
bus.ptr_time = 5 / 60  # "ASSUMPTION"
pt.ptr_time = 5 / 60  # "ASSUMPTION"
bicycle.ptr_time = 2 / 60  # "ASSUMPTION"
walk.ptr_time = 0

car.ad_wat_time = 10 / 60  # "ASSUMPTION"
taxi.ad_wat_time = 10 / 60  # "ASSUMPTION"
bus.ad_wat_time = 10 / 60  # "ASSUMPTION"
pt.ad_wat_time = 10 / 60  # "ASSUMPTION"
bicycle.ad_wat_time = 10 / 60   # "ASSUMPTION"
walk.ad_wat_time = 10 / 60  # "ASSUMPTION"
