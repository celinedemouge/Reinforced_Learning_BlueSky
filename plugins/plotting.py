import dataDef as data
import dataRL
import matplotlib.pyplot as plt


def plotting():
    """plotting function : plots conflicts, fuel, holding duration, holding distance and Q norm in function of iterations"""

    l_fuel_min = [data.saving[i - 1, 3] for i in range(1, dataRL.maxIter)]
    l_fuel_max = [data.saving[i - 1, 4] for i in range(1, dataRL.maxIter)]
    l_fuel = [data.saving[i - 1, 0] for i in range(1, dataRL.maxIter)]
    l_conflicts = [data.saving[i - 1, 1] for i in range(1, dataRL.maxIter)]
    l_q = [data.saving[i - 1, 2] for i in range(1, dataRL.maxIter)]

    nb_ac = input("Nb aircraft ? \n")

    # Fuel figure
    plt.figure()
    plt.title("Fuel consumption ({} aircraft)".format(nb_ac))
    plt.xlabel("Iterations")
    plt.ylabel("Fuel consumption (kg)")
    plt.grid(True)

    plt.plot(l_fuel, color="red", label="Mean fuel consumption")
    plt.plot(l_fuel_max, color="green", label="Max fuel consumption")
    plt.plot(l_fuel_min, color="blue", label="Min fuel consumption")
    plt.legend()

    # Conflicts figure
    plt.figure()
    plt.title("Conflict detection ({} aircraft)".format(nb_ac))
    plt.xlabel("Iterations")
    plt.ylabel("Detected conflicts")
    plt.grid(True)

    plt.plot(l_conflicts, color="red")

    # Q figure
    plt.figure()
    plt.title("Q norm ({} aircraft)".format(nb_ac))
    plt.xlabel("Iterations")
    plt.ylabel("Q norm")
    plt.grid(True)

    plt.plot(l_q)

    # Time figure
    plt.figure()
    plt.title("Time between IAF and the RWY")
    plt.grid(True)
    plt.plot([data.saving_t[i - 1, 0] for i in range(1, dataRL.maxIter)])
    plt.plot([data.saving_t[i - 1, 1] for i in range(1, dataRL.maxIter)])
    plt.plot([data.saving_t[i - 1, 2] for i in range(1, dataRL.maxIter)])

    # Distance figure
    plt.figure()
    plt.title("Distance between IAF and the RWY")
    plt.grid(True)
    plt.plot([data.saving_d[i - 1, 0] for i in range(1, dataRL.maxIter)])
    plt.plot([data.saving_d[i - 1, 1] for i in range(1, dataRL.maxIter)])
    plt.plot([data.saving_d[i - 1, 2] for i in range(1, dataRL.maxIter)])

    plt.show()
