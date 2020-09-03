def to_decimal(d, m, s):
    """from degree, minute, second coordinates to decimal ones"""
    return d + m / 60 + s / 3600


WP = {
    "ALBER": (to_decimal(42, 27, 5), to_decimal(2, 49, 56)),
    "BISBA": (to_decimal(42, 5, 11), to_decimal(3, 37, 33)),
    "CASPE": (to_decimal(41, 16, 6), to_decimal(0, 11, 58)),
    "GRAUS": (to_decimal(41, 58, 45), to_decimal(0, 22, 35)),
    "LOBAR": (to_decimal(41, 44, 53), to_decimal(0, 19, 6)),
    "OSTUR": (to_decimal(40, 46, 51), to_decimal(2, 53, 38)),
    "PUMAL": (to_decimal(42, 22, 1), to_decimal(2, 0, 30)),
    "MARTA": (to_decimal(40, 21, 17), to_decimal(1, 16, 48)),
    "MATEX": (to_decimal(40, 33, 24), to_decimal(0, 15, 56)),
    "VERSO": (to_decimal(41, 9, 11), to_decimal(3, 45, 25)),
    "NEPAL": (to_decimal(40, 41, 34), to_decimal(1, 55, 29)),
    "CLE": (to_decimal(41, 38, 24), to_decimal(2, 38, 4)),
    "*4CLE": (0, 0),
    "RAVAX": (to_decimal(40, 55, 14), to_decimal(2, 5, 17)),
    "RULOS": (to_decimal(41, 10, 38), to_decimal(2, 16, 53)),
    "TEBLA": (0, 0),
    "SOTIL": (0, 0),
    "SLL": (to_decimal(41, 31, 12), to_decimal(2, 6, 35)),
    "VIBIM": (to_decimal(41, 4, 15), to_decimal(2, 12, 23)),
    "VLA": (to_decimal(41, 20, 33), to_decimal(1, 32, 52)),
}

RWY = ["25R", "25L", "07R", "07L", "02"]

WP_IAF = {
    "ALBER": ["CLE", "CLE", "SLL", "SLL", "VBIM"],
    "BISBA": ["CLE", "CLE", "SLL", "SLL", "VIBIM"],
    "CASPE": ["SLL", "SLL", "RUBOT", "RUBOT", "TOTKI"],
    "GRAUS": ["SLL", "SLL", "RUBOT", "RUBOT", "TOTKI"],
    "LOBAR": ["SLL", "SLL", "VLA", "VLA", "TOTKI"],
    "OSTUR": ["LESBA", "LESBA", "VIBIM", "VIBIM", "VIBIM"],
    "PUMAL": ["", "", "SLL", "SLL", "VIBIM"],
    "MARTA": ["SLL", "SLL", "VLA", "VLA", ""],
    "MATEX": ["SLL", "SLL", "VLA", "VLA", ""],
    "VERSO": ["LESBA", "LESBA", "", "", ""],
    "NEPAL": ["RULOS", "RULOS", "RUBOT", "RUBOT", ""],
    "CLE": ["CLE", "CLE", "CLE", "CLE", "CLE"],
    "*4CLE": ["", "", "", "", ""],
    "RAVAX": ["", "", "", "", ""],
    "RULOS": ["RULOS", "RULOS", "", "", ""],
    "TEBLA": ["", "", "", "", ""],
    "SOTIL": ["", "", "", "", ""],
    "SLL": ["SLL", "SLL", "", "", ""],
    "VLA": ["", "", "VLA", "VLA", ""],
    "VIBIM": ["VBIM", "VBIM", "VBIM", "VBIM", "VBIM"],
}


def get_IAF(rwy, wp):
    """Return the IAF in function of the runway and the entry waypoint"""
    iaf = ""
    if rwy in ["25R", "25L"]:
        iaf = WP_IAF[wp][0]
        print(iaf)
    elif rwy in ["07R", "07L"]:
        iaf = WP_IAF[wp][2]
    elif rwy == "02":
        iaf = WP_IAF[wp][4]
    return iaf
