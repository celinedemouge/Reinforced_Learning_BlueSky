import demandExtraction


# flight data
aircraft = []
nbAircraft = 0
# different training sets to avoid overfitting
l = []
# find a flight object from its callsign
aircraftForSearch = {}
# find the index of a flight in the aircraft list from its callsign
index_aircraft = {}


fuel = 0
delta_fuel = 0
# fuel consumption for each flight
fuel_detail = {}
# holding time for each flight
time_detail = {}
# holding distance for each flight
distance_detail = {}

# saving data for plot
saving = None
saving_d = None
saving_t = None

# states for each flight as 1 state <-> 1 flight
states = []


conflicts = 0

# date of the holding beginning for each flight
begHold = []

# next order to give for each pattern
nextOrd = []
# orders of each aircraft
orders = []
# from the order, find the aircraft
order_inv = {}


# wtc of each flight
wtc = {}
# time separation
wtc_t = {
    ("SH", "H"): 1.5,
    ("SH", "M"): 3,
    ("SH", "L"): 4,
    ("SH", "SH"): 1.5,
    ("SH", "D"): 4,
    ("H", "H"): 1.5,
    ("H", "M"): 2,
    ("H", "L"): 3,
    ("H", "SH"): 1.5,
    ("M", "L"): 3,
    ("M", "M"): 1.5,
    ("M", "H"): 1.5,
    ("M", "SH"): 1.5,
    ("L", "L"): 1.5,
    ("L", "M"): 1.5,
    ("L", "H"): 1.5,
}


# in case of problem in the simulation
falseIter = []
falseIter_nb = 0

# True if aircraft has merged
merged = []
# aircraft in holding for each pattern
in_holding = [[], [], [], [], [], []]
# all aircraft in holding
in_holding_g = []
