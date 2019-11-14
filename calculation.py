"""

        Author : MP Gopani <Mitul.Gopani@dlr.de>

        This script contains calculations and plotting of the final result of infrastructure model

"""
import numpy as np
import matplotlib.pyplot as plt
import var_vehicle

# Access time model ****************************************************************************************************
# Short distance access time

var_vehicle.car.set_access_time(var_vehicle.car.city_spd)
var_vehicle.taxi.set_access_time(var_vehicle.taxi.city_spd)
var_vehicle.bus.set_access_time(var_vehicle.bus.city_spd)
var_vehicle.pt.set_access_time(var_vehicle.pt.city_spd)
var_vehicle.bicycle.set_access_time(var_vehicle.bicycle.city_spd)
var_vehicle.walk.set_access_time(var_vehicle.walk.city_spd)

if var_vehicle.walk.str_distance < 1.5:
    dtv_time = np.array([var_vehicle.car.dtv_time, var_vehicle.taxi.dtv_time, var_vehicle.bus.dtv_time,
                         var_vehicle.pt.dtv_time, var_vehicle.bicycle.dtv_time, var_vehicle.walk.dtv_time])
    wat_time = np.array([var_vehicle.car.wat_time, var_vehicle.taxi.wat_time, var_vehicle.bus.wat_time,
                         var_vehicle.pt.wat_time, var_vehicle.bicycle.wat_time, var_vehicle.walk.wat_time])
    str_time = np.array([var_vehicle.car.str_time, var_vehicle.taxi.str_time, var_vehicle.bus.str_time,
                         var_vehicle.pt.str_time, var_vehicle.bicycle.str_time, var_vehicle.walk.str_time])
    prk_time = np.array([var_vehicle.car.prk_time, var_vehicle.taxi.prk_time, var_vehicle.bus.prk_time,
                         var_vehicle.pt.prk_time, var_vehicle.bicycle.prk_time, var_vehicle.walk.prk_time])
    ptr_time = np.array([var_vehicle.car.ptr_time, var_vehicle.taxi.ptr_time, var_vehicle.bus.ptr_time,
                         var_vehicle.pt.ptr_time, var_vehicle.bicycle.ptr_time, var_vehicle.walk.ptr_time])
    ad_wat_time = np.array([var_vehicle.car.ad_wat_time, var_vehicle.taxi.ad_wat_time, var_vehicle.bus.ad_wat_time,
                            var_vehicle.pt.ad_wat_time, var_vehicle.bicycle.ad_wat_time, var_vehicle.walk.ad_wat_time])

    N_gp = 6
    fig, ax = plt.subplots()
    ind = np.arange(N_gp)
    obj1 = ["Car", "Taxi", "Bus", "public transport", "Bicycle", "Walk"]
    textstr1 = '\n'.join(("Distance = %.3f km" % var_vehicle.car.str_distance,))
    props = dict(boxstyle="round", facecolor="white", alpha=0.5)
    ax.text(0.05, 0.95, textstr1, transform=ax.transAxes, verticalalignment="top", bbox=props)
    p1 = plt.bar(ind, ad_wat_time, width=0.8, color='skyblue',
                 bottom=ptr_time + prk_time + str_time + wat_time + dtv_time)
    p2 = plt.bar(ind, ptr_time, width=0.8, color='violet', bottom=prk_time + str_time + wat_time + dtv_time)
    p3 = plt.bar(ind, prk_time, width=0.8, color='orange', bottom=str_time + wat_time + dtv_time)
    p4 = plt.bar(ind, str_time, width=0.8, color='red', bottom=wat_time + dtv_time)
    p5 = plt.bar(ind, wat_time, width=0.8, color='yellow', bottom=dtv_time)
    p6 = plt.bar(ind, dtv_time, width=0.8, color="grey")
    plt.ylabel("time (h)")
    plt.xlabel("Mode of Transport")
    plt.xticks(ind, obj1)
    plt.title("Access time of railway station")
    plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0], p6[0]), ("Waiting for train", "Parking/station to railway station",
                                                            "Parking", "Time on vehicle", "Waiting", "Door to Vehicle"),
               loc=1)

