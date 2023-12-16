"""KKK"""

def three_rain_down(position, durations):
    """https://open.spotify.com/track/2pB3TJsSleiRiL0NP6rtCw?si=9dbf1bf3ac43407a"""
    if position == "Outdoor":
        return True if durations >= 240 else False
    else:
        return True if durations >= 480 else False
print(three_rain_down(str(input()), float(input())))
