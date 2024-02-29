"""KKK"""
from json import loads

def radio_stations(stations: list):
    """stations"""
    data, stations, res = [], set(stations), []
    for _ in range(int(input())):
        data.append(loads(input()))
    while stations:
        data.sort(key=lambda x: len(set(x["Cities"]).intersection(stations)), reverse=True)
        current = data.pop(0)
        use_stations = set(current["Cities"]).intersection(stations)
        if not use_stations:
            break
        res.append(current["Name"])
        for town in use_stations:
            stations.remove(town)
    print(sorted(res))
radio_stations(loads(input()))