else:
    dtv_time = np.array([var_vehicle.car.dtv_time, var_vehicle.taxi.dtv_time, var_vehicle.bus.dtv_time,
                         var_vehicle.pt.dtv_time, var_vehicle.bicycle.dtv_time])
    wat_time = np.array([var_vehicle.car.wat_time, var_vehicle.taxi.wat_time, var_vehicle.bus.wat_time,
                         var_vehicle.pt.wat_time, var_vehicle.bicycle.wat_time])
    str_time = np.array([var_vehicle.car.str_time, var_vehicle.taxi.str_time, var_vehicle.bus.str_time,
                         var_vehicle.pt.str_time, var_vehicle.bicycle.str_time])
    prk_time = np.array([var_vehicle.car.prk_time, var_vehicle.taxi.prk_time, var_vehicle.bus.prk_time,
                         var_vehicle.pt.prk_time, var_vehicle.bicycle.prk_time])
    ptr_time = np.array([var_vehicle.car.ptr_time, var_vehicle.taxi.ptr_time, var_vehicle.bus.ptr_time,
                         var_vehicle.pt.ptr_time, var_vehicle.bicycle.ptr_time])
    ad_wat_time = np.array([var_vehicle.car.ad_wat_time, var_vehicle.taxi.ad_wat_time, var_vehicle.bus.ad_wat_time,
                            var_vehicle.pt.ad_wat_time, var_vehicle.bicycle.ad_wat_time])

    N_gp = 5
    fig, ax = plt.subplots()
    ind = np.arange(N_gp)
    obj1 = ["Car", "Taxi", "Bus", "public transport", "Bicycle", "Walk"]
    textstr1 = '\n'.join(("Distance = %.3f km" % var_vehicle.car.str_distance,))
    props = dict(boxstyle="round", facecolor="white", alpha=0.5)
    ax.text(0.05, 0.95, textstr1, transform=ax.transAxes, verticalalignment="top", bbox=props)
    p1 = plt.bar(ind, ad_wat_time, width=0.8, color='skyblue',
                 bottom=ptr_time + prk_time + str_time + wat_time + dtv_time)
    p2 = plt.bar(ind, ptr_time, width=0.8, color='violet', bottom=prk_time + str_time + wat_time + dtv_time)
    p3 = plt.bar(ind, prk_time, width=0.8, color='orange', bottom=str_time + wat_time + dtv_time)
    p4 = plt.bar(ind, str_time, width=0.8, color='red', bottom=wat_time + dtv_time)
    p5 = plt.bar(ind, wat_time, width=0.8, color='yellow', bottom=dtv_time)
    p6 = plt.bar(ind, dtv_time, width=0.8, color="grey")
    plt.ylabel("time (h)")
    plt.xlabel("Mode of Transport")
    plt.xticks(ind, obj1)
    plt.title("Access time of railway station")
    plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0], p6[0]), ("Waiting for train", "Parking/station to railway station",
                                                            "Parking", "Time on vehicle", "Waiting", "Door to Vehicle"),
               loc=1)

# Egress time model ****************************************************************************************************

var_vehicle.car.set_egress_time(var_vehicle.car.destination_city_spd)
var_vehicle.taxi.set_egress_time(var_vehicle.taxi.destination_city_spd)
var_vehicle.bus.set_egress_time(var_vehicle.bus.destination_city_spd)
var_vehicle.pt.set_egress_time(var_vehicle.pt.destination_city_spd)
var_vehicle.bicycle.set_egress_time(var_vehicle.bicycle.destination_city_spd)
var_vehicle.walk.set_egress_time(var_vehicle.walk.destination_city_spd)

