import sys
import csv
import utils


# entry WP of the CTR
ENTRY_WP = [
    "ALBER",
    "BISBA",
    "CASPE",
    "GRAUS",
    "LOBAR",
    "OSTUR",
    "PUMAL",
    "MARTA",
    "MATEX",
    "VERSO",
    "NEPAL",
    "CLE",
    "*4CLE",
    "RAVAX",
    "RULOS",
    "TEBLA",
    "SOTIL",
    "SLL",
    "VIBIM",
    "VLA",
]


class Flight:
    """Class which represents a flight"""

    def __init__(
        self, aobt_, callsign_, aircraftType_, entryWP_, timeOver_, RWY_, IAF_
    ):
        self.aobt = aobt_
        self.callsign = callsign_
        self.aircraftType = aircraftType_
        self.entryWP = entryWP_
        self.timeOver = timeOver_
        self.RWY = RWY_
        self.IAF = IAF_

    def addRWY(self, RWY_):
        self.RWY = RWY_

    def __str__(self):
        return " {}, {}, AOBT = {}, WP = {}, TIME = {}, IAF ={}".format(
            self.callsign,
            self.aircraftType,
            self.aobt,
            self.entryWP,
            self.timeOver,
            self.IAF,
        )


def extractData(csvfilename):
    """Extract data from a csv file"""
    data = []
    lastCallSign = ""
    with open(csvfilename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # If the linehas not been processed and has an entry WP as WP
            if row["ac_id"] != lastCallSign and row["wpt_name"] in ENTRY_WP:
                lastCallSign = row["ac_id"]
                flight = Flight(
                    row["aobt"],
                    row["ac_id"],
                    row["ac_type"],
                    row["wpt_name"],
                    row["time_over"],
                    row["arrival_runway"][4:],
                    utils.get_IAF(row["arrival_runway"][4:], row["wpt_name"]),
                )

                data.append(flight)

    return data
