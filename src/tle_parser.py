from sgp4.api import Satrec
from datetime import datetime
import pandas as pd

def parse_tle_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    sats = []
    for i in range(0, len(lines), 3):
        name = lines[i].strip()
        l1, l2 = lines[i+1], lines[i+2]
        sat = Satrec.twoline2rv(l1, l2)
        sats.append({
            "name": name,
            "epoch": sat.jdsatepoch,
            "inclo": sat.inclo,
            "eccentricity": sat.ecco,
            "raan": sat.nodeo,
            "argpo": sat.argpo,
            "mean_anomaly": sat.mo,
            "mean_motion": sat.no_kozai
        })
    return pd.DataFrame(sats)