if var_vehicle.walk.rte_distance < 1.5:
    destination_dtv_time = np.array([var_vehicle.car.dtv_time, var_vehicle.taxi.dtv_time, var_vehicle.bus.dtv_time,
                                     var_vehicle.pt.dtv_time, var_vehicle.bicycle.dtv_time, var_vehicle.walk.dtv_time])
    destination_wat_time = np.array([var_vehicle.car.wat_time, var_vehicle.taxi.wat_time, var_vehicle.bus.wat_time,
                                     var_vehicle.pt.wat_time, var_vehicle.bicycle.wat_time, var_vehicle.walk.wat_time])
    destination_rte_time = np.array([var_vehicle.car.rte_time, var_vehicle.taxi.rte_time, var_vehicle.bus.rte_time,
                                     var_vehicle.pt.rte_time, var_vehicle.bicycle.rte_time, var_vehicle.walk.rte_time])
    destination_prk_time = np.array([var_vehicle.car.prk_time, var_vehicle.taxi.prk_time, var_vehicle.bus.prk_time,
                                     var_vehicle.pt.prk_time, var_vehicle.bicycle.prk_time, var_vehicle.walk.prk_time])
    destination_ptr_time = np.array([var_vehicle.car.ptr_time, var_vehicle.taxi.ptr_time, var_vehicle.bus.ptr_time,
                                     var_vehicle.pt.ptr_time, var_vehicle.bicycle.ptr_time, var_vehicle.walk.ptr_time])

    N_gp = 6
    fig1, ax1 = plt.subplots()
    ind2 = np.arange(N_gp)
    obj2 = ["Car", "Taxi", "Bus", "public transport", "Bicycle", "Walk"]
    textstr2 = '\n'.join(("Car distance = %.3f km" % var_vehicle.car.rte_distance,))
    props = dict(boxstyle="round", facecolor="white", alpha=0.5)
    ax1.text(0.05, 0.95, textstr2, transform=ax.transAxes, verticalalignment="top", bbox=props)
    p11 = plt.bar(ind2, destination_dtv_time, width=0.8, color='violet',
                  bottom=(destination_prk_time + destination_rte_time
                          + destination_wat_time +
                          destination_ptr_time))
    p12 = plt.bar(ind2, destination_prk_time, width=0.8, color='orange', bottom=(destination_rte_time +
                                                                                 destination_wat_time +
                                                                                 destination_ptr_time))
    p13 = plt.bar(ind2, destination_rte_time, width=0.8, color='red',
                  bottom=destination_wat_time + destination_ptr_time)
    p14 = plt.bar(ind2, destination_wat_time, width=0.8, color='yellow', bottom=destination_ptr_time)
    p15 = plt.bar(ind2, destination_ptr_time, width=0.8, color="grey")
    plt.ylabel("time (h)")
    plt.xlabel("Mode of Transport")
    plt.xticks(ind2, obj2)
    plt.title("Egress time of railway station")
    plt.legend((p11[0], p12[0], p13[0], p14[0], p15[0]), ("Vehicle to door", "Parking", "Time on vehicle", "Waiting",
                                                          "Railway station to Parking/station"), loc=1)

else:
    destination_dtv_time = np.array([var_vehicle.car.dtv_time, var_vehicle.taxi.dtv_time, var_vehicle.bus.dtv_time,
                                     var_vehicle.pt.dtv_time, var_vehicle.bicycle.dtv_time])
    destination_wat_time = np.array([var_vehicle.car.wat_time, var_vehicle.taxi.wat_time, var_vehicle.bus.wat_time,
                                     var_vehicle.pt.wat_time, var_vehicle.bicycle.wat_time])
    destination_rte_time = np.array([var_vehicle.car.rte_time, var_vehicle.taxi.rte_time, var_vehicle.bus.rte_time,
                                     var_vehicle.pt.rte_time, var_vehicle.bicycle.rte_time])
    destination_prk_time = np.array([var_vehicle.car.prk_time, var_vehicle.taxi.prk_time, var_vehicle.bus.prk_time,
                                     var_vehicle.pt.prk_time, var_vehicle.bicycle.prk_time])
    destination_ptr_time = np.array([var_vehicle.car.ptr_time, var_vehicle.taxi.ptr_time, var_vehicle.bus.ptr_time,
                                     var_vehicle.pt.ptr_time, var_vehicle.bicycle.ptr_time])

    N_gp = 5
    fig1, ax1 = plt.subplots()
    ind2 = np.arange(N_gp)
    obj2 = ["Car", "Taxi", "Bus", "public transport", "Bicycle", "Walk"]
    textstr2 = '\n'.join(("Car distance = %.3f km" % var_vehicle.car.rte_distance,))
    props = dict(boxstyle="round", facecolor="white", alpha=0.5)
    ax1.text(0.05, 0.95, textstr2, transform=ax.transAxes, verticalalignment="top", bbox=props)
    p11 = plt.bar(ind2, destination_dtv_time, width=0.8, color='violet',
                  bottom=(destination_prk_time + destination_rte_time
                          + destination_wat_time +
                          destination_ptr_time))
    p12 = plt.bar(ind2, destination_prk_time, width=0.8, color='orange', bottom=(destination_rte_time +
                                                                                 destination_wat_time +
                                                                                 destination_ptr_time))
    p13 = plt.bar(ind2, destination_rte_time, width=0.8, color='red',
                  bottom=destination_wat_time + destination_ptr_time)
    p14 = plt.bar(ind2, destination_wat_time, width=0.8, color='yellow', bottom=destination_ptr_time)
    p15 = plt.bar(ind2, destination_ptr_time, width=0.8, color="grey")
    plt.ylabel("time (h)")
    plt.xlabel("Mode of Transport")
    plt.xticks(ind2, obj2)
    plt.title("Egress time of railway station")
    plt.legend((p11[0], p12[0], p13[0], p14[0], p15[0]), ("Vehicle to door", "Parking", "Time on vehicle", "Waiting",
                                                          "Railway station to Parking/station"), loc=1)

plt.show()
