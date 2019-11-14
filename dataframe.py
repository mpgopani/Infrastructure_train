"""

        Author : MP Gopani <Mitul.Gopani@dlr.de>

        This script contains all the data frame those are used in the model of infrastructure
"""

import pandas as pd

# Data for German cities, their area and coordinates *******************************************************************
# http://worldpopulationreview.com/countries/germany-population/cities/
city_ls = pd.read_excel("German_city_town.xlsx")  # data frame of all german cities, area and coordinates
city_ls.set_index("Name", inplace=True)
city_ls = city_ls.fillna(0)  # set all nan values to 0

# Data for vehicle speed depending on population of the city ***********************************************************
# https://elib.dlr.de/124382/1/TransportationResearch_MobilTUM_DLR_Viergutz_Krajzewicz_Travel_Time_20180814.pdf
vehicle_spd = pd.read_excel("mode_of_transport.xlsx")
