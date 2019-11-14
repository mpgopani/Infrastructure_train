"""

        Author : MP Gopani <Mitul.Gopani@dlr.de>

        This script contains all required input for user to model infrastructure
"""

import dataframe

origin_city = input("Please enter city of origin : ")
# check if given city name is in the data frame (German_city_town.xlsx)
while True:
    try:
        a = dataframe.city_ls.loc[origin_city]
        break
    except KeyError:
        print("No origin city found in the list")
        print("Case sensitive, please check your city name with following list")
        print("Available city name are as follow: ")
        print(dataframe.city_ls.index.tolist())
        origin_city = input("Please enter valid city name for origin : ")

destination_city = input("Please enter city of destination : ")
# check if given city name is in the data frame (German_city_town.xlsx)while True:
while True:
    try:
        a = dataframe.city_ls.loc[destination_city]
        break
    except KeyError:
        print("No destination city found in the list")
        print("Case sensitive, please check your city name with following list")
        print("Available city name are as follow: ")
        print(dataframe.city_ls.index.tolist())
        destination_city = input("Please enter valid city name for destination : ")
