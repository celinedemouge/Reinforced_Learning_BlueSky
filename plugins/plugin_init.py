""" Initialization plugin."""

import sys
import time
import createScn, demandExtraction
import dataDef as data
import dataRL
import numpy as np
import copy
import random
from bluesky import stack, sim


def init_plugin():
    """Initialization function of the plugin."""
    # Configuration parameters
    config = {
        "plugin_name": "INIT",
        "plugin_type": "sim",
        "update_interval": 3600,
    }

    stackfunctions = {
        # The command name for your function
        "INIT": [
            # A short usage string. This will be printed if one type HELP <name> in the BlueSky console
            "INIT",
            # A list of the argument types the function accepts. For a description of this, see ...
            "[]",
            # The name of the function in this plugin
            initSim,
            # a longer help text of your function.
            "Initialize the simulation with the right scenario.",
        ]
    }
    initSim()

    # init_plugin() should always return these two dicts.
    return config, stackfunctions


def initSim():
    """Initialize all the data."""
    stack.stack("HOLD")

    dataRL.nbIter += 1
    data.nextOrd = [0 for _ in range(6)]

    if dataRL.nbIter == 1:
        dataRL.conf_min = [-1 for _ in range(dataRL.nbRandom)]
        dataRL.fuel_min = [0 for _ in range(dataRL.nbRandom)]
        for i in range(dataRL.nbRandom):  # Creation of different training sets.
            la = []
            while la == []:
                i1 = 0 + random.randint(0, 5) if i != 0 else 0
                i2 = 100 + random.randint(-5, 5) if i != 0 else 2
                name = "test{}".format(i)
                la = createScn.create(i1, i2, name)
            data.l.append(la)

    data.aircraft = copy.deepcopy(data.l[dataRL.nbIter % dataRL.nbRandom])
    data.nbAircraft = len(data.aircraft)
    for i in range(data.nbAircraft):
        data.wtc[data.aircraft[i].callsign] = "D"
        data.index_aircraft[data.aircraft[i].callsign] = i
        data.aircraftForSearch[data.aircraft[i].callsign] = data.aircraft[i]

    data.orders = [-1 for _ in range(data.nbAircraft)]

    for f in data.aircraft:

        data.fuel_detail[f.callsign] = 0
        data.time_detail[f.callsign] = 0
        data.distance_detail[f.callsign] = 0

    data.states = [dataRL.State(nb_pattern(f)) for f in data.aircraft]
    data.fuel = 0

    data.conflicts = 0
    data.begHold = [-1 for _ in range(data.nbAircraft)]
    if dataRL.nbIter == 1:
        data.saving = np.zeros((dataRL.maxIter, 5))
        data.saving_d = np.zeros((dataRL.maxIter, 3))
        data.saving_t = np.zeros((dataRL.maxIter, 3))
        m = 10050000  # if maxOrder = 10
        n = 2
        print(n)
        print(m)
        dataRL.nbAction = n
        dataRL.Q = np.zeros((n, m))
        dataRL.Q1 = np.zeros((n, m))

    dataRL.lastAction = [0 for _ in range(data.nbAircraft)]
    dataRL.lastStates = copy.deepcopy(data.states)
    dataRL.lastlastAction = [0 for _ in range(data.nbAircraft)]
    dataRL.lastlastStates = copy.deepcopy(data.states)
    dataRL.orderUnderStudy = -1

    stack.stack("ASAS OFF")

    data.order_inv = [{} for _ in range(6)]
    data.merged = [False for _ in range(data.nbAircraft)]
    data.in_holding = [[] for _ in range(6)]

    dataRL.thingsDone = []
    k = dataRL.nbIter % dataRL.nbRandom

    stack.stack("IC test{}.scn".format(k))

    stack.stack("DELAY 00:00:00.3, FF")


def nb_pattern(f):
    """From a flight f, finds the pattern number."""
    r = f.RWY
    i = f.IAF
    n = -1
    if r in ["25R", "25L"]:
        if i in ["SLL", "CLE"]:
            n = 0
        else:
            n = 1
    elif r in ["07R", "07L"]:
        if i in ["SLL", "VLA"]:
            n = 2
        else:
            n = 3
    else:
        if i == "TOTKI":
            n = 4
        else:
            n = 5
    return n
